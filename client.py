# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
server = xmlrpc.client.ServerProxy('http://127.0.0.1:8008')
mysql = "1.2.3"
mongodb = "0.1.2"


def print_pkg_manager():
    print("------------------------------------------------")
    print("mysql version   : ", mysql)
    print("mongodb version : ", mongodb)
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
    data = querry_result
    if key == "mysql_update":
        mysql = data
        print("versi mysql : ", mysql)
    elif key == "mongodb_update":
        mongodb = data
        print("versi mongodb : ", data)
    elif key == "exit":
        print("exit terminal success")
    else:
        print("failed sytax")
    print()
    print('------------------------------------------------')
    print('----------------- Last Version -----------------')
    print_pkg_manager()
