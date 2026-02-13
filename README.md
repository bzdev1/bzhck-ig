# 🚀 BzHck - Instagram Account Generator

![Version](https://img.shields.io/badge/version-2.0--DEWA%2B-red)
![Platform](https://img.shields.io/badge/platform-Linux%20|%20Termux%20|%20VPS-blue)
![Status](https://img.shields.io/badge/status-Stable--AF-green)

```

╔══════════════════════════════════════════════════════════╗
║    ██████╗ ███████╗██╗  ██╗ ██████╗██╗  ██╗             ║
║    ██╔══██╗██╔════╝██║  ██║██╔════╝██║ ██╔╝             ║
║    ██████╔╝█████╗  ███████║██║     █████╔╝              ║
║    ██╔══██╗██╔══╝  ██╔══██║██║     ██╔═██╗             ║
║    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗             ║
║    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝             ║
║                                                          ║
║   [ INSTAGRAM ACCOUNT GENERATOR ]                       ║
║   ShadowX™ | DEWA+ MODE | Multi-Thread | Proxy Ready    ║
╚══════════════════════════════════════════════════════════╝

```

---

## ⚡ **TENTANG TOOL INI**
**BzHck** adalah tool auto-generator akun Instagram berbasis Python.  
Didesain untuk **kecepatan**, **stabilitas**, dan **anonimitas**.  
Menggunakan teknik request langsung ke endpoint Instagram dengan **CSRF bypass**.

🔹 **Multi-threading** (1-20 thread)  
🔹 **Rotating User-Agent**  
🔹 **Proxy support** (HTTP/HTTPS)  
🔹 **Auto-generate email** via 1secmail API  
🔹 **Random delay** anti rate-limit  
🔹 **Output ke file .txt**  
🔹 **UI ala Linux terminal** + warna  

---

## ⚠️ **DISCLAIMER PENTING - BACA ATAU MATI**
```diff
- [!] TOOL INI HANYA UNTUK TUJUAN PENDIDIKAN DAN RISET KEAMANAN.
- [!] DILARANG KERAS MENGGUNAKAN UNTUK SPAM, PHISHING, ATAU AKTIVITAS ILEGAL LAINNYA.
- [!] INSTAGRAM ADALAH PLATFORM MILIK META. MELANGGAR ToS MEREKA = AKUN KENA BANNED + RESIKO HUKUM.
- [!] PENGGUNA BERTANGGUNG JAWAB PENUH ATAS PENYALAHGUNAAN TOOL INI.
- [!] DEVELOPER TIDAK BERTANGGUNG JAWAB ATAS KERUSAKAN ATAU KERUGIAN APAPUN.
- [!] GUNAKAN DENGAN BIJAK. JANGAN JADI BURUK RUKA.
```

Dengan menggunakan tool ini, Anda dianggap sudah membaca dan menyetujui risiko di atas.

---

📦 INSTALASI

✅ Persyaratan Sistem

· Python 3.8+
· Pip
· Koneksi internet stabil
· (Opsional) Proxy list

📥 Install Dependencies

```bash
pip install requests fake-useragent colorama
```

🐧 Linux / Ubuntu / Debian

```bash
git clone https://github.com/bzdev1/bzhck-ig.git
cd bzhck-ig
python3 bzhck_ig.py
```

📱 Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/bzdev1/bzhck-ig.git
cd bzhck-ig
pip install requests fake-useragent colorama
python bzhck_ig.py
```

🖥️ VPS / Cloud Server

```bash
# SSH ke VPS
apt update && apt upgrade -y
apt install python3 python3-pip git -y
git clone https://github.com/bzdev1/bzhck-ig.git
cd bzhck-ig
pip3 install -r requirements.txt
python3 bzhck_ig.py

# Untuk running di background (screen)
screen -S bzhck
python3 bzhck_ig.py
# Ctrl+A+D untuk detach
```

🪟 Windows (WSL / CMD)

```bash
# WSL (rekomendasi)
wsl --install
# Buka WSL, lalu ikuti langkah Linux

# Atau pake CMD + Python langsung
python bzhck_ig.py
```

---

⚙️ CARPAKAI (CARA PAKAI)

1️⃣ Clone & Run

```bash
git clone https://github.com/bzdev1/bzhck-ig.git
cd bzhck-ig
python bzhck_ig.py
```

2️⃣ Menu Utama

· [1] Start Generator → Mulai generate akun
· [2] Settings → Atur thread, delay, file output
· [3] View Saved Accounts → Lihat akun yang berhasil
· [4] Proxy Manager → Load & manage proxy
· [5] Exit → Keluar

3️⃣ Setup Proxy (Opsional)

Buat file proxies.txt, isi dengan format:

```
http://user:pass@ip:port
http://ip:port
socks5://ip:port
```

Lalu aktifkan di menu Proxy Manager → Load Proxies → ON.

4️⃣ Mulai Generate

Pilih menu 1, enter, dan biarkan bot bekerja.
Hasil akun akan tersimpan di bz_live.txt (default).

---

🧠 TIPS & TRIK

Tips Keterangan
🚀 Thread 5-8 Paling optimal untuk koneksi biasa
⏱️ Delay 3-7 detik Hindari rate limit Instagram
🧦 Pakai Proxy Wajib kalau mau generate massal
📁 Ganti Output File Biar gak tercampur sama hasil lama
🧹 Clear Proxy List Kalau ganti provider proxy
🛑 Ctrl+C Stop generator kapan saja

---

📂 STRUKTUR FILE

```
bzhck-ig/
├── bzhck_ig.py          # Main script
├── proxies.txt          # Daftar proxy (buat manual)
├── bz_live.txt          # Output akun live
├── requirements.txt     # Dependencies
└── README.md           # Dokumentasi
```

---

🔧 FILE REQUIREMENTS.TXT

Biar gampang install, bikin file requirements.txt:

```txt
requests
fake-useragent
colorama
```

Install dengan:

```bash
pip install -r requirements.txt
```

---

🧪 TESTED ON

· ✅ Kali Linux 2024
· ✅ Ubuntu 22.04 LTS
· ✅ Termux (Android 13+)
· ✅ Debian 11 VPS
· ✅ Windows 11 + WSL2

---

🐞 KNOWN ISSUES

· Instagram kadang minta verifikasi email → skip otomatis
· Proxy jelek bikin timeout → ganti proxy
· Kalau kena rate limit, naikin delay

---

🔐 BYPASS CSRF?

Yes. Script otomatis ambil token sebelum register.
Tanpa ini, request langsung ditolak 403.

---

🧑‍💻 CREDITS

```
Author   : Bapak Ku / BzHck
Channel  : [REDACTED]
Telegram : [REDACTED]
```

Dibuat dengan ☕ dan energi gelap.