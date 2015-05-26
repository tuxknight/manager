from django.shortcuts import render, loader
from django.template import Template, Context, RequestContext
from django.http import HttpResponse
from controller.models import Device, DeviceState, ManageLog, Modules
from templates import template_strings
from . import ansible_exec
from . import ops_models
# Create your views here.


def list(request):
    t = Template(template_strings.list_template)
    device_list = Device.objects.all()
    response_html = t.render(
        Context({'device_list': device_list, 'module': 'list'})
    )
    return HttpResponse(response_html)


def add(request):
    t = Template(template_strings.add_template)
    if request.POST:
        action = 'post'
        name = request.POST['device_name']
        host = request.POST['host']
        sn = request.POST['sn']
        login = request.POST['login']
        password = request.POST['password']
        notes = request.POST['notes']
        ops_models.add_device(name, sn, host, login, password, notes)
        action = 'Add Device|%s|%s|%s|%s' % (name, host, sn, notes)
        ops_models.operate_log(action)
        return list(request)
    else:
        action = 'new'
        response_html = t.render(
            RequestContext(request, {'action': action})
        )
        return HttpResponse(response_html)




def device(request):
    t = Template(template_strings.manage_template)
    device_list = Device.objects.all()
    module_list = Modules.objects.all()
    response_html = t.render(
        RequestContext(request, {'device_list': device_list,
                        'module_list': module_list,
                        'module': 'device'})
    )
    return HttpResponse(response_html)


def commit(request):
    t = Template(template_strings.commit_template)

    host = request.POST['host']
    module = request.POST['module']
    arguments = request.POST['arguments']
    action = 'Exec|%s|%s|%s' % (host, module, arguments)
    ops_models.operate_log(action)
    executor = ansible_exec.Executor(host, module, arguments)
    results = executor.doExec()
    dark = results['dark']
    contacted = results['contacted']
    if host in dark.keys():
        messages = results['dark']
    elif host in contacted.keys():
        messages = results['contacted']
    else:
        messages = {host: {'msg': 'Unkown Error!'}}

    response_html = t.render(
        Context({'host': host,
                 'module': module,
                 'arguments': arguments,
                 'messages': messages[host].iteritems()}
                )
    )
    return HttpResponse(response_html)


def log(request):
    t = Template(template_strings.log_template)
    logs = ManageLog.objects.order_by('-log_time')
    response_html = t.render(
        Context({'logs': logs})
    )
    return HttpResponse(response_html)
