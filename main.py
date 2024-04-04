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

def get_targets():
    while True:
        print("\n> Enter targets (Example: IP or website - 192.168.1.1 or example.com), or enter 0 to return:")
        targets = input("  > ").strip()
        if targets == "0":
            return None
        elif targets:
            return targets
        print("Invalid input. Please enter targets or press 0 to return.")

def get_additional_options():
    print("\n> Enter additional options for the scan (leave empty for default):")
    return input("  > ").strip()

def start_scan(helper, options):
    print("*" * 60)
    print("Scan starting... please wait.\n")
    try:
        result, exit_code = helper.scan(options)
        print(result)
        print("*" * 60)
        print(f"Scan completed with exit code: {exit_code}\n")
    except Exception as e:
        print(f"Error: {e}\n")

def main():
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
        10: {"description": "Slow comprehensive scan", "command": """-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" """
        },
    }

    try:
        while True:
            print("\nOperations:")
            for key, value in operations.items():
                print(f"  {key}) -> {value['description']}")
            print("  0) -> QUIT")

            try:
                operation = int(input("\n> Choose operation: "))
                if operation == 0:
                    print("\nExiting the tool. Goodbye!")
                    break
                elif operation not in operations:
                    print("Invalid operation\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            print("\n" + "*" * 60)
            print("Press ctrl + c to close the tool.")
            targets = get_targets()
            if targets is None:
                continue
            additional_options = get_additional_options()

            try:
                helper = Nmap(targets)
                options = operations[operation]["command"] + " " + additional_options
                start_scan(helper, options)
            except Exception as error:
                print(f"Error: {error}\n")
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting the tool. Goodbye!\n")

if __name__ == "__main__":
    main()
