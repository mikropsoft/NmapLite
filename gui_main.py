import subprocess
import time
import os
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

class Nmap:
    def __init__(self, target):
        self.target = target

    def scan(self, options, output_file):
        try:
            command = ["nmap"] + options.split() + [self.target]
            with open(output_file, "w") as f:
                result = subprocess.run(command, stdout=f, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                with open(output_file, "r") as f:
                    output = f.read()
                return output, result.returncode
            else:
                return f"Error: {result.stderr}\n", result.returncode
        except FileNotFoundError:
            return "Error: nmap not found. Please install nmap and try again.\n", 1

class NmapGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nmap GUI")
        self.root.geometry("700x500")

        self.operations = {
            1: {"description": "Intense Scan", "command": "-T4 -A -v"},
            2: {"description": "Intense Scan Plus UDP", "command": "-sS -sU -T4 -A -v"},
            3: {"description": "Intense Scan, All TCP Ports", "command": "-p 1-65535 -T4 -A -v"},
            4: {"description": "Intense Scan, No Ping", "command": "-T4 -A -v -Pn"},
            5: {"description": "Ping Scan", "command": "-sn"},
            6: {"description": "Quick Scan", "command": "-T4 -F"},
            7: {"description": "Quick Scan Plus", "command": "-sV -T4 -O -F --version-light"},
            8: {"description": "Quick Traceroute", "command": "-sn --traceroute"},
            9: {"description": "Regular Scan", "command": ""},
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
            20: {"description": "Traceroute and Geolocation", "command": "--traceroute --script traceroute-geolocation"},
        }

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}

        self.target_label = tk.Label(self.root, text="Target:")
        self.target_label.grid(row=0, column=0, **padding, sticky="e")

        self.target_entry = tk.Entry(self.root)
        self.target_entry.grid(row=0, column=1, columnspan=3, **padding, sticky="ew")

        self.options_label = tk.Label(self.root, text="Options:")
        self.options_label.grid(row=1, column=0, **padding, sticky="e")

        self.options_entry = tk.Entry(self.root)
        self.options_entry.grid(row=1, column=1, columnspan=3, **padding, sticky="ew")

        self.operation_label = tk.Label(self.root, text="Operation:")
        self.operation_label.grid(row=2, column=0, **padding, sticky="e")

        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set(list(self.operations.values())[0]["description"])

        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, *[op["description"] for op in self.operations.values()])
        self.operation_menu.grid(row=2, column=1, **padding, sticky="ew")

        self.scan_button = tk.Button(self.root, text="Start Scan", command=self.start_scan, bg="lightgreen")
        self.scan_button.grid(row=2, column=2, **padding, sticky="ew")

        self.save_button = tk.Button(self.root, text="Save Output", command=self.save_output, bg="lightblue")
        self.save_button.grid(row=2, column=3, **padding, sticky="ew")

        self.output_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.output_text.grid(row=3, column=0, columnspan=4, **padding, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=0)
        for i in range(1, 4):
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

    def start_scan(self):
        target = self.target_entry.get()
        if not target:
            messagebox.showerror("Input Error", "Please enter a target.")
            return
        
        additional_options = self.options_entry.get()
        selected_operation = self.operation_var.get()

        operation_command = next(op["command"] for op in self.operations.values() if op["description"] == selected_operation)
        options = f"{operation_command} {additional_options}".strip()
        output_file = f"nmap_scan_{int(time.time())}.log"

        self.output_text.insert(tk.END, "Scan starting... please wait.\n")

        try:
            helper = Nmap(target)
            result, exit_code = helper.scan(options, output_file)
            self.output_text.insert(tk.END, result + "\n")
            self.output_text.insert(tk.END, f"Scan completed with exit code: {exit_code}\n")
            self.output_file = output_file
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")

    def save_output(self):
        if hasattr(self, "output_file") and os.path.exists(self.output_file):
            save_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log"), ("All files", "*.*")])
            if save_path:
                os.rename(self.output_file, save_path)
                messagebox.showinfo("Save Output", f"Output saved to {save_path}")
        else:
            messagebox.showwarning("Save Output", "No scan output available to save.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NmapGUI(root)
    root.mainloop()
