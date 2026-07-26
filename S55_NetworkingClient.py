
'Code -System 02 for LAN connection OR localhost CMD TAB 02 for localhost'
'client.py program'

import socket 
HOST = "127.0.0.1" #localhost 
PORT = 65531

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.connect((HOST,PORT))
    s.sendall(b"Hello ! from client")
    data =s.recv(1024)
    print("Recevied:",data.decode())


'Concepts'

'1.socket'
'''
-It is python built in module 
-a socket is a software endpoint that enables two programs or two computers to communicate
over a network. It provides a way to send and receive data between applications'''

'2.HOST'
'''
-A host means the computer's address
-Every computer connected to a network has an address called an IP address
-It identifies which computer should receive the data
-Eg . 
192.168.1.5
172.16.0.1
10.0.0.2
127.0.0.1 # this is a localhost 
'''

'3.PORT'
'''
- A port is a logical communication endpoint used to identify a specific
  application or service running on a computer.
- A computer can run many network applications simultaneously.
- Each network service or application listens on a unique port number
  so that the operating system knows which application should receive
  incoming network data.
'''

'''
NOTE
with ....as s :

- 'with' creates a context manager that automatically manages the socket.
- 'as s' creates an alias (reference) named 's' for the socket object.
- The variable 's' is used to perform socket operations such as
  bind(), listen(), connect(), send(), and recv().
- When the 'with' block ends, Python automatically closes the socket,
  so there is no need to call s.close() manually
'''

'4.socket.socket()'
'''
This part creates a new socket object which is like opening a commnication endpoint '''


'5.socket.AF_INET'
'''
-AF_INET stands for Address Family - Internet (IPv4)
-It tells Python, This socket will use IPv4 addresses
'''

'6.socket.SOCK_STREAM'
'''
-SOCK_STREAM tells Python to create a TCP socket
-Since TCP provides reliable communication

 6.1 TCP
-TCP (Transmission Control Protocol) is a communication protocol that provides reliable 
and ordered delivery of data between two devices'''


'7.s.connect((HOST,PORT))'
'''
-connect() establishes a connection between the client and the server'''

'8.sendall()'
'''
-sendall() sends data through the socket and ensures that all the data is transmitted
'''

'09.b'
'''
-conn.sendall(b"Hello from Server")
The b before the string means it is being sent as bytes, which is the standard format for
network communication
'''
'10.recv(1024)'
'''
-recv() receives data sent by the connected client
-1024 means the server can receive up to 1024 bytes in one call
'''

'11.decode()'
'''
-Data transmitted over a network is sent as bytes, not normal Python strings.
-decode() converts bytes into a readable string'''

