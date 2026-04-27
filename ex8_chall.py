import threading
import queue

def worker(host, port, username, q, stop_event, lock):
    attempts = 0

    while not stop_event.is_set() and attempts < 3:
        try:
            password = q.get_nowait()
        except queue.Empty:
            return
        
        with lock:
            print(f"[{threading.current_thread().name}] Testing password")

        attempts += 1
