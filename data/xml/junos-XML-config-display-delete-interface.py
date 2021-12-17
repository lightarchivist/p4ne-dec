# Import the xmltodict library
import xmltodict

# Open the sample xml file and read it into variable
with open("junos-config-for-testing.xml") as f:
    xml_example = f.read()

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)

int_dict = xml_dict["rpc-reply"]["data"]["configuration"]["interfaces"]['interface']

print(f'The number of items in the list of interface OrderdDicts is: {len(int_dict)}')
print('Interfaces present are:')
for item in int_dict:
    print(item['name'])


for i in range(len(int_dict)):
    if int_dict[i]['name'] == 'ge-1':
        print(f'Deleting interface config for: {int_dict[i]}')
        int_dict.pop(i)
    
print('after deletion...')
print('Interfaces now present are:')
print(len(int_dict))
for item in int_dict:
    print(item['name'])


