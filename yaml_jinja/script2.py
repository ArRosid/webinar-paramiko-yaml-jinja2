import yaml
import json
from jinja2 import Template

file_yaml = open("data.yml", "r")
data_yaml = yaml.load(file_yaml)

print(json.dumps(data_yaml, indent=3))


template_file = open("template.j2","r").read()
template = Template(template_file)

for router in data_yaml:
    ip = router["ip"]
    user = router["username"]
    passw = router["password"]
    iface_list = router["interface_list"]
    
    print("---------------------------")
    print("connecting to {} with user&password {}/{}".format(ip, user, passw))
    # print(json.dumps(iface_list, indent=3))

    cmds = template.render(interface_list=iface_list)
    print(cmds)
