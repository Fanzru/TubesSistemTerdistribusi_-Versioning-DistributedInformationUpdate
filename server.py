# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
# import json
import json
# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

data_json = open('server.json')
data = json.load(data_json)

globvar = ""


def set_globvar(values):
    global globvar  # Needed to modify global copy of globvar
    globvar = values


def get_globvar():
    return globvar


# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = '/RPC2'


# Buat server
with SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()


    def update(x):

        # critical section dimulai harus dilock
        lock.acquire()

        # jika update set global variable
        if x == "mysql_update":
            set_globvar("mysql")
        elif x == "mongodb_update":
            set_globvar("mongodb")
        elif x == exit:
            set_globvar("exit")
        else:
            set_globvar("null")
        # critical section berakhir, harus diunlock
        lock.release()


    # register fungsi update() sebagai update client
    server.register_function(update, "update")


    def querry_result():
        # critical section dimulai
        update_var = get_globvar()
        lock.acquire()
        if update_var == "mysql":
            lock.release()
            return data.get("mysql")
        elif update_var == "mongodb":
            lock.release()
            return data.get("mongodb")
        else:
            lock.release()
            return "failed update"


    # register querry_result sebagai querry
    server.register_function(querry_result, "querry_result")

    print("Server voting is Running...")
    # Jalankan server
    server.serve_forever()
