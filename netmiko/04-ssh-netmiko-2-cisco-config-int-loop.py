import netmiko

# router_num will loop through numbers 1 to 3
for router_num in range(1,4):
    # create the target IP address fro SSH connection
    host_ip = '10.99.99.1' + str(router_num)

    R1 = {
        'device_type': 'cisco_ios',
        'host':  host_ip,
        'username': 'sntuser',
        'password': 'Ilovenetworks99',
        'secret' : 'cisco'}

    device_connection = netmiko.ConnectHandler(**R1)
    device_connection.enable()

    # create the loopback IP address correct for the route number
    loopback_ip = '1.1.1.' + str(router_num)
    
    router_config = ['interface loopback0',
                    'ip address ' + loopback_ip + ' 255.255.255.255']
    response = device_connection.send_config_set(router_config)
    print(response)


