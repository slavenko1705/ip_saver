i_dict = [{
                "ip_address": "192.168.1.100",
                "name": "dgf",
                "cabinet": "205",
                "version": "IPv4",
                "type": "static",
                "device": "PC-User",
                "service": "internet",
                "status": "on"
            },
            {
                "ip_address": "192.168.1.101",
                "name": "dgf",
                "cabinet": "205",
                "version": "IPv4",
                "type": "static",
                "device": "PC-User",
                "service": "internet",
                "status": "on"
            }]
print(type(next((i for i,e in enumerate(i_dict) if e["ip_address"] == "192.168.1.101"), -1)))
