import subprocess
import os
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from datetime import datetime

class NmapScanner:
    def __init__(self, target, options):
        self.target = target
        self.options = options

    def run(self):
        cmd = ['nmap'] + self.options.split() + [self.target]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except FileNotFoundError:
            return "Error: Nmap is not installed or not found in PATH."

class NmapGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nmap Advanced GUI")
        self.root.geometry("800x600")
        self.output = ""

        self.scan_options = {
            "Intense Scan": "-T4 -A -v",
            "Intense Scan Plus UDP": "-sS -sU -T4 -A -v",
            "All TCP Ports": "-p 1-65535 -T4 -A -v",
            "No Ping": "-T4 -A -v -Pn",
            "Ping Scan": "-sn",
            "Quick Scan": "-T4 -F",
            "Quick Scan Plus": "-sV -T4 -O -F --version-light",
            "Traceroute": "-sn --traceroute",
            "Regular Scan": "",
            "Slow Comprehensive": "-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script discovery,safe",
            "Custom Ports": "-p ",
            "Service Detection": "-sV",
            "OS Detection": "-O",
            "Aggressive Scan": "-A",
            "Firewall Detection": "--script firewall-bypass",
            "Vulnerability Scan": "--script vuln",
            "Malware Scan": "--script malware",
            "Custom NSE Script": "--script ",
            "Heartbleed Check": "--script ssl-heartbleed",
            "Traceroute Geolocation": "--traceroute --script traceroute-geolocation"
        }

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Target IP/Hostname:").grid(row=0, column=0, sticky='w')
        self.target_entry = ttk.Entry(frame)
        self.target_entry.grid(row=0, column=1, columnspan=3, sticky='ew', pady=5)

        ttk.Label(frame, text="Scan Type:").grid(row=1, column=0, sticky='w')
        self.scan_combo = ttk.Combobox(frame, values=list(self.scan_options.keys()), state='readonly')
        self.scan_combo.current(0)
        self.scan_combo.grid(row=1, column=1, sticky='ew', pady=5)

        ttk.Label(frame, text="Additional Options:").grid(row=2, column=0, sticky='w')
        self.options_entry = ttk.Entry(frame)
        self.options_entry.grid(row=2, column=1, columnspan=3, sticky='ew', pady=5)

        self.start_btn = ttk.Button(frame, text="Start Scan", command=self.start_scan_thread)
        self.start_btn.grid(row=3, column=1, sticky='ew', pady=5)

        self.save_btn = ttk.Button(frame, text="Save Output", command=self.save_output)
        self.save_btn.grid(row=3, column=2, sticky='ew', pady=5)

        self.clear_btn = ttk.Button(frame, text="Clear", command=self.clear_output)
        self.clear_btn.grid(row=3, column=3, sticky='ew', pady=5)

        self.output_area = scrolledtext.ScrolledText(frame, wrap='word', state='disabled')
        self.output_area.grid(row=4, column=0, columnspan=4, sticky='nsew', pady=10)

        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)

    def append_output(self, text):
        self.output_area.config(state='normal')
        self.output_area.insert('end', text + '\n')
        self.output_area.config(state='disabled')
        self.output_area.see('end')

    def start_scan_thread(self):
        threading.Thread(target=self.start_scan, daemon=True).start()

    def start_scan(self):
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror("Input Error", "Please enter a target.")
            return

        scan_type = self.scan_combo.get()
        base_options = self.scan_options[scan_type]
        additional_options = self.options_entry.get().strip()
        options = f"{base_options} {additional_options}".strip()

        if base_options.endswith("-p"):
            ports = additional_options
            if not ports:
                messagebox.showerror("Port Error", "Specify ports for this scan type.")
                return
            options = f"{base_options}{ports}"

        self.append_output(f"Starting '{scan_type}' scan on {target}...")
        scanner = NmapScanner(target, options)
        result = scanner.run()
        self.output = result

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.append_output(f"Scan Completed [{timestamp}]:\n{result}")

    def save_output(self):
        if not self.output:
            messagebox.showwarning("Save Error", "No output to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".log",
            filetypes=[("Log files", "*.log"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.output)
            messagebox.showinfo("Saved", f"Output saved to {file_path}")

    def clear_output(self):
        self.output_area.config(state='normal')
        self.output_area.delete('1.0', 'end')
        self.output_area.config(state='disabled')
        self.output = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = NmapGUI(root)
    root.mainloop()
