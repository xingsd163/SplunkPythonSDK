
"""Retrieves a list of installed apps from Splunk using the binding module."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from xml.etree import ElementTree

import splunklib.binding as binding

HOST = "192.168.2.131"
PORT = 8089
USERNAME = "admin"
PASSWORD = "xingsd163"

context = binding.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

response = context.get('apps/local')
if response.status != 200:
    raise Exception, "%d (%s)" % (response.status, response.reason)

body = response.body.read()
data = ElementTree.XML(body)
apps = data.findall("{http://www.w3.org/2005/Atom}entry/{http://www.w3.org/2005/Atom}title")
for app in apps:
    print app.text

