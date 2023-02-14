import socket

HOST, PORT = '', 8080
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(True)
print(f'Serving HTTP on port {PORT} ...')

while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = """\
    HTTP/1.1 200 OK

    Welcome This is my first webpage, GREAT!
    """
    client_connection.sendall(bytes(http_response, "utf-8"))
    client_connection.close()