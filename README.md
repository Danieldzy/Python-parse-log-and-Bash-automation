<h1>Python code for log parsing, Bash for automation</h1>


<h2>Description</h2>
The project consists of a simple Python script that parses log files based on the Regex pattern, for the script please refer to the Python_script.py file
Also, a bash script to automate the backup of logs or sensitive data with time stamps
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Bash</b>

<h2>Environments Used </h2>

- <b>Ubuntu Linux</b> 

<h2>Program walk-through:</h2>



<p align="center">
Import Regex and define file path: <br/>
<img src="https://i.imgur.com/ksK0Hfn.png" height="80%" width="80%" alt="Import re module"/>



<br />
Define parse_log function:  <br/>
<img src="https://i.imgur.com/NQTRYDH.png" height="80%" width="80%" alt="Define parse_log"/>



<br />
Print out parse_log function:  <br/>
<img src="https://i.imgur.com/2YCbRSG.png" height="80%" width="80%" alt="Print out parse_log function"/>
<br />
<br />
Format the output, and print out the dictionary that we need:  <br/>
<img src="https://i.imgur.com/D8rkEpp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />


The final output is a dictionary that filters out error codes 403 and 404 along with their associated IP addresses and error code counts. The output shows only 2 counts of the 403 error but significantly more counts of the 404 error, with a notable 60 counts of 404 errors from IP address 208.91.156.11.  <br/>

<br />
<br />

Use Bash to automate file backup  <br/>
<br />
Print out parse_log function:  <br/>
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
