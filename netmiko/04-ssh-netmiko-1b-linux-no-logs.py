import netmiko

R1 = {
    'device_type': 'linux',
    'host': '10.99.99.121',
    'username': 'sntuser',
    'password': 'Ilovenetworks99',
    #root password
    'secret' : 'Ilovenetworks99'}

device_connection = netmiko.ConnectHandler(**R1)

# the following is executed as the user
response1 = device_connection.send_command('date -R')
print(response1)

linux_cmds = ['docker ps -a',
              'uname -n']
# will try to become root for the following
response2 = device_connection.send_config_set(linux_cmds)
print(response2) #response is a string

# will try to become root for the following
response3 = device_connection.send_config_from_file('./linux-script.txt')
print(response3)

#  to gracefully exit the SSH session
# device_connection.cleanup() or
device_connection.disconnect()