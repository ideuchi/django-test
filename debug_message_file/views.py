from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime
import subprocess as sp

# Create your views here.
DEBUG_FILE = 'debug.txt'

def debug_cat(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time+' /debug_cat called.\n'
    file = DEBUG_FILE
    if "path" in request.GET:
        file = request.GET.get("path")
    if os.path.isfile(file):
        with open(file, 'r') as f:
            message += '\n\n' + file + ' contents:\n' + f.read()
    with open(DEBUG_FILE, 'a') as f:
        print('\n/debug_cat result:\n' + message, file=f)
    return HttpResponse('<pre>' + message + '</pre>')

def debug_ls(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time + ' /debug_ls called.\n'
    message += 'current dir: ' + os.getcwd() + '\n'
    cmd = 'ls -al'
    if "path" in request.GET:
        cmd += ' ' + request.GET.get("path")
    proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = proc.communicate()
    ls_file_name = std_out.decode('utf-8').rstrip()
    message += cmd +' result: ' + '\n' + ls_file_name
    with open(DEBUG_FILE, 'a') as f:
        print('\n/debug_ls result:\n' + message, file=f)
    return HttpResponse('<pre>' + message + '</pre>')

def debug_setup(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time + '/debug_setup called.\n'
    with open(DEBUG_FILE, 'a') as f:
        print('\n' + message, file=f)
    cmd = 'chmod +x debug_message_file/setup_test && debug_message_file/setup_test'
    proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = proc.communicate()
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message += cmd + ' result: \n  ' + cmd + ' std_out:\n' + std_out.decode('utf-8').rstrip() + '\n  ' + cmd + ' std_err:\n' + std_err.decode('utf-8').rstrip() + '\n'
    with open(DEBUG_FILE, 'a') as f:
        print('\n' + message, file=f)
    return HttpResponse('<pre>' + message + '</pre>')
