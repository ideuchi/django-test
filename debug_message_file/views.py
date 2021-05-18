from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime
import subprocess as sp

# Create your views here.
def debug(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    debug_message = str_time+' debug called.\n'
    with open('debug.txt', 'a') as f:
        print('\n/index(debug) stdout:\n' + debug_message + ' + debug.txt contents', file=f)
    if os.path.isfile('debug.txt'):
        with open('debug.txt', 'r') as f:
            debug_message += '\n\ndebug.txt contents:\n' + f.read()
    return HttpResponse('<pre>' + debug_message + '</pre>')

def files(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time + '/files called.\n'
    message += 'current dir: ' + os.getcwd() + '\n'
    message += '__file__:    ' + __file__ + '\n'
    message += 'basename:    ' + os.path.basename(__file__) + '\n'
    message += 'dirname:     ' + os.path.dirname(__file__) + '\n'
    cmd = 'ls -al'
    if "action" in request.GET:
        cmd = request.GET.get("action")
    if "path" in request.GET:
        cmd += ' ' + request.GET.get("path")
    proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = proc.communicate()
    ls_file_name = std_out.decode('utf-8').rstrip()
    message += cmd +' result: ' + '\n' + ls_file_name
    with open('debug.txt', 'a') as f:
        print('\n/files stdout:\n' + message, file=f)
    return HttpResponse('<pre>' + message + '</pre>')

def prepare_debug(request):
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message = str_time + '/prepare_debug called.\n'
    with open('debug.txt', 'a') as f:
        print('\n' + message, file=f)
    
    cmd = 'chmod +x debug_message_file/setup_test'
    proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = proc.communicate()
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message += cmd + ' result: \n  ' + cmd + ' std_out:\n' + std_out.decode('utf-8').rstrip() + '\n  ' + cmd + ' std_err:\n' + std_err.decode('utf-8').rstrip() + '\n'
    with open('debug.txt', 'a') as f:
        print('\n' + message, file=f)
    
    cmd = 'debug_message_file/setup_test'
    proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    std_out, std_err = proc.communicate()
    time = datetime.datetime.now()
    str_time = time.strftime('%Y/%m/%d %H:%M:%S')
    message += cmd + ' result: \n  ' + cmd + ' std_out:\n' + std_out.decode('utf-8').rstrip() + cmd + ' std_err:\n' + "".join(c for c in std_err.decode('utf-8').rstrip() if c.isprintable()) + '\n'
    with open('debug.txt', 'a') as f:
        print('\n' + message, file=f)
    
    return HttpResponse('<pre>' + message + '</pre>')

