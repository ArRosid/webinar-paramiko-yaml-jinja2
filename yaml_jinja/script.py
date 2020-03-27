import yaml
import json

file_yaml = open("data.yml", "r")
data_yaml = yaml.load(file_yaml)

# print(data_yaml)
print(json.dumps(data_yaml, indent=3))

for router in data_yaml:
    ip = router["ip"]
    user = router["username"]
    passw = router["password"]

    print(ip, user, passw)