import http.client
import os

conn = http.client.HTTPSConnection("restapi.amap.com")
conn.request("GET", "/v3/direction/driving?origin=120.11862443412909,30.340600563162834&destination=120.11941494297787,30.34049147415585&output=json&key=586103122fb6ab7c4a35fe208f427526")
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))

path = os.path.split(__file__)[0]
f=open(path + "/index.json",'wb')
f.write(data)
f.close()
