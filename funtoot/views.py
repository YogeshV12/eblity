from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import os
import signal
import subprocess

from funtoot.models import Buttons
import pandas as pd


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def schedule(request):
    row = Buttons.objects.get(id=1)
    data = {
        'stitched_start': row.stitched_start,
        'stitched_stop': row.stitched_stop,
        'time_series_start': row.time_series_start,
        'time_series_stop': row.time_series_stop
    }
    return render(request, 'schedule.html', data)

def alert(request):
    df = pd.read_csv('all_alerts.csv').to_dict('r')
    data = {'data': df}
    return render(request, 'alert_page.html', data)

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

