import napalm

driver=napalm.get_network_driver("ios")
router = driver(hostname='10.99.99.11',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
router.open()


configs_all = router.get_config(retrieve='running')
#  configs_all is a dictionary with three keys: starup, running, and candidate
config_running = configs_all['running']
print(config_running)

# Open the file with write access.
router_config = open('router_config.conf', 'w')
# Write to file.cd ../../../nap 
router_config.write(config_running)
# which is the same as:
# router_config.write((router.get_config(retrieve='running'))['running'])

router.close()