#!/usr/bin/env python3

# this will telnet into a remote Cisco router and execute the command:
#  "show ip interface brief"
import getpass
import telnetlib

HOST = "10.99.99.11"
user = input("Enter your remote username: ")
password = getpass.getpass()

# the following two lines could combine: telnet_connection_1 = telnetlib.Telnet(HOST)
telnet_connection_1 = telnetlib.Telnet()
telnet_connection_1.open(HOST)

# read output from device until you find 'username:', timeout=3secs
telnet_connection_1.read_until(b"username: ",3)
# write to the device the username encoded as ASCII text with Enter (new line)
telnet_connection_1.write(user.encode("ascii") + b"\n")

# if the password contains anything
if password:
   telnet_connection_1.read_until(b"Password:",3)
   telnet_connection_1.write(password.encode("ascii") + b"\n")

telnet_connection_1.write(b"show ip int br\n")

# read the output from the device until you reach the
# new line character \n
nextline = telnet_connection_1.read_until(b"\n", 3)
# if the line has sometext in it
while nextline :
    print (nextline.decode('UTF-8'))
    nextline = telnet_connection_1.read_until(b"\n", 3)

# exit the telnet connection
telnet_connection_1.write(b"exit\n")

# close the connection object
telnet_connection_1.close()  
