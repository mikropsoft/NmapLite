import os

class Nmap():
    def __init__(self, target):
        self.target = target

    def scan(self, options):
        return os.system(f"nmap {options} {self.target}")

def get_targets():
    return input("Input targets (Example: IP or website (192.168.1.1 or example.com): \n")

def start_scan(helper, options):
    print("*" * 15 + " Scan starting... wait " + "*" * 15)
    print()
    helper.scan(options)
    print("*" * 15 + " Scan completed! " + "*" * 15)
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

while True:
    print("Operations:")
    for key, value in operations.items():
        print(f"{key}) -> {value['description']}")
    print("0) -> QUIT")

    operation = int(input("Choose operation: "))

    if operation in operations:
        while True:
            print("Press 0 to return to the main menu, press ctrl + c to close the tool")
            targets = get_targets()

            if targets == "0":
                break
            try:
                helper = Nmap(targets)
                start_scan(helper, operations[operation]["command"])
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as error:
                print(f"Error: {error}\n")
    elif operation == 0:
        print("Exiting the tool. Goodbye!")
        break
    else:
        print("Invalid operation\n")