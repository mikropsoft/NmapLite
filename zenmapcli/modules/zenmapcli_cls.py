import os

class zenmapcli():

    def __init__(self, target):
        self.target = target

    def intense_scan(self):
        return os.system("nmap -T4 -A -v " + self.target)

    def intense_scan_plus_udp(self):
        return os.system("nmap -sS -sU -T4 -A -v " + self.target)

    def intense_scan_all_tcp_ports(self):
        return os.system("nmap -p 1-65535 -T4 -A -v " + self.target)

    def intense_scan_no_ping(self):
        return os.system("nmap -T4 -A -v -Pn" + self.target)

    def ping_scan(self):
        return os.system("nmap -sn " + self.target)

    def quick_scan(self):
        return os.system("nmap -T4 -F " + self.target)

    def quick_scan_plus(self):
        return os.system("nmap -sV -T4 -O -F --version-light " + self.target)  

    def regular_scan(self):
        return os.system("nmap " + self.target)          

    def version_and_os_scan(self):
        return os.system("nmap -sS -sV -O " + self.target)
