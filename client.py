import socket


if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 53210))

    server_message = client_sock.recv(1024)
    server_message = server_message.decode('utf-8')
    print(server_message)

    while True:
        server_message = client_sock.recv(1024)
        server_message = server_message.decode('utf-8')

        if server_message == 'End':
            client_sock.close()
            break
        print(server_message)

        client_input = input()
        while len(client_input) == 0:
            client_input = input()
        try:
            client_sock.send(client_input.encode('utf-8'))
        except BrokenPipeError:
            print("Troubles with connection")
            client_sock.close()
            break
