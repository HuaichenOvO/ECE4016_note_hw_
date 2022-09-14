<font color = grey>

# <font color = Purple>1 Intro and Overview</font>
[上一章](/notes/CPT0.md)
[下一章](/notes/CPT0.md)
## <font color = PaleVioletRed>TA contact</font>

Dayou Zhang (张大猷): 221019044@link.cuhk.edu.cn

Boxiang Zhu (朱伯湘): 222010011@link.cuhk.edu.cn

Panlong Wu (吴攀龙): 222010016@link.cuhk.edu.cn

## <font color = PaleVioletRed>Grading </font>

<table bgcolor = NavajoWhite>
<tr>
    <td>Assignment: 20% + 5% + 15% = 40% (May have bonus)
<tr>
    <td>Quiz/ Attendance: 5%
<tr>
    <td>Final 35%
</table>

<table bgcolor = NavajoWhite>
<tr>
    <td>Assignment1: 
    <td>measure end-to-end throughput and delay of networks (i.e., simple speed test)
<tr>
    <td>Assignment2: 
    <td>video streaming from CDNs (i.e., simple Netflix)
<tr>
    <td>Assignment3:
    <td>reliable transport (i.e., how to transfer data over an unreliable network)
<tr>
    <td>All on (emulated) realistic networks using mininet
</table>

## <font color = PaleVioletRed>Two ways to share switched networks </font>

<table bgcolor = NavajoWhite>
<tr> 
    <td >circuit switching 
    <td>simple and fast
    <td>switch fails == all fail; extremely inefficient
<tr>
    <td>packet switching 
    <td>efficient & Simpler
    <td>requires buffer
</table>

## <font color = PaleVioletRed>Performance metrics </font>

<table bgcolor = NavajoWhite>
<tr> 
    <td rowspan="5"> Delay
<tr> 
    <td>Transmission Delay 
    <td>
    <td rowspan="2">和link本身有关 
<tr> 
    <td>Propagation Delay 
    <td>Time for one bit to move through the link 
<tr> 
    <td>Queuing Delay
    <td rowspan="2">due to to traffic mix and 
switch internals
<tr> 
    <td>Processing Delay

<tr> 
    <td>Milk
    <td> white cold drink
</table>

<font color = navy>
Transmission delay = Packet size / Transmission rate of the link 

$\text{e.g. } TD = {1000 bits} / {(100 Mb/s)} = 10^{-5}s$

Propagation delay= Link length /Propagation speed of link （默认是光速）

$\text{e.g. } PD = {30 km} / {(3*10^8 km/s)} = 10^{-4}s$

例题：<br>
Link with 1Mbps, 1ms <br>
Packet delay = Transmission delay + Propagation delay = 
![P2](/pics/L1P1.png)
${30 km} / {(3*10^8 km/s)} = 10^{-4}s$


</font>

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"