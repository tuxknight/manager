import os

from django.template import Template, Context, RequestContext
from django.http import HttpResponse
from controller.models import Device, DeviceState, ManageLog, Modules
from templates import template_strings

from . import ansible_exec
from . import ops_models
# Create your views here.


def list(request):
    """list devices"""
    t = Template(template_strings.list_template)
    device_list = Device.objects.all()
    response_html = t.render(
        Context({'device_list': device_list, 'module': 'list'})
    )
    return HttpResponse(response_html)


def add(request):
    """add devices"""
    t = Template(template_strings.add_template)
    if request.POST:
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
    """user interface to exec ansible modules"""
    t = Template(template_strings.manage_template)
    device_list = Device.objects.all()
    module_list = Modules.objects.all()
    response_html = t.render(
        RequestContext(request, {'device_list': device_list,
                       'module_list': module_list, 'module': 'device'})
    )
    return HttpResponse(response_html)


def commit(request):
    """run ansible modules and display results"""
    t = Template(template_strings.commit_template)
    id_host = request.POST['host']
    host = id_host.split('|')[0]
    id = id_host.split('|')[1]
    module = request.POST['module']
    arguments = request.POST['arguments']
    action = 'Exec|%s|%s|%s' % (host, module, arguments)
    ops_models.operate_log(action)
    # exec ansible module via ansible_exec.Executor
    server = ansible_exec.device_info(id)
    login = server.login
    passwd = server.password
    executor = ansible_exec.Executor(host, module, arguments, loginname=login, password=passwd)
    results = executor.doExec()
    dark = results['dark']
    contacted = results['contacted']
    if host in dark.keys():  # exec failed
        messages = results['dark']
    elif host in contacted.keys():  # exec sucessed
        messages = results['contacted']
    else:
        messages = {host: {host: 'host not found in ansible hosts file.'}}

    response_html = t.render(
        Context({'host': host,
                 'module': module,
                 'arguments': arguments,
                 'login': login,
                 'passwd': passwd,
                 'messages': messages[host].iteritems()}
                )
    )
    return HttpResponse(response_html)


def log(request):
    """display operate logs"""
    t = Template(template_strings.log_template)
    logs = ManageLog.objects.order_by('-log_time')
    response_html = t.render(
        Context({'logs': logs})
    )
    return HttpResponse(response_html)
