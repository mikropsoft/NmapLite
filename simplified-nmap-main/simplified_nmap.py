from modules.nmap import nmap

while True:
    print("""
    Operations:
    1-) Intense scan
    2-) Intense scan plus UDP
    3-) Intense scan, all TCP ports
    4-) Intense scan, no ping
    5-) Ping scan
    6-) Quick scan
    7-) Quick scan plus
    8-) Version and OS scan
    9-) Regular scan
    0-) QUIT
    """)

    operations = input("Choose operation:")

    print("\n")

    if operations == "1":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.intense_scan()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "2":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.intense_scan_plus_udp()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "3":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.intense_scan_all_tcp_ports()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "4":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.intense_scan_no_ping()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "5":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.ping_scan()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "6":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.quick_scan()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "7":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.quick_scan_plus()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "8":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.version_and_os_scan()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "9":
        while True:
            try:
                print("Press 0 to return to the main menu, press ctrl + c to close the tool")
                targets = input("Input targets (Example: Ip or website (192.168.1.1 or example.com): \n")
                print("\n")

                if targets == "0":
                    break 
                else:
                    my_object = nmap(targets)
                    print("*" * 15 + " Scan starting ... wait " + "*" * 15)
                    print()
                    my_object.regular_scan()
                    print("*" * 15 + " Scan completed " + "*" * 15)
                    print("\n")
            except KeyboardInterrupt:
                print("\nCtrl+C detected. Returning to the main menu...\n")
                break  
            except Exception as e:
                print(f"Error: {e}\n")

    elif operations == "0":
        print("Exiting the tool. Goodbye!")
        break
    else:
        print("Invalid operation\n")
     