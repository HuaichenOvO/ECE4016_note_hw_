import socket
import sys
import dnslib

# socket    connect     receive/send    close

# Use a variable flag to indicate whether ask the public server for the IP address. 
# When the flag is set to be 0 , ask the public server for the IP address. 
# When the flag is set to be 1 , do the recursive/iterative searching

IP_and_PORT = ("127.0.0.1", 1234)


def client():
    # 1 client socket creation
    # 2 client socket connection
    try:
        client_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # INET means IPv4, SOCK_STREAM means TCP type
        print("[Client] Socket created")

        client_instance.connect(IP_and_PORT)  # 连接到服务器
        print("[Client] Socket connected to HOST: %s" %str(IP_and_PORT))

    except socket.error or socket.gaierror as err:
        print("[Client] Client socket failed with an error %s" % (err))
        sys.exit()

    # 3 client socket recv/send
    try:
        print (client_instance.recv(100).decode())
    except socket.error or socket.gaierror as err:
        print("[Client] Receiving failed with an error %s" % (err))
        sys.exit()

    # 4 client socket close
    client_instance.close()

if __name__ =="__main__":
    client()
    
    # client()