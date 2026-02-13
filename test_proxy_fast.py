#!/usr/bin/env python3
import requests
import threading
from queue import Queue

print("\033[93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
print("\033[92m    PROXY TESTER FAST - BzHck EDITION\033[0m")
print("\033[93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

with open('proxies.txt', 'r') as f:
    proxies = [line.strip() for line in f if line.strip()]

print(f"\033[92m[✓] Total proxy: {len(proxies)}\033[0m")
print("\033[93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

q = Queue()
for p in proxies:
    q.put(p)

live = []
lock = threading.Lock()

def tester():
    while not q.empty():
        proxy = q.get()
        try:
            r = requests.get(
                'https://httpbin.org/ip',
                proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'},
                timeout=5
            )
            if r.status_code == 200:
                with lock:
                    live.append(proxy)
                    print(f"\033[92m[✓] LIVE: {proxy}\033[0m")
        except:
            pass
        finally:
            q.task_done()

threads = []
for _ in range(30):  # 30 thread parallel
    t = threading.Thread(target=tester)
    t.start()
    threads.append(t)

q.join()

with open('live_proxies.txt', 'w') as f:
    for p in live:
        f.write(p + '\n')

print("\033[93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
print(f"\033[92m[✓] Selesai! Proxy hidup: {len(live)} dari {len(proxies)}\033[0m")
print("\033[92m[✓] Disimpan di: live_proxies.txt\033[0m")
print("\033[93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
