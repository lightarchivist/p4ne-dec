# Dictionaries

devs  = {'rtrs':'blue', 'swtchs':'orange', 'vpns':'green'}

# print each dictionary item (key : value)
print(devs.items())
# print all the keys
print(devs.keys())

# print all the values
print(devs.values())

# walk through the dictionary and print all items
# one per line
for item in devs.items():
    print(item)

    devs  = {'rtrs':'blue', 'swtchs':'orange', 'vpns':'green'}


# this shows all dictionary key: value pairs 
for key in devs:
    print(key, ' : ', devs[key])



# the items method returns key,value tuples
# which we catch in a couple of variables 
for key, value in devs.items():
    print(key, ' : ', value)

# adding an item to the dictionary
devs['hub']='brown'

# sorting the keys and printing them
print(sorted(devs))
