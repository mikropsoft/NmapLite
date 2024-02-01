import subprocess

class Nmap:
    def __init__(self, target):
        self.target = target

    def scan(self, options):
        try:
            command = ["nmap", options, self.target]
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout, result.returncode
        except FileNotFoundError:
            return "Error: nmap not found. Please install nmap and try again.\n", 1
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}\n", e.returncode

def print_separator(length=60):
    print("*" * length)

def get_targets():
    try:
        while True:
            targets = input("Input targets (Example: IP or website - 192.168.1.1 or example.com):\n").strip()
            if targets == "0" or not targets:
                return targets
            print("Invalid input. Please enter targets or press 0 to return.\n")
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Returning to the main menu...\n")
        return "0"

def start_scan(helper, options):
    print_separator(15)
    print("Scan starting... please wait.")
    print()
    try:
        result, exit_code = helper.scan(options)
        print(result)
        print_separator(15)
        print(f"Scan completed with exit code: {exit_code}")
    except Exception as e:
        print(f"Error: {e}\n")
    print("\n")

operations = {
    1: {"description": "Intense scan", "command": "-T4 -A -v"},
    2: {"description": "Intense scan plus UDP", "command": "-sS -sU -T4 -A -v"},
    3: {"description": "Intense scan, all TCP ports", "command": "-p 1-65535 -T4 -A -v"},
    4: {"description": "Intense scan, no ping", "command": "-T4 -A -v -Pn"},
    5: {"description": "Ping scan", "command": "-sn"},
    6: {"description": "Quick scan", "command": "-T4 -F"},
    7: {"description": "Quick scan plus", "command": "-sV -T4 -O -F --version-light"},
    8: {"description": "Quick traceroute", "command": "-sn --traceroute"},
    9: {"description": "Regular scan", "command": ""},
    10: {"description": "Slow comprehensive scan", "command": """nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" """
    },
}

def print_operations():
    print("Operations:")
    for key, value in operations.items():
        print(f"{key}) -> {value['description']}")
    print("0) -> QUIT")

def main():
    try:
        while True:
            print_operations()

            try:
                operation = int(input("Choose operation: "))
                if operation not in operations and operation != 0:
                    print("Invalid operation\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            if operation == 0:
                print("Exiting the tool. Goodbye!")
                break

            while True:
                print_separator()
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = get_targets()

                if targets == "0":
                    print("Returning to the main menu...\n")
                    break

                try:
                    helper = Nmap(targets)
                    start_scan(helper, operations[operation]["command"])
                except KeyboardInterrupt:
                    print("\nCtrl+C detected. Returning to the main menu...\n")
                    break
                except Exception as error:
                    print(f"Error: {error}\n")
                    break
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting the tool. Goodbye!\n")

if __name__ == "__main__":
    main()
