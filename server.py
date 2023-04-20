import socket

HOST = '192.168.64.2' # The server's hostname or IP address
PORT = 1234 # The port used by the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a specific address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print('Server listening on', HOST, PORT)
    # Accept a connection
    conn, addr = s.accept()
    print('Connected by', addr)
    # Receive data from the client
    data = conn.recv(1024)
    print('Received', repr(data))
    # Send a response back to the client
    conn.sendall(b'Hello, client!')
