from django.shortcuts import render, redirect
from .models import Plan_Table, Subtopic_Table, Topic_Table, Journey_template, Resources
import json
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
  return render(request,'attendance.html')



# login system

def logout_view(request):
    return render(request,'logout.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('logout.html'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/plan')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})