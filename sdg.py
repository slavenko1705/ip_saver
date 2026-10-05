# i_dict = {
#     "ip_addresses": [
#         {
#             "192.168.1.1": [
#                 {"name": "dgf"},
#                 {"cabinet": "205"},
#                 {"version": "IPv4"},
#                 {"type": "static"},
#                 {"device": "PC-User"},
#                 {"service": "internet"}                
#             ]
#         }
#     ]
# }

# for ip in i_dict["ip_addresses"]:
#     if "192.168.1.1" in ip.keys():
#         ip["192.168.1.1"].append({"status": "on"})
#         break
# print(i_dict)

import json


with open("data.json", "r", encoding="utf-8") as file:
    file_info = json.load(file)

for subnetwork in file_info["ip_addresses"]:
    for ip in subnetwork.values():
        print(type(ip))