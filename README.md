# TUGAS BESAR SISTEM TERDISTRIBUSI - Versioning / Distributed  Information Update

Tugas ini dikerjakan dengan anggota :
1. Ananda Affan Fattahila - 1301194175
2. Faishal Januarahman - 1301194049
3. Shabrina Retno Ningsih - 1301194162
4. Zendy Bramantia Alfareza - 1301194145

Adapun cara pemakaian sistem ini menjadi 2 yaitu

>  Menggunakan server kelompok kami

client.py
 ```
 server = xmlrpc.client.ServerProxy('http://103.55.38.98:1001')
```
server.py
Tidak perlu di atur karena sudah di running pada vm kelompok kami.
>  Menggunakan 1 komputer saja

client.py
 ```
 server = xmlrpc.client.ServerProxy('http://localhost:1001')
```
server.py
```
with SimpleXMLRPCServer(("localhost",  1001),  requestHandler=RequestHandler,  allow_none=True)  as server:
```

This is a major assignment for a distributed systems course entitled " Versioning/Distributed Information Update".