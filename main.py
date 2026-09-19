import json


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
            if not ip_add[i].isnumeric() or int(ip_add[i]) < 0 or int(ip_add[i]) > 255:
                ip_add_mistakes += f", октет {i}"

        if ip_add_mistakes != "Невірна ip-адреса. Зверніть увагу на":
            print(ip_add_mistakes + ".")
            continue
        break
    return ".".join(ip_add)


def write_to_file(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
    
network_data = {"ip_addresses": [
    {"name": input("Введіть ім'я мережі: "),
    "ip_addr": get_ip(),
    "description": input("Додайте опис мережі: "),
    "properties": {
                    "version": "IPv4",
                    "type": "static",
                    "device": "PC-User",
                    "service": "internet"
                }}
    ]}

write_to_file(network_data, "data.json")
