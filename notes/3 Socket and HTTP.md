<font color = grey>

# <font color = Purple>3 Socket and HTTP</font>
[Branch: 2 Layering](/notes/2%20Layering.md)
||
[Branch: 4 CDN DNS]()


## <font color = PaleVioletRed>1. Layer Review</font>

<img src="../pics/L3P1.png" width=400>

## <font color = PaleVioletRed>2. Socket</font>
### <font color = PaleVioletRed>2.1 Definition</font>
Most programming are for application layer stuff. For inter-app communication, people need network programming.<br>
Socket: the simplest interface between App and Trans. <font color=#705000>It is a <b>host-local</b>, <b>application-created</b>, <b>OS-controlled</b> interface (a “door”) into which application process can both send and receive messages to/from another application process</font>

<font color=#705000><b>One socket is tied to one application process (or thread). </b>An application can create many processes (and hence sockets)</font>

### <font color = PaleVioletRed>2.2 Socket programming using TCP</font>

TCP service: reliable transfer of bytes from one process to another. <br>
An application may view TCP as a reliable queue structure.

    Process:
    
    Before Client contacts Server:
        1. server process must first be running
        2. server must have created socket (door) that welcomes client’s contact

    Client contacts server by: 
        1. creating client-local TCP socket
        2. specifying IP address, port number of server process
        3. when client creates socket: client TCP establishes connection to server TCP

    When contacted by client,:
        server creates new TCP socket for server process to communicate with client
        so: allows server to talk with multiple clients
        and: source port numbers used to distinguish clients

<img src="../pics/L3P2.png" width=400>

The process of TCP socket<br>
Other content neglected

## <font color = PaleVioletRed>3 Socket's Addressing Process</font>
IP + port number<br>
e.g. <br>
HTTP server: 80<br>
Mail server: 25<br>
To send HTTP message to sse.cuhk.edu.cn web server: <br>
IP address: <font color=SandyBrown>137.189.91.182</font>; Port number: <font color=SeaGreen>80</font>


### <font color = PaleVioletRed>3.1 Illustrations</font>

HTTP server uses fixed port number (80)<br>
while HTTP client can use self-defined ones

<img src="../pics/L3P3.png" width=600>


## <font color = PaleVioletRed>4 Web Components</font>

Clients and Servers<br>
URL & HTML<br>
Protocol of Info trsansmittion


## <font color = PaleVioletRed>4.1 URL</font>
URL: 
<font color=SandyBrown>Protocol://</font><font color=LightSeaBlue>host_name[:port]/</font><font color=maroon>directory_path/</font><font color=SeaGreen>resource</font> <br>
e.g.: <font color=SandyBrown>https://</font><font color=LightSeaBlue>github.com/</font><font color=maroon>HuaichenOvO/</font><font color=SeaGreen>ECE4016_note_hw_</font>

<b>Protocol</b> includes http, ftp, smtp, etc<br>
<b>Host_name</b> can be a DNS name or an IP address<br>
<b>port</b> e.g. http:80, https:443<br>
<b>dir_path</b> follows that of the file system<br>
<b>resource</b> files/other Info

## <font color = PaleVioletRed>4.2 HTTP Protocol</font>

<img src="../pics/L3P4.png" width=400>

Process

APIs:
GET, HEAD, PUT, DELETE
