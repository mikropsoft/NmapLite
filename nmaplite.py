import subprocess
import time
import os
import re
from datetime import datetime

class NmapScanner:
    def __init__(self, target):
        self.target = target

    def run_scan(self, options, log_file):
        cmd = ["nmap"] + options.split() + [self.target]
        start = time.time()
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            duration = time.time() - start
            with open(log_file, "w") as file:
                file.write(result.stdout)
            return result.stdout, duration
        except subprocess.CalledProcessError as e:
            return e.stderr, None
        except FileNotFoundError:
            return "Nmap not installed or not found in PATH.", None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_with_prompt(prompt):
    user_input = input(f"\033[92m{prompt}\033[0m").strip()
    return user_input if user_input else None

def validate_target(target):
    pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}|(?:\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, target)

def save_scan_log(default_name):
    choice = input_with_prompt("Save log file? (y/n): ")
    if choice and choice.lower() == 'y':
        custom_name = input_with_prompt("Custom log filename (leave empty for default): ")
        final_name = f"{custom_name}.log" if custom_name else default_name
        os.rename(default_name, final_name)
        print(f"Log saved as {final_name}\n")
    else:
        os.remove(default_name)
        print("Log discarded.\n")

def scan_menu():
    scans = {
        "1": ("Intense Scan", "-T4 -A -v"),
        "2": ("Intense Scan + UDP", "-sS -sU -T4 -A -v"),
        "3": ("All TCP Ports", "-p 1-65535 -T4 -A -v"),
        "4": ("No Ping Scan", "-T4 -A -v -Pn"),
        "5": ("Ping Scan", "-sn"),
        "6": ("Quick Scan", "-T4 -F"),
        "7": ("Quick Scan Plus", "-sV -T4 -O -F --version-light"),
        "8": ("Traceroute Scan", "-sn --traceroute"),
        "9": ("Regular Scan", ""),
        "10": ("Slow Comprehensive", "-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script discovery,safe"),
        "11": ("Specific Ports", "-p "),
        "12": ("Service Detection", "-sV"),
        "13": ("OS Detection", "-O"),
        "14": ("Aggressive Scan", "-A"),
        "15": ("Firewall Detection", "--script firewall-bypass"),
        "16": ("Vulnerability Scan", "--script vuln"),
        "17": ("Malware Scan", "--script malware"),
        "18": ("Custom NSE Script", "--script "),
        "19": ("Heartbleed Check", "--script ssl-heartbleed"),
        "20": ("Traceroute Geolocation", "--traceroute --script traceroute-geolocation"),
    }

    for key, (desc, _) in scans.items():
        print(f"\033[94m[{key:2}]\033[0m {desc}")
    print("\033[91m[0]\033[0m Quit")

    return scans

def main():
    clear_console()
    print("\033[96m" + r"""
 _____ _____ _____ _____ __    _____ _____ _____
|   | |     |  _  |  _  |  |  |     |_   _|   __|
| | | | | | |     |   __|  |__|-   -| | | |   __|
|_|___|_|_|_|__|__|__|  |_____|_____| |_| |_____|
by @mikropsoft
""" + "\033[0m")

    while True:
        scans = scan_menu()
        choice = input_with_prompt("\nSelect scan type (0 to quit): ")
        if choice == "0":
            print("\nExiting...\n")
            break
        if choice not in scans:
            print("Invalid selection. Try again.\n")
            continue

        target = input_with_prompt("Enter IP/Hostname: ")
        if not target or not validate_target(target):
            print("Invalid target. Try again.\n")
            continue

        extra = input_with_prompt("Additional options (optional): ") or ""
        scan_type, default_opts = scans[choice]
        if default_opts.strip().endswith("-p"):
            ports = input_with_prompt("Enter ports (e.g., 80,443): ")
            if not ports:
                print("Ports required. Returning...\n")
                continue
            default_opts += ports

        log_name = f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        scanner = NmapScanner(target)
        print("\033[93mStarting scan...\033[0m\n")
        result, duration = scanner.run_scan(f"{default_opts} {extra}".strip(), log_name)

        print(result)
        if duration:
            print(f"\033[92mScan completed in {duration:.2f} seconds.\033[0m\n")
            save_scan_log(log_name)
        else:
            print(f"\033[91mScan failed: {result}\033[0m\n")

        input("Press Enter to continue...")
        clear_console()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91mExited by user.\033[0m\n")
