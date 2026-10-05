i_dict = {
    "ip_addresses": [
        {
            "192.168.1.1": [
                {"name": "dgf"},
                {"cabinet": "205"},
                {"version": "IPv4"},
                {"type": "static"},
                {"device": "PC-User"},
                {"service": "internet"}                
            ]
        }
    ]
}

for ip in i_dict["ip_addresses"]:
    if "192.168.1.1" in ip.keys():
        ip["192.168.1.1"].append({"status": "on"})
        break
print(i_dict)
