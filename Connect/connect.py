import splunklib.client as client

HOST = "192.168.2.131"
PORT = 8089
USERNAME = "admin"
PASSWORD = "xingsd163"

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print app.name