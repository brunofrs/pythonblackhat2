from colorama import Fore, Back, Style
import socket
import threading


#Defindo IP do servidor e porta
IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Servidor iniciado {IP}:{PORT}' + Style.RESET_ALL)

    while True:
        client, address = server.accept()
        print(Fore.GREEN + f'[*] Conexão estabelecida com {address[0]}:{address[1]}' + Style.RESET_ALL)
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(Fore.YELLOW + f'[*] Recebendo: {request.decode("utf-8")}' + Style.RESET_ALL) 
        sock.send(b'ACK')


if __name__=='__main__':
    main()