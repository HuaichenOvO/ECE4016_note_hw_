<font color='SteelBlue'>

# <font color='ForestGreen'><b>Detailed grading rule</b></font>

### <b>The local DNS server should have the following function:</b>

Listen and accept the DNS queries

Send response to the clients

Maintain a __cache__. If the ip address is quried before, it should be stored in the cache. if the answer for the query is found in cache, Local DNS Server send this answer to lient as the DNS response **(20 points)**

Support __direct search__ to the public DNS server **(15 points)**

Support __recursive/iterative__ searching **(25 points)** 二选一

Support __A(25 points)__ and __CNAME(15 points)__ type queries

# <font color='ForestGreen'><b>Requirements</b></font>

<font color='red'>Due: Oct.16, 23:59</font>

The server is required to work on __port 1234 of 127.0.0.1__

You can use __dig__ to test your local DNS server.

__e.g.__: 

<i>dig www.example.com @127.0.0.1 -p 1234</i>

<i>dig www.baidu.com @127.0.0.1 -p 1234</i>
