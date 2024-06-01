import subprocess
import time
import os

class Nmap:
    def __init__(self, target):
        self.target = target

    def scan(self, options):
        try:
            command = ["nmap"] + options.split() + [self.target]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return result.stdout, result.returncode
            else:
                return f"Error: {result.stderr}\n", result.returncode
        except FileNotFoundError:
            return "Error: nmap not found. Please install nmap and try again.\n", 1

def clear_console():
    print("\033c", end="")

def get_input(prompt, exit_option="0"):
    while True:
        user_input = input(prompt).strip()
        clear_console()
        if user_input == exit_option:
            return None
        if user_input:
            return user_input
        print(f"Invalid input. Please enter a value or press {exit_option} to return.")

def start_scan(helper, options):
    print("*" * 60)
    print("Scan starting... please wait.\n")
    time.sleep(1)
    try:
        result, exit_code = helper.scan(options)
        print(result)
        print("*" * 60)
        print(f"Scan completed with exit code: {exit_code}\n")

        save_log = get_input("Would you like to save the log output? (yes/no): ").lower()
        if save_log == "yes":
            output_file = f"nmap_scan_{int(time.time())}.log"
            new_filename = get_input("Would you like to give a custom name to the log file? (leave empty for default): ", exit_option="")
            if new_filename:
                new_filename = new_filename if new_filename.endswith(".log") else new_filename + ".log"
                output_file = new_filename
            with open(output_file, "w") as f:
                f.write(result)
            print(f"Output saved to {output_file}\n")
        else:
            print("Log output not saved.\n")

    except KeyboardInterrupt:
        print("\nScan interrupted. Returning to the main menu...\n")

def display_operations(operations):
    print("Operations:\n")
    keys = list(operations.keys())
    half = (len(keys) + 1) // 2
    for i in range(half):
        key1 = keys[i]
        key2 = keys[i + half] if i + half < len(keys) else ""
        desc1 = operations[key1]["description"]
        desc2 = operations[key2]["description"] if key2 else ""
        print(f"  {key1:2}) -> {desc1:35}  {key2:2}) -> {desc2}")
    print("\n  0) -> QUIT")

def main():
    ascii_art = """
 _  _ __  __   _   ___ _    ___ _____ ___ 
| \| |  \/  | /_\ | _ \ |  |_ _|_   _| __|
| .` | |\/| |/ _ \|  _/ |__ | |  | | | _| 
|_|\_|_|  |_/_/ \_\_| |____|___| |_| |___|
                                                                   
by @mikropsoft
"""
    print(ascii_art)
    time.sleep(1)

    operations = {
        1:  {"description": "Intense Scan", "command": "-T4 -A -v"},
        2:  {"description": "Intense Scan Plus UDP", "command": "-sS -sU -T4 -A -v"},
        3:  {"description": "Intense Scan, All TCP Ports", "command": "-p 1-65535 -T4 -A -v"},
        4:  {"description": "Intense Scan, No Ping", "command": "-T4 -A -v -Pn"},
        5:  {"description": "Ping Scan", "command": "-sn"},
        6:  {"description": "Quick Scan", "command": "-T4 -F"},
        7:  {"description": "Quick Scan Plus", "command": "-sV -T4 -O -F --version-light"},
        8:  {"description": "Quick Traceroute", "command": "-sn --traceroute"},
        9:  {"description": "Regular Scan", "command": ""},
        10: {"description": "Slow Comprehensive Scan", "command": "-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script discovery,safe"},
        11: {"description": "Scan Specific Ports", "command": "-p "},
        12: {"description": "Service Version Detection", "command": "-sV"},
        13: {"description": "OS Detection", "command": "-O"},
        14: {"description": "Aggressive Scan", "command": "-A"},
        15: {"description": "Detect Firewall", "command": "--script firewall-bypass"},
        16: {"description": "Scan for Vulnerabilities", "command": "--script vuln"},
        17: {"description": "Scan for Malware", "command": "--script malware"},
        18: {"description": "Scan with NSE Scripts", "command": "--script "},
        19: {"description": "Detect Heartbleed Vulnerability", "command": "--script ssl-heartbleed"},
        20: {"description": "Traceroute and Geolocation", "command": "--traceroute --script traceroute-geolocation"}
    }

    while True:
        try:
            display_operations(operations)
            operation_input = get_input("\n> Choose operation: ")
            if operation_input is None:
                print("\nExiting the tool. Goodbye!")
                break

            try:
                operation = int(operation_input)
                if operation == 0:
                    print("\nExiting the tool. Goodbye!")
                    break
                if operation not in operations:
                    print("Invalid operation\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            print("\n" + "*" * 60)
            print(ascii_art)
            print("Press ctrl + c to close the tool.")
            targets = get_input("\n> Enter targets (Example: IP or website - 192.168.1.1 or example.com), or enter 0 to return: ")
            if targets is None:
                continue

            additional_options = get_input("\n> Enter additional options for the scan (leave empty for default): ", exit_option="")
            if additional_options is None:
                additional_options = ""

            helper = Nmap(targets)
            options = f"{operations[operation]['command']} {additional_options}".strip()
            start_scan(helper, options)

        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting the tool. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
