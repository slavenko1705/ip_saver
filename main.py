import json


filename = "data_c.json"


print(f"********** IP Saver Tool **********")


def get_ip():
    while True:
        ip_add = input("Введіть ip-адресу: ")
        if "." not in ip_add or ip_add.count(".") != 3:
            print("Невірна ір-адреса. Перегляньте розділові знаки між октетами.")
            continue
        ip_add_mistakes = "Невірна ip-адреса. Зверніть увагу на"
        ip_add = ip_add.split(".")
        
        for i in range(len(ip_add)):
            # print(len(ip_add[i]))
            if (len(ip_add[i]) < 1 or len(ip_add[i]) > 3) or not ip_add[i].isnumeric() or int(ip_add[i]) < 0 or int(ip_add[i]) > 255:
                if ip_add_mistakes != "Невірна ip-адреса. Зверніть увагу на":
                    ip_add_mistakes += f", октет {i}"
                else:
                    ip_add_mistakes += f" октет {i}"

        if ip_add_mistakes != "Невірна ip-адреса. Зверніть увагу на":
            print(ip_add_mistakes + ".")
            continue
        break
    return ip_add


def ip_data(ip_address) -> dict:
    new_user_data = {
                        "ip_address" : ".".join(ip_address),
                        "name": input("Введіть ім'я мережі: "),
                        "cabinet": input("Номер кабінету: "),
                        "version": "IPv4",
                        "type": "static",
                        "device": "PC-User",
                        "service": "internet",
                        "status": "on"
                    }
    return new_user_data
    
    
def write_to_file(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
        
def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
        

def ip_dublicate_check(ip_address: list, json_data: dict) -> bool: 
    result = False
    for data in json_data.values():
        for subnet in data:
            for ip_list in subnet.values():
                for ip in ip_list:
                    if ".".join(ip_address) == ip["ip_address"]:
                        result = True
                        return result
    return result
                    

# read our json file
json_data = read_json(filename)

is_done = False
while is_done == False:
    # take new data from user/admin 
    ip_address = get_ip()

    # check for subnetworks and ip dublicates
    for subnetwork in json_data["ip_addresses"]:
        if not ".".join(ip_address[:3] + ["0"]) in subnetwork.keys():
            json_data["ip_addresses"] += [{f"{".".join(ip_address[:3] + ["0"])}": [ip_data(ip_address)]}]
            print("1")
            break
        elif ".".join(ip_address[:3] + ["0"]) in subnetwork.keys() and ip_dublicate_check(ip_address, json_data):
            rewrite = input("Така адреса вже існує. Перезаписати дані? (y/n): ")
            while True:
                
                if rewrite == "y":
                    new_ip_data = ip_data(ip_address)
                    print(new_ip_data)
                    is_done = True
                    print("Дані перезаписано")
                    break
                elif rewrite == "n":
                    is_done = True
                    break
                else:
                    print("Будь ласка, оберіть правильну відповідь")
                    rewrite = input("Перезаписати дані? (y/n): ")
            
            break            
    
    if is_done == True:
        break
    
            # else: 
                    # додати включення блоку з ір адресою в потрібне місце
           








# # check for subnetworks and ip dublicates
# for subnetwork in json_data["ip_addresses"]:
#     if not ".".join(ip_address[:3] + ["0"]) in subnetwork.keys():
#         json_data["ip_addresses"] += [{f"{".".join(ip_address[:3] + ["0"])}": []}]
#     else:
#         # a = ["1", "2", "9", "10"]
#         # b = "0"

#         for index, ip_adr in enumerate(json_data["ip_addresses"]):
#             print(f"el: {el}, index: {i}")
            
#             if int(b) > int(el) and i == (len(a) - 1):
#                 a.append(b)
#                 # c = a
#                 print("1")
#                 break
#             elif int(b) > int(el):
#                 print("2")
#                 continue
#             else:
#                 a = a[:i] + list(b) + a[i:]
#                 print("3")
#                 break

                
# network_data = {"ip_addresses": new_user_data}

# write_to_file(network_data, filename)