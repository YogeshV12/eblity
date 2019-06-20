from django.shortcuts import render, redirect
from .models import Plan_Table, Subtopic_Table, Topic_Table, Journey_template, Resources, Attendance_Table, Student_Table
import json
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from datetime import date
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def plan_view(request):
   if (request.method == 'POST'):
      if(request.POST.get("go_to_journey") == "1"):
         print("go to journey page")
         return HttpResponseRedirect('/plan/journey')
      else:
         print("printing data")
         sequence_info = json.loads(request.POST.get('sequence'))
         print(sequence_info)
         for i, data in enumerate(sequence_info):
            obj = Plan_Table.objects.get(topic_id = Topic_Table.objects.get(topic_id = int(data)))
            obj.sequence = i + 1
            obj.save()
         print("page refressed")
         return redirect('/plan')
   else:
      count = Plan_Table.objects.all().count()
      print("else condition")
      obj = []
      obj2 = []
      query_set = Plan_Table.objects.all().order_by('sequence')
      for data in query_set:
         obj.append(data)
      for i in range(count):
         count2 = Subtopic_Table.objects.filter(topic_id=i + 1).count()
         for j in range(count2):
            obj2.append(Subtopic_Table.objects.get(topic_id=i+1, subtopic_id=j+1))

      context = {
         'object': obj,
         'object2' : obj2
      }

      return render(request, 'plans.html', context)


def Journey_view(request):
    if (request.method == 'POST'):
        if(request.POST.get("go_to_journey") == "1"):
            print("got the data")
            global student_id, topic_id, subtopic_id
            student_id = int(json.loads(request.POST.get('journey'))[0])
            topic_id = int(json.loads(request.POST.get('journey'))[1])
            subtopic_id = int(json.loads(request.POST.get('journey'))[2])
            print(student_id, topic_id, subtopic_id)
            if (Journey_template.objects.filter(student_id = student_id, topic_id = Topic_Table.objects.get(topic_id=topic_id), subtopic_id=subtopic_id).exists()):
                print("second time")
                return view_journey_page(request, student_id, topic_id, subtopic_id)
            else:
                print("first time")
                obj = Resources.objects.filter(topic_id=Topic_Table.objects.get(topic_id=topic_id), subtopic_id=subtopic_id)
                for resource in obj:
                    Journey_template(student_id = student_id, subtopic_id=resource.subtopic_id, resource_id=resource,
                                     topic_id=Topic_Table.objects.get(topic_id=topic_id)).save()
                return view_journey_page(request, student_id, topic_id, subtopic_id)

        elif(request.POST.get("add_resources")=='1'):
            pending_info =json.loads(request.POST.get('pending_ids'))
            print(pending_info)
            for data in pending_info:
                Journey_template(student_id=student_id, resource_id= Resources.objects.get(resource_id=int(data['resource_id'])), subtopic_id=int(data['subtopic_id']), topic_id=Topic_Table.objects.get(topic_id=int(data['topic_id']))).save()
                return view_journey_page(request, student_id, topic_id, subtopic_id)
        else:
            print("printing data")
            pending_info =json.loads(request.POST.get('pending_ids'))
            skipped_info =json.loads(request.POST.get('skipped_ids'))
            completed_info = json.loads(request.POST.get('completed_ids'))
            for data in pending_info:
                obj = Journey_template.objects.get(journey_template_key=int(data['journey_template_key']))
                obj.status = str(data['status'])
                obj.save()
            for data in skipped_info:
                obj = Journey_template.objects.get(journey_template_key=int(data['journey_template_key']))
                obj.status = str(data['status'])
                obj.save()
            for data in completed_info:
                obj = Journey_template.objects.get(journey_template_key=int(data['journey_template_key']))
                obj.status = str(data['status'])
                obj.rating = int(data['rating'])
                obj.feedback = str(data['feedback'])
                obj.save()
            return view_journey_page(request, student_id, topic_id, subtopic_id)
    else:
        print("else")
        return view_journey_page(request, student_id, topic_id, subtopic_id)


def view_journey_page(request, student_id, topic_id, subtopic_id):
        topic_name = Topic_Table.objects.get(topic_id = topic_id).topic_name
        subtopic_name = Subtopic_Table.objects.get(topic_id = topic_id, subtopic_id = subtopic_id).subtopic_name
        print(topic_name, subtopic_name)
        completed_obj = Journey_template.objects.filter(student_id = student_id, topic_id = topic_id, subtopic_id=subtopic_id, status='completed')
        pending_obj = Journey_template.objects.filter(student_id = student_id, topic_id = topic_id,subtopic_id=subtopic_id, status='pending')
        skipped_obj = Journey_template.objects.filter(student_id = student_id, topic_id = topic_id,subtopic_id=subtopic_id, status='skipped')
        all_obj = Resources.objects.filter(topic_id = Topic_Table.objects.get(topic_id=topic_id),subtopic_id=subtopic_id)
        maximum = max([completed_obj.count(),pending_obj.count()+skipped_obj.count()])
        # print("return here")
        print(skipped_obj)
        print("max : ",maximum)
        return render(request,'journey-page.html',{'completed' : completed_obj, 'pending' : pending_obj, 'skipped' : skipped_obj, 'all_obj' : all_obj, 'max_length' : range(maximum), 'topic_name': topic_name, 'subtopic_name' : subtopic_name} )

def attendance_view(request):
  student_obj = Student_Table.objects.all()
  # Attendance_Table(student_id=student_obj[0], date="2016-06-20").save()
  if(request.method == 'POST'):
    if(request.POST.get("selected") == "1"):
      global date
      date = request.POST.get('select_date')
      print("select_date: ",date)
      check(date)
      obj = Attendance_Table.objects.filter(date=date)
      data = [d['fields'] for d in json.loads(serializers.serialize('json',obj))]
      print("data : ",data)
      # print("serialized data : ",serializers.serialize('json',obj))
      
      return JsonResponse({'obj' : data})
      # return render(request,'attendance.html', {'obj' : data})
  # elif request.method == 'GET':
  #   print("get request---------------------")
    elif (request.POST.get("update_data") == "1"):
      date = request.POST.get("selected_date")
      check(date)
      attendance_obj = Attendance_Table.objects.filter(date=date)
      print("attendance_obj : ",attendance_obj)
      return render(request,'attendance_content.html', {'obj' : attendance_obj})


  elif (request.method == 'GET'):
    date = datetime.now().strftime("%Y-%m-%d")
    print("date==============",date)
    print("Type------------: " ,type(date))
    check(date)
  attendance_obj = Attendance_Table.objects.filter(date=date)
  print("attendance_obj : ",attendance_obj)
  return render(request,'attendance.html', {'obj' : attendance_obj})

def check(date):
  student_obj = Student_Table.objects.all()
  for obj in student_obj:
    if(Attendance_Table.objects.filter(student_id=obj.student_id, date=date).exists()):
      print("exist")
    else:
      Attendance_Table(student_id=Student_Table.objects.get(student_id=obj.student_id), date=date).save() 


def index(request, data):
  print(date);