import socket

target_host= "www.google.com"
target_port= 80

#1 - cria um cliente do objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 - Conecta no cliente
client.connect((target_host,target_port))

#3 - envia os dados
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#4 - Recebendo os dados da mensagem
response = client.recv(4096)

print(response.decode())
client.close()