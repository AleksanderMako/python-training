
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
#add wifi interface
host = '*'
print(host)
serversocket.bind((host, 8000))
# become a server socket
serversocket.listen(1)

# accept connections from outside
(clientsocket, address) = serversocket.accept()
print("Accepted smth")

filname = "ipfs-p2p-file-system.pdf"
myfile = open(filname,"rb")
msg = "HTTP/1.1 200 OK\n"+"Content-Type: application/pdf\n" +"\n"

clientsocket.send(msg.encode()+myfile.read()+"\n".encode())
clientsocket.close()
