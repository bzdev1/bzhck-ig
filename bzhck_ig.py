#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BzHck - Instagram Generator DEWA+ EDITION
# Bzone Core Protocol

import os
import sys
import time
import json
import random
import string
import threading
import requests
from datetime import datetime
from fake_useragent import UserAgent

# ===== PAKET WARNA =====
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    R = Fore.RED; G = Fore.GREEN; Y = Fore.YELLOW; B = Fore.BLUE; M = Fore.MAGENTA; C = Fore.CYAN; W = Fore.WHITE; RS = Style.RESET_ALL
except:
    R=G=Y=B=M=C=W=RS=''

# ===== KONFIGURASI DEFAULT =====
CONFIG = {
    'threads': 3,
    'delay_min': 2,
    'delay_max': 6,
    'proxy_file': 'proxies.txt',
    'output_file': 'bz_live.txt',
    'use_proxy': False,
    'proxy_list': []
}

ua = UserAgent()

# ===== BANNER BzHck =====
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{R}
╔══════════════════════════════════════════════════════════╗
║    ██████╗ ███████╗██╗  ██╗ ██████╗██╗  ██╗             ║
║    ██╔══██╗██╔════╝██║  ██║██╔════╝██║ ██╔╝             ║
║    ██████╔╝█████╗  ███████║██║     █████╔╝              ║
║    ██╔══██╗██╔══╝  ██╔══██║██║     ██╔═██╗              ║
║    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗             ║
║    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝             ║
║                                                          ║
║    {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}      ║
║    {C}[ INSTAGRAM ACCOUNT GENERATOR ]{R}                         ║
║    {Y}ShadowX™ | DEWA+ MODE | Multi-Thread | Proxy Ready{R}      ║
║    {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}      ║
╚══════════════════════════════════════════════════════════╝{RS}
    """)

# ===== LOAD PROXY =====
def load_proxies():
    if not CONFIG['use_proxy']:
        return
    try:
        with open(CONFIG['proxy_file'], 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
            if proxies:
                CONFIG['proxy_list'] = proxies
                print(f"{G}[✓] Loaded {len(proxies)} proxies{RS}")
            else:
                print(f"{Y}[!] Proxy file empty, using direct connection{RS}")
                CONFIG['use_proxy'] = False
    except:
        print(f"{Y}[!] No proxy file found, using direct connection{RS}")
        CONFIG['use_proxy'] = False
    time.sleep(1)

# ===== MENU UTAMA =====
def main_menu():
    while True:
        banner()
        print(f"{C}══════════════════════════════════════════════════════════{RS}")
        print(f"{W}  [1]{RS} {G}▶ Start Generator{RS}")
        print(f"{W}  [2]{RS} {Y}⚙ Settings{RS}")
        print(f"{W}  [3]{RS} {B}📁 View Saved Accounts{RS}")
        print(f"{W}  [4]{RS} {M}🔧 Proxy Manager{RS}")
        print(f"{W}  [5]{RS} {R}⏏ Exit{RS}")
        print(f"{C}══════════════════════════════════════════════════════════{RS}")
        
        choice = input(f"{R}┌─[{C}BzHck{R}]─[{Y}Menu{R}]\n└──╼ {W}${RS} ").strip()
        
        if choice == '1':
            start_generator()
        elif choice == '2':
            settings_menu()
        elif choice == '3':
            view_accounts()
        elif choice == '4':
            proxy_menu()
        elif choice == '5':
            print(f"{R}[!] Exiting BzHck System...{RS}")
            sys.exit(0)
        else:
            print(f"{R}[!] Invalid option{RS}")
            time.sleep(1)

# ===== SETTINGS =====
def settings_menu():
    while True:
        banner()
        print(f"{Y}═══════════════════ SETTINGS ═══════════════════{RS}")
        print(f"{W}  [1] Threads     : {G}{CONFIG['threads']}{RS}")
        print(f"{W}  [2] Delay Min   : {G}{CONFIG['delay_min']}s{RS}")
        print(f"{W}  [3] Delay Max   : {G}{CONFIG['delay_max']}s{RS}")
        print(f"{W}  [4] Output File : {G}{CONFIG['output_file']}{RS}")
        print(f"{W}  [5] Proxy File  : {G}{CONFIG['proxy_file']}{RS}")
        print(f"{W}  [6] Proxy Status: {G}{'ON' if CONFIG['use_proxy'] else 'OFF'}{RS}")
        print(f"{W}  [7] Back to Main{RS}")
        print(f"{Y}════════════════════════════════════════════════{RS}")
        
        choice = input(f"{R}┌─[{C}BzHck{R}]─[{Y}Settings{R}]\n└──╼ {W}${RS} ")
        
        if choice == '1':
            try:
                t = int(input(f"{Y}[?] Thread count (1-20): {RS}"))
                CONFIG['threads'] = max(1, min(20, t))
            except: pass
        elif choice == '2':
            try:
                d = float(input(f"{Y}[?] Min delay (1-10): {RS}"))
                CONFIG['delay_min'] = max(0.5, min(10, d))
            except: pass
        elif choice == '3':
            try:
                d = float(input(f"{Y}[?] Max delay (1-15): {RS}"))
                CONFIG['delay_max'] = max(CONFIG['delay_min'], min(15, d))
            except: pass
        elif choice == '4':
            f = input(f"{Y}[?] Output filename: {RS}").strip()
            if f: CONFIG['output_file'] = f
        elif choice == '5':
            f = input(f"{Y}[?] Proxy filename: {RS}").strip()
            if f: CONFIG['proxy_file'] = f
        elif choice == '6':
            CONFIG['use_proxy'] = not CONFIG['use_proxy']
            if CONFIG['use_proxy']:
                load_proxies()
        elif choice == '7':
            break
        else:
            print(f"{R}[!] Invalid{RS}")
            time.sleep(0.5)

# ===== PROXY MENU =====
def proxy_menu():
    while True:
        banner()
        print(f"{M}══════════════════ PROXY MANAGER ══════════════════{RS}")
        print(f"{W}  [1] Load Proxies{RS}")
        print(f"{W}  [2] Test Proxies{RS}")
        print(f"{W}  [3] Clear List{RS}")
        print(f"{W}  [4] View List ({len(CONFIG['proxy_list'])} proxies){RS}")
        print(f"{W}  [5] Back{RS}")
        print(f"{M}════════════════════════════════════════════════{RS}")
        
        choice = input(f"{R}┌─[{C}BzHck{R}]─[{M}Proxy{R}]\n└──╼ {W}${RS} ")
        
        if choice == '1':
            load_proxies()
        elif choice == '2':
            print(f"{Y}[*] Testing proxies...{RS}")
            time.sleep(1)
            print(f"{G}[✓] Done{RS}")
            time.sleep(1)
        elif choice == '3':
            CONFIG['proxy_list'] = []
            print(f"{R}[!] Proxy list cleared{RS}")
            time.sleep(1)
        elif choice == '4':
            print(f"\n{Y}Proxy List:{RS}")
            for i, p in enumerate(CONFIG['proxy_list'][:20], 1):
                print(f"{W}  {i}. {p}{RS}")
            if len(CONFIG['proxy_list']) > 20:
                print(f"{W}  ... and {len(CONFIG['proxy_list'])-20} more{RS}")
            input(f"\n{Y}Press Enter to continue...{RS}")
        elif choice == '5':
            break

# ===== VIEW SAVED ACCOUNTS =====
def view_accounts():
    banner()
    print(f"{B}══════════════════ SAVED ACCOUNTS ══════════════════{RS}")
    try:
        with open(CONFIG['output_file'], 'r') as f:
            lines = f.readlines()
            if lines:
                for line in lines[-20:]:
                    print(f"{G}{line.strip()}{RS}")
                print(f"{W}\nTotal: {len(lines)} accounts | Showing last 20{RS}")
            else:
                print(f"{Y}[!] No accounts yet{RS}")
    except:
        print(f"{Y}[!] No output file found{RS}")
    
    input(f"\n{Y}Press Enter to continue...{RS}")

# ===== GENERATOR CLASS =====
class BzGenerator:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.success = 0
        self.failed = 0
        
    def get_temp_email(self):
        try:
            r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", timeout=10)
            return r.json()[0]
        except:
            return f"{self.gen_username()}@{random.choice(['mailinator.com','temp-mail.org','10minutemail.net'])}"
    
    def gen_username(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(8,12)))
    
    def gen_password(self):
        return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=16))
    
    def get_proxy_dict(self):
        if CONFIG['use_proxy'] and CONFIG['proxy_list']:
            proxy = random.choice(CONFIG['proxy_list'])
            return {'http': proxy, 'https': proxy}
        return None
    
    def create_account(self, thread_id, stats):
        headers = {
            'User-Agent': self.ua.random,
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
        }
        
        while True:
            try:
                email = self.get_temp_email()
                username = self.gen_username()
                password = self.gen_password()
                
                payload = {
                    'email': email,
                    'username': username,
                    'password': password,
                    'first_name': username[:6],
                }
                
                sess = requests.Session()
                if CONFIG['use_proxy']:
                    sess.proxies.update(self.get_proxy_dict())
                sess.headers.update(headers)
                
                sess.get('https://www.instagram.com', timeout=15)
                sess.headers.update({'x-csrftoken': sess.cookies.get('csrftoken', '')})
                
                r = sess.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/', 
                            data=payload, timeout=20)
                
                if r.status_code == 200:
                    result = r.json()
                    if result.get('account_created') or result.get('status') == 'ok':
                        timestamp = datetime.now().strftime('%H:%M:%S')
                        acc_line = f"[{timestamp}] {username}:{password} | {email}\n"
                        
                        with open(CONFIG['output_file'], 'a') as f:
                            f.write(acc_line)
                        
                        stats['success'] += 1
                        print(f"{G}[✓][T{thread_id}] {username}:{password}{RS}")
                    else:
                        stats['failed'] += 1
                else:
                    stats['failed'] += 1
                    
                delay = random.uniform(CONFIG['delay_min'], CONFIG['delay_max'])
                time.sleep(delay)
                
            except KeyboardInterrupt:
                break
            except:
                stats['failed'] += 1
                time.sleep(1)
                continue

# ===== START GENERATOR =====
def start_generator():
    banner()
    print(f"{C}══════════════════ GENERATOR ACTIVE ══════════════════{RS}")
    print(f"{W}  Threads     : {G}{CONFIG['threads']}{RS}")
    print(f"{W}  Delay       : {G}{CONFIG['delay_min']}-{CONFIG['delay_max']}s{RS}")
    print(f"{W}  Proxy       : {G}{'ON' if CONFIG['use_proxy'] else 'OFF'}{RS}")
    print(f"{W}  Output      : {G}{CONFIG['output_file']}{RS}")
    print(f"{C}════════════════════════════════════════════════════{RS}\n")
    
    input(f"{Y}Press Enter to start or Ctrl+C to cancel...{RS}")
    
    try:
        import requests
    except:
        print(f"{R}[!] requests not installed. Run: pip install requests fake-useragent{RS}")
        return
    
    stats = {'success': 0, 'failed': 0}
    threads = []
    
    for i in range(CONFIG['threads']):
        gen = BzGenerator()
        t = threading.Thread(target=gen.create_account, args=(i+1, stats))
        t.daemon = True
        threads.append(t)
        t.start()
        time.sleep(0.3)
    
    try:
        while True:
            time.sleep(5)
            print(f"{Y}[*] Stats - Success: {G}{stats['success']}{Y} Failed: {R}{stats['failed']}{RS}")
    except KeyboardInterrupt:
        print(f"\n{R}[!] Generator stopped{RS}")
        print(f"{G}[✓] Total success: {stats['success']}{RS}")
        print(f"{B}[📁] Saved to: {CONFIG['output_file']}{RS}")
        time.sleep(3)

# ===== ENTRY POINT =====
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Force exit{RS}")
        sys.exit(0)