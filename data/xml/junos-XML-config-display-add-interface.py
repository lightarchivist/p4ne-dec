# Import the xmltodict library
import xmltodict

# Open the sample xml file and read it into variable
with open("junos-config-for-testing.xml") as f:
    xml_example = f.read()

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)
print(type(xml_dict))
print(xml_dict)
int_dict = xml_dict["rpc-reply"]["data"]["configuration"]["interfaces"]['interface']
print(type(int_dict))
print(int_dict)
print(f'The number of items in the list of interface OrderdDicts is: {len(int_dict)}')
print('Interfaces present are:')
for item in int_dict:
    print(item['name'])

# Open the sample xml file and read it into variable
with open("junos-interface-only.xml") as f:
    xml_example = f.read()

# Parse the XML into a Python dictionary
int_to_add = xmltodict.parse(xml_example)['interface']
print(type(int_dict))
print(int_dict)
print(type(int_to_add))
print(int_to_add)
# add the OrderedDict containing the new interface to the end of the orininal
# OrderedDict containing all the interfaces.
int_dict.append(int_to_add)

print('after addition...')
print('Interfaces present are:')
print(len(int_dict))
for item in int_dict:
    print(item['name'])

