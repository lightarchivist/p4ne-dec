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

# router_config = open('router_config.conf')
rtr_running_config = router.get_config(retrieve='running')
# router_config.write(router.get_config(retrieve='running'))
running_config = rtr_running_config['running']
better = running_config.split('\n')


# pprint.pprint(json.dumps(rtr_running_config, indent=4))

router.close()