import socket

HOST = '127.0.0.1'
PORT = 5555

server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f'[*] Listening on {HOST}:{PORT}')

while True:
    try:
        client_socket, address = server_socket.accept()
    except KeyboardInterrupt:
        print("\nClosing Server Socket...")
        server_socket.close()
        sys.exit()

    print(f'[*] Accept connection from {address[0]}:{address[1]}')
    request = client_socket.recv(1024)
    print(f'[*] Recieved: {request.decode("utf-8")}')
    client_socket.send(b'THIS_IS_THE_SERVER_SPEAKING')
    client_socket.close()