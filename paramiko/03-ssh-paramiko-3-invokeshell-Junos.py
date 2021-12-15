import paramiko
import time

ssh_connection_1 = paramiko.client.SSHClient()
HOST="185.175.114.42"

# the policy is a predefined subclass of paramiko.client and says what to do when presented with unknown cert. from other end.
ssh_connection_1.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

ssh_connection_1.connect(HOST, port=55631, username="sntuser", password="Ilovenetworks99")

# open an interactive shell session with remote host (of type paramiko.channel.Channel)
interactive_shell = ssh_connection_1.invoke_shell()

# send the command to execute
interactive_shell.send("show version\n")

# gives chance for the output of the command to get back
time.sleep(1)

response = interactive_shell.recv(65535)
print(response.decode('utf8'))

ssh_connection_1.close()

