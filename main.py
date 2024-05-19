import subprocess

class Nmap:
    def __init__(self, target):
        self.target = target

    def scan(self, options):
        try:
            command = ["nmap"] + options.split() + [self.target]
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout, result.returncode
        except FileNotFoundError:
            return "Error: nmap not found. Please install nmap and try again.\n", 1
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}\n", e.returncode

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
    try:
        result, exit_code = helper.scan(options)
        print(result)
        print("*" * 60)
        print(f"Scan completed with exit code: {exit_code}\n")
    except KeyboardInterrupt:
        print("\nScan interrupted. Returning to the main menu...\n")

def display_operations(operations):
    print("\nOperations:")
    for key, value in operations.items():
        print(f"  {key}) -> {value['description']}")
    print("  0) -> QUIT")

def main():
    ascii_art = """

 _  _ __  __   _   ___ _    ___ _____ ___ 
| \| |  \/  | /_\ | _ \ |  |_ _|_   _| __|
| .` | |\/| |/ _ \|  _/ |__ | |  | | | _| 
|_|\_|_|  |_/_/ \_\_| |____|___| |_| |___|
                                                                   
by @mikropsoft

"""
    print(ascii_art)

    operations = {
        1: {"description": "Intense Scan", "command": "-T4 -A -v"},
        2: {"description": "Intense Scan Plus UDP", "command": "-sS -sU -T4 -A -v"},
        3: {"description": "Intense Scan, All TCP Ports", "command": "-p 1-65535 -T4 -A -v"},
        4: {"description": "Intense Scan, No Ping", "command": "-T4 -A -v -Pn"},
        5: {"description": "Ping Scan", "command": "-sn"},
        6: {"description": "Quick Scan", "command": "-T4 -F"},
        7: {"description": "Quick Scan Plus", "command": "-sV -T4 -O -F --version-light"},
        8: {"description": "Quick Traceroute", "command": "-sn --traceroute"},
        9: {"description": "Regular Scan", "command": ""},
        10: {"description": "Slow Comprehensive Scan", "command": "-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script discovery,safe"}
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
