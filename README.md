<h1>Python code for log parsing, Bash for automation</h1>


<h2>Description</h2>
The project includes a simple Python script, Python_script.py, that parses log files using a Regex pattern, as well as a bash script designed to automate the backup of logs or sensitive data with timestamps. Both scripts can be found in this repository.
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

<h1>Use Bash to automate file backup  </h1>
<br />
Bash Script is used to back up file member_data.txt, I’ve incorporated a timestamp into the script. This means the filename will bear a new timestamp each time a backup is made, the new file will be saved in /home/Autobackup directory:  <br/>
<img src="https://i.imgur.com/AOTpcmQ.png" height="80%" width="80%" alt="Backup member_data.txt"/>
<br />
<br />

Next, we are creating a Cron job to schedule and automate this backup process Every Wednesday at 12:00 AM. First, we use nano to edit crontab, add the cron command:0 0 * * 3 / home/student/bashbackup.sh:  <br/>
<img src="https://i.imgur.com/5kkD3GT.png" height="80%" width="80%" alt="Backup member_data.txt"/>

<br />

With these Bash scripts, the system will automatically backup file member_data.txt Every Wednesday at 12:00 AM and save it to the Autobackup directory with a new time stamp.
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
