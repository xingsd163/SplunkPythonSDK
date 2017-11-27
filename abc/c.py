#coding=utf-8

"""
获取 Entity  信息，比如应用、索引、用户、角色、版本

"""

import splunklib.client as client

HOST = "192.168.2.131"
PORT = 8089
USERNAME = "admin"
PASSWORD = "xingsd163"

service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

print "********Splunk Apps********"
for app in service.apps:
    print app.name

print "********Splunk Indexes*********"

for index in service.indexes:
    print index.name

print "********Splunk Users*********"

for user in service.users:
    print user.name


print "********Splunk Roles*********"
for role in service.roles:
    print role.name

print "********Splunk Version*********"

print service.splunk_version


print "********Splunk Roles*********"
for alert in service.fired_alerts:
    print alert.name
