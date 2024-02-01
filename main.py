import subprocess

class Nmap:
    def __init__(self, target):
        self.target = target

    def scan(self, options):
        try:
            command = ["nmap", options, self.target]
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print(result.stdout)
            return result.returncode
        except FileNotFoundError:
            print("Error: nmap not found. Please install nmap and try again.\n")
            return 1
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}\n")
            return e.returncode

def get_targets():
    while True:
        targets = input("Input targets (Example: IP or website - 192.168.1.1 or example.com):\n")
        if targets == "0":
            return targets
        if targets.strip():
            return targets
        print("Invalid input. Please enter targets or press 0 to return.\n")

def start_scan(helper, options):
    print("*" * 15 + " Scan starting... wait " + "*" * 15)
    print()
    try:
        exit_code = helper.scan(options)
        print("*" * 15 + f" Scan completed with exit code: {exit_code} " + "*" * 15)
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
    8: {"description": "Version and OS scan", "command": "-sS -sV -O"},
    9: {"description": "Regular scan", "command": ""},
}

def print_operations():
    print("Operations:")
    for key, value in operations.items():
        print(f"{key}) -> {value['description']}")
    print("0) -> QUIT")

def main():
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
            print("Press 0 to return to the main menu, press ctrl + c to close the tool")
            targets = get_targets()

            if targets == "0":
                print("Returning to the main menu...\n")
                break

            try:
                helper = Nmap(targets)
                start_scan(helper, operations[operation]["command"])
            except KeyboardInterrupt:
                print("\nCtrl+C detected. closing nmap tool...\n")
                break
            except Exception as error:
                print(f"Error: {error}\n")
                break

if __name__ == "__main__":
    main()
