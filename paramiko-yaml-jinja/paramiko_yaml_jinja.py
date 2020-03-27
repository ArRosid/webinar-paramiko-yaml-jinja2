import paramiko
import yaml
from pprint import pprint
from jinja2 import Template
import time

file_input = input("Masukan file yaml: ") or 'data.yml'
file_yaml = open(file_input, 'r')
data_yaml = yaml.load(file_yaml)

template_file_input = input("Masukkan file template: ") or 'template.j2'
template_file = open(template_file_input,"r").read()
template = Template(template_file)

for router in data_yaml:
	ip = router['ip']
	username = router['username']
	password = router['password']

	interface_list = router['interface_list']
	bgp_network = router["bgp"]['network']
	as_number = router['bgp']['local_as']
	router_id = router['bgp']['router_id']
	bgp_neighbor_list = router['bgp']['neighbor']

	dhcp_list = router['dhcp']
	
	cmds = template.render(interface_list=interface_list, 
						bgp_network=bgp_network,
						dhcp_list=dhcp_list,
						as_number=as_number,
						router_id=router_id,
						bgp_neighbor_list=bgp_neighbor_list)

	cmds = cmds.splitlines() # split("\n")

	print("connecting to {}".format(ip))
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip,username=username,password=password)
	
	conn = ssh_client.invoke_shell()
	conn.send("conf t\n")
	for cmd in cmds:
		conn.send(cmd + "\n")
		time.sleep(0.5)

	output = conn.recv(65535)
	print (output.decode())
	ssh_client.close()