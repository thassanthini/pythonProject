import socket
import sys

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("Socket creation failed with error %s" % err)


port = 80
try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("There is a problem resolving the host")
    sys.exit()

s.connect((host_ip, port))
print("Successfully connected to the website given %s:%s" % (host_ip,port))