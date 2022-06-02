import socket
from pprint import pprint
import threading
import sqlite3

connection = sqlite3.connect(database='/home/sirius/ban_list/chat_ban-list.db')
cursor = connection.cursor()

HOST = '127.0.0.1'
PORT = 12345
AUTH_OK = 'Auth ok'


def enc(s):
    return s.encode('utf-8')


def dec(s):
    return s.decode('utf-8')


def new_client(client_socket, username):
    global users
    while True:
        recv_msg = client_socket.recv(1024)
        print('\nIncoming msg: \n')
        decoded = dec(recv_msg)
        print('User {0}: {1}'.format(username, decoded))
        if decoded == 'q':
            del users[username]
            print('user {0} disconnected'.format(username))
            pprint(users)
            break


def banned():
    cursor.execute('''SELECT * FROM ban_names''')
    ban_name_var = cursor.fetchall()
    cursor.execute('''SELECT * FROM ban_addresses''')
    ban_range = cursor.fetchall()
    ban_name = []
    for i in ban_name_var:
        ban_name.append(i[0])
    return ban_name, ban_range


def check_range(address, ban_range):
    for i in ban_range:
        if address[0] == i[2]:
            if i[0] <= address[1] <= i[1]:
                return False
    return True


def server_auth(user, address, users):
    while True:
        user.send(enc('Type your name: '))
        username = dec(user.recv(1024))

        ban_name, ban_range = banned()

        if username not in users.keys():
            if username not in ban_name:
                if check_range(address, ban_range):
                    print('User {0[0]}:{0[1]} connected as {1}'.format(address, username))
                    users[username] = address
                    print('\nNow connected: \n')
                    pprint(users)
                    user.send(enc(AUTH_OK))
                    return username, users


if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    users = dict()  # addrs

    try:
        while True:
            user, address = server_socket.accept()
            print('Connected: ', address)
            username, users = server_auth(user, address, users)
            threading.Thread(target=new_client, \
                             args=(user, username)).start()

    except KeyboardInterrupt:
        print('n\Server shut down!')
        server_socket.close()
        connection.close()
    except Exception as e:
        print(e)
        server_socket.close()
        connection.close()
    server_socket.close()
    connection.close()