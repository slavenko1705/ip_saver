import json


filename = "data.json"


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
            print(len(ip_add[i]))
            if (len(ip_add[i]) < 1 or len(ip_add[i]) > 3) or not ip_add[i].isnumeric() or int(ip_add[i]) < 0 or int(ip_add[i]) > 255:
                if ip_add_mistakes != "Невірна ip-адреса. Зверніть увагу на":
                    ip_add_mistakes += f", октет {i}"
                else:
                    ip_add_mistakes += f" октет {i}"

        if ip_add_mistakes != "Невірна ip-адреса. Зверніть увагу на":
            print(ip_add_mistakes + ".")
            continue
        break
    print(ip_add)
    return ip_add




def write_to_file(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
        
def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
        
        
json_data = read_json(filename)
new_user_data = [
                    {
                    ".".join(get_ip()): {
                                    "name": input("Введіть ім'я мережі: "),
                                    "cabinet": input("Додайте опис мережі: "),
                                    "version": "IPv4",
                                    "type": "static",
                                    "device": "PC-User",
                                    "service": "internet",
                                    "status": "on"
                                    },
                    }
                ]
network_data = {"ip_addresses": new_user_data}

write_to_file(network_data, filename)