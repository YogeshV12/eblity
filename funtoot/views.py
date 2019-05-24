from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import os
import signal
import subprocess

pro = 123
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def schedule(request):
    return render(request, 'schedule.html')

def alert(request):
    return render(request, 'alerts.html')

def stitched_start(request):
    # os.system('python schedule_tasks')
    cmd = 'python schedule_tasks.py' 
    # The os.setsid() is passed in the argument preexec_fn so
    # it's run after the fork() and before  exec() to run the shell.
    pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid)
    return HttpResponse("Hello, world. You're at the polls index.")
    print("killing the process")
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups

