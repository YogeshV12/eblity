from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import os
import signal
import subprocess

import pandas as pd
from django.views.decorators.csrf import csrf_exempt

from funtoot.models import Alerts, Comments, Interventions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. webpack")

# def schedule(request):
#     row = Buttons.objects.get(id=1)
#     data = {
#         'stitched_start': row.stitched_start,
#         'stitched_stop': row.stitched_stop,
#         'time_series_start': row.time_series_start,
#         'time_series_stop': row.time_series_stop
#     }
#     return render(request, 'schedule.html', data)

@csrf_exempt
def alert(request):
    # df = pd.read_csv('all_alerts.csv').to_dict('r')
    if request.method == 'POST':
        if (str(request.POST.get('add_intervention')) == "1"):
            print("add intervention")
            print("alert_id: ", int(request.POST.get('alert_id')))
            print("intv_id: ", int(request.POST.get('interv_id')))
            print("interv_type: ", int(request.POST.get('interv_type'))) 
            print(int(request.POST.get('asgn_to')))
            print(str(request.POST.get('follow_up_by')))
            print(int(request.POST.get('interv_status')))
            print(int(request.POST.get('rating')))
            if ((Interventions.objects.filter(alert_id =int(request.POST.get('alert_id')), interv_id = int(request.POST.get('interv_id')))).exists()):
                obj = Interventions.objects.get(alert_id =int(request.POST.get('alert_id')), interv_id = int(request.POST.get('interv_id'))) 
                print("update")
                obj = Interventions.objects.get(id = obj.id)
                obj.interv_type = int(request.POST.get('interv_type'))
                obj.asgn_to=int(request.POST.get('asgn_to')) 
                obj.follow_up_by=str(request.POST.get('follow_up_by'))
                obj.interv_status=int(request.POST.get('interv_status'))
                obj.rating = int(request.POST.get('rating'))
                obj.save(update_fields=['interv_type', 'asgn_to', 'follow_up_by', 'interv_status', 'rating'])
            else:
                Interventions(alert_id=int(request.POST.get('alert_id')), interv_id=int(request.POST.get('interv_id')), interv_type=int(request.POST.get('interv_type')), asgn_to=int(request.POST.get('asgn_to')), follow_up_by=str(request.POST.get('follow_up_by')), interv_status=int(request.POST.get('interv_status')), rating=int(request.POST.get('rating'))).save()
            
        if (str(request.POST.get('update_alert_id')) == "1"):
            obj = Alerts.objects.get(id=int(request.POST.get('id')))
            obj.status = int(request.POST.get('alert_id'))
            obj.save()
        if str(request.POST.get('post')) == "1":
            text = request.POST.get('comment')
            cmt_id = request.POST.get('id')
            Comments(cmt_id = int(cmt_id), text = str(text)).save()
            
        data = []
        data.append(Alerts.objects.get(id=int(request.POST.get('alert'))))
        data.append(Comments.objects.filter(cmt_id=int(request.POST.get('alert'))))
        data.append(Interventions.objects.filter(alert_id=int(request.POST.get('alert'))))
        return render(request, 'alert_details.html', {'data' : data})
    else:
        df = pd.read_csv('all_alerts.csv')
        for UserName, StudentName, Grade, Date, Concept, ConceptProgress, SubConcept, SubConceptProgress, PerSolved, AverageTimePerQuestion, LGD, LGR, PerLearningGapResolved, comment in zip(df['UserName'], df['StudentName'], df['Grade'], df['TimeSeries'], df['Concept'], df['ConceptProgress'], df['SubConcept'], df['SubConceptProgress'], df['PerSolved'], df['AverageTimePerQuestion'], df['LGD'], df['LGR'], df['PerLearningGapResolved'], df['comment']):
            if not (Alerts.objects.filter(UserName=str(UserName), SubConcept=str(SubConcept), comment=str(comment)).exists()):
                print("data doesnot exists")
                Alerts(UserName = str(UserName), StudentName = str(StudentName), Grade = int(Grade), Date = str(Date), Concept = str(Concept), ConceptProgress = int(ConceptProgress), SubConcept = str(SubConcept), SubConceptProgress = int(SubConceptProgress), PerSolved = int(PerSolved), AverageTimePerQuestion = int(AverageTimePerQuestion), LGD = int(LGD), LGR = int(LGR), PerLearningGapResolved = str(PerLearningGapResolved), comment = str(comment)).save()
        data = Alerts.objects.all().order_by('Date').reverse()
        paginator = Paginator(data,10)
        page = request.GET.get('page')
        data_var = paginator.get_page(page)
        return render(request, 'alert_page.html', {'data':data_var})

def alert_details(request):
    return render(request, 'alert_details.html')

def stitched_start(request):
    pass
    # # os.system('python schedule_tasks')
    # cmd = 'python schedule_tasks.py' 
    # # The os.setsid() is passed in the argument preexec_fn so
    # # it's run after the fork() and before  exec() to run the shell.
    # pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
    #                    shell=True, preexec_fn=os.setsid)
    # return HttpResponse("Hello, world. You're at the polls index.")
    # print("killing the process")
    # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups

def show_alerts_views(request):
    if request.method == 'POST':
            # data_rec = json.loads(request.body)
    # diction = create_dict(data_rec)
    # print(diction)
        print(request.POST.get("alert", None))
        print("post method")
    return render(request, 'alert_details.html')