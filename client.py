"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port


    HOST = "172.20.10.5"  # The server's hostname or IP address
    PORT = 10000  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
    # TODO: Get user input and send it to the server using your TCP socket
        u_in = input('Enter something fun!\n') 

    #for i in bytearray(u_in, 'ascii'):
       # s.sendall(i)

        s.send(u_in.encode())
        data = s.recv(256)
    # TODO: Receive a response from the server and close the TCP connection
    pass



    print(data.decode())


if __name__ == '__main__':
    main()
