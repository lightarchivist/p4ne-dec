from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command

# for the progress bars
from tqdm import tqdm


def set_loopbacks(task: Task,):
    loopbacks = task.host.data['loopbacks']
    for key in loopbacks:
        interface = 'interface loopback' + str(key)
        # ip_addr = 'ip address ' + loopbacks[key] + ' 255.255.255.255'
        ip_addr = f'ip address {loopbacks[key]} 255.255.255.255'
        config_cmds = [interface, ip_addr]
        task.run(task=netmiko_send_config, config_commands=config_cmds)

my_nornir = InitNornir(config_file="./inventory/rtrs-cisco-simple/config.yaml")

result = my_nornir.run(
    #  this name can be seen in the screen output
    name="Setting the loopback IP addresses...",
    # task to run
    task=set_loopbacks,
)

print_result(result)
