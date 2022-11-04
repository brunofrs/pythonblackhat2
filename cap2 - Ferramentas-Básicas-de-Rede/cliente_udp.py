import socket

target_host = "127.0.0.1"
target_port = 9998

#1 - Cria um objeto socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#2 - envia alguns dados
client.sendto(b"TESTE", (target_host, target_port))

#3 - Recebendo os dados
data, addr = client.recv(4096)

print(data.decode())
client.close()