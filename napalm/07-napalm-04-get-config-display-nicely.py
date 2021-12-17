import napalm
import json
import pprint

driver=napalm.get_network_driver("ios")
router = driver(hostname='10.99.99.11',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
router.open()

rtr_running_config = router.get_config(retrieve='running')

# rtr_running_config is a dictionary with only two items.
# The item with key 'running' is a single string of the configuration including
#  \n new line.
running_config = rtr_running_config['running']
running_cnfg_line_list = running_config.split('\n')
for line in running_cnfg_line_list:
    print(line)

router.close()