import json


filename = "data_c.json"


print(f"********** IP Saver Tool **********\n\nНатисність 'q' або 'quit' якщо бажаєте вийти\n")


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


def ip_data(ip_address: list) -> dict:
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
    ip_address_str = ".".join(ip_address)

    # check for subnetworks and ip dublicates
    for i,subnetwork in enumerate(json_data["ip_addresses"]):
        subnetwork_str = ".".join(ip_address[:3] + ["0"])
        
        
        if not subnetwork_str in subnetwork.keys() and i == len(json_data["ip_addresses"]) - 1:
            # якщо немає підмережі - створюємо та одразу додаємо нові дані
            json_data["ip_addresses"] += [{subnetwork_str: [ip_data(ip_address)]}]
            print("Додано нову підмережу та нову ip адресу")
            is_done = True
            break
        if subnetwork_str in subnetwork.keys():
            if subnetwork_str in subnetwork.keys() and ip_dublicate_check(ip_address, json_data):
                # якщо є така підмережа та є ір-адреса:
                rewrite = input("Така адреса вже існує. Перезаписати дані? (y/n): ")
                while True:
                    
                    if rewrite == "y":
                        new_ip_data = ip_data(ip_address)
                        print(new_ip_data)
                        # Перезаписуємо дані ip боксу:
                        ip_box_index = next((i for i,el in enumerate(subnetwork[subnetwork_str]) if el["ip_address"] == ip_address_str), -1)
                        subnetwork[subnetwork_str][ip_box_index] = new_ip_data                    
                        # print(ip_box_index)
                        # print(f"subnetwork = {subnetwork}")
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
            else:
                # якщо немає дублів додаємо нові дані в потрібне місце
                ip_adresses_list = [ip["ip_address"] for ip in subnetwork[subnetwork_str]]
                fourth_ip_octets = [ip.split(".")[3] for ip in ip_adresses_list]
                fourth_new_ip_octet = ip_address[3]
                if fourth_new_ip_octet == "0":
                    print("ip-адресу не може бути додано, це підмережа")
                    break
                for i, el in enumerate(fourth_ip_octets):                
                    if fourth_new_ip_octet in fourth_ip_octets:
                        print("ip_адреса дублюється")
                        break
                    elif int(fourth_new_ip_octet) > int(el) and i == (len(fourth_ip_octets) - 1):
                        fourth_ip_octets.append(fourth_new_ip_octet)
                        break
                    elif int(fourth_new_ip_octet) > int(el):
                        continue
                    else:
                        fourth_ip_octets = fourth_ip_octets[:i] + [fourth_new_ip_octet] + fourth_ip_octets[i:]
                        break
                print(fourth_ip_octets)
                
                # Перевірка індексу в списку адрес підмережі, якщо немає, то додаємо в кінці
                if fourth_ip_octets.index(fourth_new_ip_octet) > len(subnetwork[subnetwork_str]) - 1: 
                    print("1")
                    subnetwork[subnetwork_str].append(ip_data(ip_address))
                elif fourth_ip_octets.index(fourth_new_ip_octet) < 1:
                    print("2")
                    subnetwork[subnetwork_str].insert(0, ip_data(ip_address))
                else:
                    print("3")
                    subnetwork[subnetwork_str] = (subnetwork[subnetwork_str][:fourth_ip_octets.index(fourth_new_ip_octet)] 
                    + [ip_data(ip_address)]
                    + subnetwork[subnetwork_str][fourth_ip_octets.index(fourth_new_ip_octet):])

                is_done = True
                break
            
    
    if is_done == True:
        break
    

write_to_file(json_data, filename)