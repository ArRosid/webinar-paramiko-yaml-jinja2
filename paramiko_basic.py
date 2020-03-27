
import paramiko
import time
import getpass

ip_list = ["192.168.100.1", "192.168.100.2"]
username = "cisco"
password = "cisco"

for ip in ip_list:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip,username=username, password=password)

	print ("Success login to {}".format(ip))
	conn = ssh_client.invoke_shell()

	conn.send("conf t\n")
	conn.send("int lo172\n")
	conn.send("ip add 172.1.1.1 255.255.255.255\n")
	time.sleep(1)

	output = conn.recv(65535)
	print (output.decode())

	ssh_client.close()