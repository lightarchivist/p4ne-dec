from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from nornir.core.filter import F

# This task does not actually set the loopback as the commands to 
# do that are missing.
# This only logs in, goes to the interface loopback 99, then returns
# a message.
def set_loopbacks(task: Task,):
    loopbacks = task.host.data['loopbacks']
    task.run(task=netmiko_send_config, config_commands = ["interface loopback 99"])
        
    return Result(
        host=task.host,
        result=f"{task.host.name} loopbacks configured to - {loopbacks}"
    )

my_nornir = InitNornir(config_file="./inventory/rtrs-cisco-simple/config.yaml")
my_nornir = my_nornir.filter(F(groups__contains="cisco_rtrs"))
print(my_nornir.inventory.hosts.keys())
results = my_nornir.run(task=set_loopbacks)
print_result(results)

