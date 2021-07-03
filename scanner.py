#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("inavlid set of arguments")
	print("Syntax : python3 scanner.py <ip>")
	
#add a banner
print("_." * 50)
print("Scanning target "+target)
print("Time Started : "+str(datetime.now()))
print("_." * 50)

try:
	for port in range(1,85):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExisting Program.")
	sys.exit()
	
except socket.gaierror:
	print("hostname couldn't be resolved.")
	sys.exit()
	
except socket.error:
	print("couldn't connect to the server.")
	sys.exit()
	
	
