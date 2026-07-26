'NETWORKING'
'''
Networking in Python is the process of using Python programs 
to communicate and exchange data between two or more devices
over a network using networking protocols such as TCP/IP or 
UDP. Python provides the built-in socket module to create 
client-server applications and enable communication between 
computers
'''

'Types of Networking'

'A.Local connection (locallost)'
'''
-We use localhost in networking because it lets a program 
communicate with the same computer it is running on 
-Client and server on the same computer
'''

'B.LAN connection'
'''
-Another system on the same network 
-Client and server on different computers in the same Wi-Fi/LAN
'''

'C.Remote/Internet connection'
'''
-Another system over the Internet
-Client and server on computers over the Internet
'''

'Code - System 01 for LAN connection OR localhost CMD TAB 01 for localhost'
'server.py program'

import socket 
HOST = "127.0.0.1" #localhost 
PORT = 65531

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print(f"Server listening on{HOST}:{PORT}")
    
    conn ,addr = s.accept()
    with conn:
        print("Connected by:",addr)
        data=conn.recv(1024)
        print("Received :",data.decode())
        conn.sendall(b"Hello ! from Server")
        
'AA.Concepts'

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

'7.bind()'
'''
-bind() associates a socket with a specific IP address and port number.
-It tells the operating system this server will use this IP address and this port
-Syntax:
 s.bind((HOST, PORT))
'''

'8.listen()'
'''
-listen() puts the server into listening mode, allowing it to wait for incoming client 
connection requests
-the server waits patiently until a client connects'''

'9.conn, addr = s.accept()'
'''
where,
conn - is the new communication socket
addr - is the client's IP address and port
s.accept()
-accept() waits for an incoming client connection. When a client connects, it creates a 
new socket dedicated to communicating with that client'''

'''
NOTE : 
Why create a new socket?
The original server socket continues listening for future clients.
The new conn socket is used for the current client's conversation.
This allows the server to accept more clients late'''

'10.with conn :'
'''
-with conn: means "Use this client connection, and when you're done, automatically close it'''

'11.recv(1024)'
'''
-recv() receives data sent by the connected client
-1024 means the server can receive up to 1024 bytes in one call'''

'12.decode()'
'''
-Data transmitted over a network is sent as bytes, not normal Python strings.
-decode() converts bytes into a readable string'''

'13.sendall()'
'''
-sendall() sends data through the socket and ensures that all the data is transmitted
'''

'14.b'
'''
-conn.sendall(b"Hello from Server")
The b before the string means it is being sent as bytes, which is the standard format for
network communication
'''



'BB.Execution'

'''
BB.1.Execution Steps (When Using 127.0.0.1 - Localhost)

Here, both the server and client run on the same computer.


-first save both program in same directory or folder 
-then open cmd (tab 01 )from that directory which we saved programs
-in cmd type 
py server.py 

-then press Enter 
 
Step 1: Start the Server
HOST = "127.0.0.1"
PORT = 65531
The server creates a socket.
It binds to 127.0.0.1:65531.
It starts listening for incoming connections.

Output:
Server listening on 127.0.0.1:65531



after that 
-then open cmd (tab 02 )from that directory which we saved programs
-in cmd type 
py client.py 

-then press Enter 



Step 2: Start the Client
The client also uses
HOST = "127.0.0.1"
PORT = 65531

The client creates a socket and executes
s.connect((HOST, PORT))
Since the server is already listening on 127.0.0.1:65531, the connection is established.



Step 3: Server Accepts the Connection

The server executes
conn, addr = s.accept()

Example output:
Connected by: ('127.0.0.1', 52148)

Here,

127.0.0.1 → Client IP (same computer)
52148 → Temporary (ephemeral) port assigned to the client by the operating system
Step 4: Client Sends Data

Client:

s.sendall(b"Hello ! from client")

Server receives:

data = conn.recv(1024)

Output:
Received : Hello ! from client
Step 5: Server Sends Reply

Server:

conn.sendall(b"Hello ! from Server")

Client receives:

data = s.recv(1024)

Output:
Received: Hello ! from Server'''




'BB.2.Execution Steps (Different Computers)'
'''
Suppose:

Server Computer

IP Address
192.168.1.100

Client Computer

IP Address
192.168.1.105

Both computers must be connected to the same network (or otherwise able to reach each other).



Step 1: Change the Server HOST

Instead of
HOST = "127.0.0.1"

use the server computer's IP address:
HOST = "192.168.1.100"

or, to listen on all network interfaces:
HOST = "0.0.0.0"

0.0.0.0 means:
"Accept connections on any IP address assigned to this computer."



Step 2: Run the Server
system 01 
The server starts listening.

Output:
Server listening on 192.168.1.100:65531
(or it will still print 0.0.0.0:65531 if that's what you set as HOST).




Step 3: Change the Client HOST
system 02 
The client must connect to the server's IP address, not its own.

HOST = "192.168.1.100"

Then:
s.connect((HOST, PORT))



Step 4: Server Accepts the Connection

Output:
Connected by: ('192.168.1.105', 53210)

Meaning:
192.168.1.105 → Client's IP address
53210 → Client's temporary port number



Step 5: Communication Begins

Client
Hello ! from client

↓

Server receives it.

↓

Server replies
Hello ! from Server
'''


 