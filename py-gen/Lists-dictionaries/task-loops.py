# create a list of IP addresses
iplist = ['10.99.99.11', '10.99.99.12','10.99.99.13']

# # print each IP address in the list
for ipaddr in iplist:
    print(f'The IP address is: {ipaddr}')

# print each IP and its index number
for index in range(len(iplist)):
    print(f'The IP address at index {index} is {iplist[index]}')

# Create the dictionary of device names to IP addresses.
deviceips = {'R1':'10.99.99.11','R2':'10.99.99.12','R3':'10.99.99.13'}

# Print out all the keys
for key in deviceips:
    print(f'The device name is: {key}')

# Print out all the values
for value in deviceips.values():
    print(f'The device IP is: {value}')

# Print out the key: value pairs
for key,value in deviceips.items():
    print(f'Device {key} has IP: {value}')


# print out all numbers in range 0 to 9
for num in range(10):
    print(num)

# print out all IP addresses from 10.1.1.1 to 10.1.1.9
for num in range(1,10):
    print('10.1.1.' + str(num))


    