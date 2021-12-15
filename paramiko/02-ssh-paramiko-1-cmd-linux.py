import paramiko

ssh_connection_1 = paramiko.client.SSHClient()
HOST="10.99.99.100"
# the policy is a predefined subclass of paramiko.client and says what to do when presented with unknown certs from other end.
ssh_connection_1.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
print(type(ssh_connection_1))

ssh_connection_1.connect(HOST, username="sntuser", password="Ilovenetworks99")
print(ssh_connection_1.get_transport())

# 3-tuple returned of "file-like" objects
# stdin for input to the connection
# stdout for output from the connection
# stderr for error msgs
# jack,jill,jo=ssh_connection_1.exec_command("ls", timeout=5) shows names unimportant
stdin,stdout,stderr=ssh_connection_1.exec_command("ls", timeout=5)

# print(stdout.read().decode("utf8"))
# the following also works for the print
# print(f'STDOUT: {stdout.read().decode("utf8")}')
for oneline in stdout.readlines():
    print(oneline)

# file objects should be to be closed
stdin.close()
stdout.close()
stderr.close()

ssh_connection_1.close()
print('SSH connection to ' + HOST + ' now closed.')

