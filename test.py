import json

def read_json():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)
    

def write_file():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(a, file, indent=4)
        print(f"Файл записано.")
        

b = {
            "ip_addr": "192.168.1.1"
            # "properties": {
            #     "name": "bdf",
            #     "description": "df",
            #     "version": "IPv4",
            #     "type": "static",
            #     "device": "PC-User",
            #     "service": "internet"
            # }
        }

a = read_json()
# if type(a) == dict and "ip_addresses" in a.keys():

# del a["ip_addresses"][0]

if b["ip_addr"] in [ip["ip_addr"] for ip in a["ip_addresses"]]:
    print("дубль")
else:
    a["ip_addresses"][:1].append(b)
    print(f"Інформацію додано.")
    
write_file()