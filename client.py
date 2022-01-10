# import xmlrpc bagian client saja
import xmlrpc.client
import json

# buat stub (proxy) untuk client
server = xmlrpc.client.ServerProxy('http://localhost:8000')
#untuk membaca dan meload database client yang disimpan pada file client.json
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
# memamnggil prosedur print_pkg_manager()
print_pkg_manager()
# init value key
key = ""

#running client cli menu
while key != "exit":
    #input key command to update database
    key = input("comand : ")
    # memanggil prosedur update() pada server rpc
    server.update(key)
    # lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
    querry_result = server.querry_result()
    data_server = querry_result
    #handle menu key input
    if key == "mysql_update":
        mysql = data_server
        print("versi mysql : ", mysql)
        #update database pada client.json
        data_client["mysql"] = mysql
        f = open("client.json", "w")
        json.dump(data_client, f)
        f.close()
    elif key == "mongodb_update":
        mongodb = data_server
        print("versi mongodb : ", mongodb)
        #update database pada client.json
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
#melakukan commit untuk menutup file client.json
f.close()