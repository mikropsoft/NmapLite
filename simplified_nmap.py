from modules.nmap import nmap
from modules.print_colored import PrintStyle
from pyfiglet import Figlet
my_text = Figlet().renderText("SİMPLE NMAP")
print(PrintStyle.CGREEN + my_text + PrintStyle.CGREEN)
print(PrintStyle.CBLUE + 15*"*"+""" BY MDKSEC """ + 15*"*"+PrintStyle.CYELLOW)

while True:
    print(PrintStyle.CITALIC + """

Operations:

1-) Intense scan
2-) Intense scan plus UDP
3-) Intense scan, all TCP ports
4-) Intense scan, no ping
5-) Ping scan
6-) Quick scan
7-) Quick scan plus
8-) Version and os scan
9-) Regular scan
0-) QUIT

""" + PrintStyle.CRED)
    operations = input("Choose operation:")
    print("\n")
    if operations == "1":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.intense_scan()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "2":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.intense_scan_plus_udp()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "3":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.intense_scan_all_tcp_ports()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "4":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.intense_scan_no_ping()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "5":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.ping_scan()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "6":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.quick_scan()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "7":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.quick_scan_plus()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "8":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.version_and_os_scan()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "9":

        while True:
            print(PrintStyle.CBEIGE +
                  "Press 0 for return to main menu , press ctrl + c to close the tool" + PrintStyle.CVIOLET)
            targets = input(PrintStyle.CBLUE + "Input targets " + PrintStyle.CBLUE + PrintStyle.CYELLOW +
                            "(Example: Ip or website (192.168.1.1 or example.com) : " + PrintStyle.CITALIC)
            print("\n")

            if targets == "0":
                break
            else:
                my_object = nmap(targets)
                try:
                    print(
                        PrintStyle.CGREEN + "*" * 15 + " Scan starting ... wait " + "*" * 15 + PrintStyle.CGREEN)
                    print(PrintStyle.CGREEN)

                    my_object.regular_scan()
                    print(PrintStyle.CRED + "*" * 15 +
                          " Scan completed " + "*" * 15 + PrintStyle.CRED)
                    print("\n")
                except:
                    print(PrintStyle.CRED + "Error" + PrintStyle.CRED)

    elif operations == "0":
        break
    else:
        print(PrintStyle.CRED + "Invalid operations" + PrintStyle.CRED)
