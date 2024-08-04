<h1>SSH Brute Force Attack Script</h1>


<h2>Description</h2>
This Python script performs a brute-force attack on an SSH server to find the correct password for a specified user. It leverages the pexpect library to automate interactions with the SSH server, handling initial connections and password prompts. The script reads passwords from a "Passwords.txt" file and attempts each one in succession, checking if it successfully logs in. If a successful login is detected, it prints the discovered password and executes a whoami command on the target machine. 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>Kali Linux</b>

<h2>Program walk-through:</h2>

<p align="center">
Sample Text File Containing Passwords: <br/>
<img src="https://imgur.com/GgK0Ds3.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The User Is Asked For The IP Address Of The Target:  <br/>
<img src="https://imgur.com/llT8Yny.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The User Is Asked For The Accounts Username:  <br/>
<img src="https://imgur.com/YQf3M6z.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The Script Tries All Passwords From The Passwords.TXT File to Brute Force:  <br/>
<img src="https://imgur.com/TKlpVx2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
