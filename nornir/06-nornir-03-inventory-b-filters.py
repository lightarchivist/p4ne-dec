from nornir import InitNornir
from nornir.core.inventory import Host
import json


my_nornir = InitNornir(config_file = "./inventory/rtrs-cisco-simple/config.yaml")


# filters can be based on key: value pairs from the inventory yaml files.
# my_new_nornir is an object of same type as my_nornir so you can run tasks
# on it etc.
my_new_nornir = my_nornir.filter(priority=2)
# will show all the items with priority 1
print('Here are all the items with priority = 2:')
print(my_new_nornir.inventory.hosts.keys(), '\n')

#  filter using multiple items
my_new_nornir = my_nornir.filter(priority=99, site='london')
# will show all the items with priority 1 and site london
print('Here are all the items with priority = 99 and site = london:')
print(my_new_nornir.inventory.hosts.keys(), '\n')

# Showing inheritance hosts --> groups --> defaults
host_names = my_nornir.inventory.hosts.keys()
for host in host_names:
    print(f"The colour of {host} is {my_nornir.inventory.hosts[host]['colour']}\n")

# find group members
junos_members = my_nornir.inventory.children_of_group('junos_rtrs')
print('Here are all the members of group junos_rtrs')
print(junos_members)
