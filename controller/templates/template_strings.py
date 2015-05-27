#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'alex'

head = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<a href='/controller/index/'>Home Page</a><em>|</em>
<a href='/controller/list/'>Devices List</a><em>|</em>
<a href='/controller/add/'>Add Devices</a><em>|</em>
<a href='/controller/device/'>Manage Devices</a><em>|</em>
<a href='/controller/log/'>Logs</a><em>|</em>
<a href='/admin'>Administration</a>
'''

list_template = head + '''
{%if module == 'list' %}
<table border='1'>
<th>Name</th>
<th>SN</th>
<th>IpAddr</th>
<th>LoginName</th>
<th>PassWord</th>
<th>Notes</th>
  {%for d in device_list %}
  <tr>
  <td>{{d.name}}</td>
  <td>{{d.sn}}</td>
  <td>{{d.ipaddr}}</td>
  <td>{{d.login}}</td>
  <td>{{d.password}}</td>
  <td>{{d.notes}}</td>
  </tr>
  {%endfor%}
</table>
{%endif%}
</body>
</html>'''

add_template = head + '''
{%if action == 'new'%}
<form name='add_device' action='/controller/add/' method='post'>
{%csrf_token%}
<!-- avoid cross site request forgery using csrf_token-->
<table border='1'>
<tr><td>Name</td><td><input type='text' name='device_name' /></td></tr>
<tr><td>Host</td><td><input type='text' name='host' /></td></tr>
<tr><td>SN</td><td><input type='text' name='sn' /></td></tr>
<tr><td>Login User</td><td><input type='text' name='login' /></td></tr>
<tr><td>Passwords</td><td><input type='text' name='password' /></td></tr>
<tr><td>Notes</td><td><input type='text' name='notes' /></td></tr>
<tr><td colspan='2'><input type='submit' name='add_submit' value='Submit' /></td></tr>
</table>
</form>
{%else%}
<table>
<tr>
<td>{{name}}</td>
<td>{{host}}</td>
<td>{{sn}}</td>
<td>{{login}}</td>
<td>{{password}}</td>
<td>{{notes}}</td>
</tr>
</table>
{%endif%}
</body>
</html>'''


manage_template = head + '''
{%if module == 'device' %}
<form name='exec_info' action='/controller/commit/' method='post'>
{%csrf_token%}
<!-- avoid cross site request forgery using csrf_token-->
<table border='1'>
<th colspan='2'>Please select your action:</th>
<tr>
<td>Host:</td>
<td>
<select name='host'>
{%for d in device_list%}
  <option value='{{d.ipaddr}}|{{d.id}}'>{{d.ipaddr}} *{{d.login}} | {{d.name}} |{{d.id}}*</option>
{%endfor%}
</td>
</tr>

<tr>
<td>Module:</td>
<td>
<select name='module'>
{%for m in module_list%}
  <option value='{{m.name}}'>{{m.name}}</option>
{%endfor%}
</td>
</tr>

<tr>
<td>Arguments:</td>
<td>
<input type='text' name='arguments' />
</td>
</tr>

<tr>
<td colspan='2'>
<input type='submit' name='execute' value='Submit' />
</td>
</tr>

</table>
</form>
{%endif%}
</body>
</html>'''

commit_template = head + '''
<br />
{{host}}<em>|</em>
{{module}}<em>|</em>
{{arguments}}<em>|</em>
{{login}}<em>|</em>
{{passwd}}<br />

<table border='2'>
{%for k, v in messages%}
<tr><td>{{k}}</td><td>{{v}}</td></tr>
{%endfor%}
</table>
</body>
</html>'''


log_template = head + '''
<table border='2'>
{%for records in logs%}
<tr><td>{{records.log_time}}</td><td>{{records.action}}</td></tr>
{%endfor%}
</table>
</body>
</html>'''