# UAH-Xploit

This repository contains an RCE exploit for the U.A High School THM Room, targeting a vulnerable PHP page.

# Usage

After configuring the attacker's IP & port and specifying the target URL/IP, we can execute the script.

Upon execution, we get two options:

1️⃣ Interactive Shell – Allows us to execute commands one by one and receive responses directly in the terminal.

2️⃣ Reverse Shell – Establishes a persistent shell connection, redirecting the session to nc for better control.

    ┌──(kali㉿kali)-[~/UAH-Xploit]
    └─$ python UAH-Xploit.py
    [1] Interactive Shell
    [2] Get Reverse Shell
    Choose an option: 


Why Two Options?

Having both options provides flexibility in different attack scenarios:

Interactive Shell is useful for running single commands when the system is unstable or when we need specific output without maintaining an open connection.

Reverse Shell is more practical when we want a continuous session with full interactive access, allowing us to move deeper into the system.


# Interactive Shell

If the Interactive Shell option is selected, the script follows these steps:

Encodes the command using URL encoding to ensure safe transmission.

Sends the command to the vulnerable PHP script (index.php?cmd=<COMMAND>).

Receives the response in Base64, as encoded by the web application.

Decodes the Base64 output and prints the actual command result in the terminal.


    ┌──(kali㉿kali)-[~/UAH-Xploit]
    └─$ python UAH-Xploit.py 
    [1] Interactive Shell
    [2] Get Reverse Shell
    Choose an option: 1
    [*] Enter commands (type 'exit' to quit)
    SHELL> whoami

    [+] Command Output:
    www-data
    
    SHELL> 



# Reverse Shell

If the Reverse Shell option is selected, the script:

Generates a Base64-encoded Python reverse shell payload.

Sends it to the vulnerable server.

Opens a persistent shell connection to the attacker's machine.

Before executing the Reverse Shell option, start a listener on your attacking machine:
        
    nc -lvnp <YOUR_PORT>
    
Run the exploit and select 2 to spawn a reverse shell.

    ┌──(kali㉿kali)-[~/UAH-Xploit]
    └─$ python UAH-Xploit.py
    [1] Interactive Shell
    [2] Get Reverse Shell
    Choose an option: 2
    [*] Launching Reverse Shell...

# Post-Connection TTY Upgrade (nc)

Background the shell
    
    Ctrl + Z

Fix terminal settings
    
    stty raw -echo; fg

Reset terminal
    
    reset

Fix display & enable colors

    export TERM=xterm-256color; exec /bin/bash

# Features

Execute remote commands dynamically – No need for manual payload crafting.

Receive command output in Base64 format and decode it – Ensures clean, readable output even when special characters or multi-line responses are returned.

Keeps the session interactive for continuous command execution – Instead of manually sending each request via Burp Suite, this script allows seamless interaction with the target, making exploitation faster and more efficient.
