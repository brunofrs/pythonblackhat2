import socket

target_host= "127.0.0.1"
target_port= 9998

#1 - cria um cliente do objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 - Conecta no cliente
client.connect((target_host,target_port))

#3 - envia os dados
client.send(b"TESTE de MSG")

#4 - Recebendo os dados da mensagem
response = client.recv(4096)

print(response.decode())
client.close()