import json

def read_json():
    with open("data_c.json", "r", encoding="utf-8") as file:
        return json.load(file)
    

# def write_file():
#     with open("data_c.json", "w", encoding="utf-8") as file:
#         json.dump(a, file, indent=4)
#         print(f"Файл записано.")
        

b = {
            "ip_addr": "192.168.1.101"
            # "properties": {
            #     "name": "bdf",
            #     "description": "df",
            #     "version": "IPv4",
            #     "type": "static",
            #     "device": "PC-User",
            #     "service": "internet"
            # }
        }
ip = ["192", "168", "1", "101"]
json_data = read_json()
# if type(a) == dict and "ip_addresses" in a.keys():

# del a["ip_addresses"][0]

# for data in json_data.values():
#     for subnet in data:
#         for ip_list in subnet.values():
#             if not b["ip_addr"] in [ip["ip_address"] for ip in ip_list]:
#                 print("f")


print(json_data["ip_addresses"][ip.index("1")][".".join(ip[:3] + ["0"])][next((i for i,e in enumerate(".".join(ip[:3] + ["0"]) if e["ip_address"] == ), -1)])
        
