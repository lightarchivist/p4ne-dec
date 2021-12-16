import netmiko

# dictionary for the netmiko connection arguments
R1 = {
    'device_type': 'linux',
    'host': '10.99.99.121',
    'username': 'sntuser',
    'password': 'Ilovenetworks99',
    'secret' : 'Ilovenetworks99'}

device_connection = netmiko.ConnectHandler(**R1)

# we have given the root password already so we don't need the following:
# device_connection.enable(cmd="sudo su", pattern='password')
# to become root
device_connection.enable()
response = device_connection.send_command('docker ps -a')
device_connection.exit_enable_mode()
print(response)

# device_connection.cleanup() or
device_connection.disconnect()

