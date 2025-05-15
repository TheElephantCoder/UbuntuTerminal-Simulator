import os
import subprocess

def ubuntu_terminal_simulator():
    print("Ubuntu Terminal Simulator")
    print("Type 'exit' to quit.\n")

    while True:
        # Display a prompt
        current_dir = os.getcwd()
        command = input(f"{current_dir}$ ")

        # Exit the simulator
        if command.lower() == "exit":
            print("Exiting Ubuntu Terminal Simulator.")
            break

        # Simulated commands
        simulated_commands = {
            "ls": "\n".join(os.listdir(current_dir)),
            "pwd": current_dir,
            "whoami": os.getlogin(),
            "date": subprocess.getoutput("date"),
            "uname": subprocess.getoutput("uname"),
            "echo Hello World": "Hello World",
            "clear": "\033c",
            "cat /etc/os-release": subprocess.getoutput("cat /etc/os-release"),
            "df -h": subprocess.getoutput("df -h"),
            "free -m": subprocess.getoutput("free -m"),
            "ps aux": subprocess.getoutput("ps aux | head -10"),
            "top": "Simulated 'top' command (Press 'q' to exit)",
            "man ls": "Simulated 'man' page for 'ls'. Use 'ls' to list files.",
            "grep": "Usage: grep [OPTION]... PATTERN [FILE]...",
            "sudo": "Simulated 'sudo' command. You do not have admin privileges.",
            "curl": "Usage: curl [options...] <url>",
            "ping google.com": "PING google.com (172.217.164.238): 56 data bytes\n64 bytes from 172.217.164.238: icmp_seq=0 ttl=118 time=10.3 ms",
            "mkdir test_dir": "Created directory: test_dir",
            "rm -rf test_dir": "Removed directory: test_dir",
            "touch test_file": "Created file: test_file",
        }

        # Check if the command is simulated
        if command in simulated_commands:
            output = simulated_commands[command]
            print(output)
            if command == "clear":
                os.system("cls" if os.name == "nt" else "clear")
        else:
            # Execute the command
            try:
                result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(result.stdout, end="")
                if result.stderr:
                    print(result.stderr, end="")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    ubuntu_terminal_simulator()
