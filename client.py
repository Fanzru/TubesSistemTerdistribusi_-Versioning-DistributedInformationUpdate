# import xmlrpc bagian client saja
import xmlrpc.client
import json

# buat stub (proxy) untuk client
server = xmlrpc.client.ServerProxy('http://localhost:8000')

f = open('client.json')
data_client = json.load(f)

def print_pkg_manager():
    print("------------------------------------------------")
    print("mysql version   : ", data_client.get("mysql"))
    print("mongodb version : ", data_client.get("mongodb"))
    print("------------------------------------------------")


# lakukan pemanggilan fungsi update versi app yang ada di server
print('------------------------------------------------')
print('----------- Update Package Managermu -----------')
print('------------------------------------------------')
print_pkg_manager()
key = ""
while key != "exit":
    key = input("comand : ")
    server.update(key)
    # lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
    querry_result = server.querry_result()
    data_server = querry_result
    if key == "mysql_update":
        mysql = data_server
        print("versi mysql : ", mysql)
        data_client["mysql"] = mysql
        f = open("client.json", "w")
        json.dump(data_client, f)
        f.close()
    elif key == "mongodb_update":
        mongodb = data_server
        print("versi mongodb : ", mongodb)
        data_client["mongodb"] = mongodb
        f = open("client.json", "w")
        json.dump(data_client, f)
        f.close()
    elif key == "exit":
        print("exit terminal success")
    else:
        print("failed sytax")
    print()
    print('------------------------------------------------')
    print('----------------- Last Version -----------------')
    print_pkg_manager()
f.close()