import socket
from server import HOST, PORT, enc, dec

client_socket = socket.socket()

client_socket.connect((HOST, PORT))


def user_auth(client_socket):
    while True:
        recv_msg = dec(client_socket.recv(1024))
        if recv_msg == 'Auth ok':
            print(recv_msg)
            break
        else:
            name = input(recv_msg)
            client_socket.send(enc(name))


try:
    user_auth(client_socket)

    while True:
        inpu = input('\nType ur msg: \n')
        client_socket.send(enc(inpu))
        if inpu == 'q':
            break

except KeyboardInterrupt:
    print('n\Client shut down!')
    client_socket.send(enc('q'))
    client_socket.close()
except Exception as e:
    print(e)
    client_socket.close()
client_socket.close()
