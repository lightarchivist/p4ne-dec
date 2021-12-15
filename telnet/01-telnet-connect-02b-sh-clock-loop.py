#!/usr/bin/env python3

# this will telnet into a remote Cisco router and execute the command:
#  "show clock"
import getpass
import telnetlib

host_list = ["10.99.99.11", "10.99.99.12", "10.99.99.13"]
user = input("Enter your remote username: ")
password = getpass.getpass()

for host in host_list:
    # the following two lines could combine: telnet_connection_1 = telnetlib.Telnet(HOST)
    telnet_connection_1 = telnetlib.Telnet()
    telnet_connection_1.open(host)

    telnet_connection_1.read_until(b"username: ",3)
    telnet_connection_1.write(user.encode("ascii") + b"\n")
    if password:
        telnet_connection_1.read_until(b"assword:",3)
        telnet_connection_1.write(password.encode("ascii") + b"\n")

    telnet_connection_1.write(b"show clock\n")
    nextline = telnet_connection_1.read_until(b"\n", 3)
    while nextline :
        print (nextline.decode('UTF-8'))
        nextline = telnet_connection_1.read_until(b"\n", 3)

    telnet_connection_1.write(b"exit\n")

    telnet_connection_1.close()  

