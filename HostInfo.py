import socket
import time

print ("This script is for educational propose use it atyour own risk")
print ("Hello To This Script This Script Give You Info About Your Victime")
time.sleep(3)
hostvictime = input("Give Me The Host Or IP To Get Info:")
portvictime = input("Give Me The Port To Get Info:")
target_host = hostvictime
target_port = portvictime

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: hostvictime\r\n\r\n")

#receive some data
reponse = client.recv(4096)

print (reponse)
