from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime
import subprocess as sp

# Create your views here.
def index(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    debug_message = str_time+'debug called.\n'
    if os.path.isfile('debug.txt'):
        with open('debug.txt') as f1:
            debug_message += f1.read()
    return HttpResponse('<pre>' + debug_message + '</pre>')

def file_list(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time + '\n'
    message += 'current dir: ' + os.getcwd() + '\n'
    message += '__file__:    ' + __file__) + '\n'
    message += 'basename:    ' + os.path.basename(__file__) + '\n'
    message += 'dirname:     ' + os.path.dirname(__file__) + '\n'
    cmd = 'ls -l'
    proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = proc.communicate()
    ls_file_name = std_out.decode('utf-8').rstrip()
    message += 'ls -l result: ' + '\n' + ls_file_name
    with open('debug.txt', 'a') as f:
        print(message, file=f)
    return HttpResponse('<pre>' + message + '</pre>')

