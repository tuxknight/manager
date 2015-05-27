from django.template import  Context, RequestContext
from django.shortcuts import render_to_response
from controller.models import Device,  ManageLog, Modules

from . import ansible_exec
from . import ops_models
# Create your views here.

def list(request):
    device_list = Device.objects.all()
    return render_to_response('list.html', Context({'device_list': device_list, 'module': 'list'}))


def add(request):
    """add devices"""
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
        return render_to_response('add.html', RequestContext(request, {'action': action}))


def device(request):
    """user interface to exec ansible modules"""
    device_list = Device.objects.all()
    module_list = Modules.objects.all()
    return render_to_response(
        'manage.html',
        RequestContext(request,
                       {'device_list': device_list,
                        'module_list': module_list,
                        'module': 'device'}
        )
    )


def commit(request):
    """run ansible modules and display results"""
    id_host = request.POST['host']
    host = id_host.split('|')[0]
    device_id = id_host.split('|')[1]
    module = request.POST['module']
    arguments = request.POST['arguments']
    action = 'Exec|%s|%s|%s' % (host, module, arguments)
    ops_models.operate_log(action)
    # exec ansible module via ansible_exec.Executor
    server = ansible_exec.device_info(device_id)
    login = server.login
    passwd = server.password
    if len(login) == 0:
        login = 'root'
    if len(passwd) == 0:
        passwd = None
    executor = ansible_exec.Executor(host, module, arguments, loginname=login, password=passwd)
    results = executor.doExec()
    dark = results['dark']
    contacted = results['contacted']
    if host in dark.keys():  # exec failed
        messages = results['dark']
    elif host in contacted.keys():  # exec succeed
        messages = results['contacted']
    else:
        messages = {host: {host: 'host not found in ansible hosts file.'}}

    return render_to_response('commit.html',
                              Context(
                                  {'host': host,
                                   'module': module,
                                   'arguments': arguments,
                                   'login': login,
                                   'passwd': passwd,
                                   'messages': messages[host].iteritems()
                                   }
                              )
    )


def log(request):
    """display operate logs"""
    logs = ManageLog.objects.order_by('-log_time')
    return render_to_response('log.html', Context({'logs': logs}))
