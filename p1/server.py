from os import access
import socket
import sys

IP_and_PORT = ("127.0.0.1", 1234)

"""
Basic function of server's socket creation, binding, listening, recv/sending and closing
"""
def server():
    # 1 server/client socket creation
    try:
        server_instance = socket.socket()  # by default family=AF_INET, indicating IPv4 address family
        print("[Server] Socket created")

        server_instance.bind(IP_and_PORT)
        print("[Server] Socket binded")

        server_instance.listen(5) # the number of unaccepted connections that the system will allow before refusing new connections = 5
        print("[Server] Socket listening mode configured")
    except socket.gaierror or socket.error as err:
        print("[Server] Before able to accept, this program failed with an error %s" % (err))
        sys.exit()

    # 4 server socket accpeting
    # if accepted, <<<<new>>>> create a new thread and let it due with the communication
    # while True:
    try:
        new_socket_target, new_IP_addr = server_instance.accept()
        print("[Server] Connected to ", new_IP_addr)

        new_socket_target.send(("<Server> You have connected to the server succcessfully: PORT=%s" %str(IP_and_PORT[1])).encode())

        new_socket_target.close()

    except socket.gaierror or socket.error as err:
        print("[Server] Connection with an error: %s" % (err))
        sys.exit()

        # break
    server_instance.close()

"""
Uses an priority queue to implement the IP cache
"""


if __name__ =="__main__":
    server()