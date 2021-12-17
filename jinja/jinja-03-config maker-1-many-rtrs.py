import jinja2
import yaml
import os


my_j2_environment = jinja2.Environment(loader = jinja2.FileSystemLoader('./jinja-templates'), trim_blocks=True, lstrip_blocks=True)

# loads a specific template
my_template = my_j2_environment.get_template('j2-tmplt-03-lpbks-ifs-b.j2')

# Opens then loads the yaml configuration data file
my_yaml_cfg_file = open('./jinja-data/j2-data-03-lpbks-ifs-b.yml')
my_config_data = yaml.load(my_yaml_cfg_file, Loader=yaml.FullLoader)
# my_config_data is a dictionary whose keys are the IDs R1, R2, R3.
# The keys are the top level of the yaml file.

# We can now iterate through that dictionary for each key (host)
for host in my_config_data:
    # Create the file path to the new config file for that host.
    config_filename =  f'./j2-config-files/{host}-config-file-3.cfg'
    # Open that new config file with write access (overwrites file)
    with open(config_filename, 'w') as new_config_file:
        # Merge/render the host branch of the yaml file with the template.
        new_config_file.write(my_template.render(my_config_data[host]))

