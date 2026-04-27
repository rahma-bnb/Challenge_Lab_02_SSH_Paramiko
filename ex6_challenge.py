import time

def handle_with_backoff(passwords, try_ssh_fn):
    consecutive_errors = 0

    for password in passwords:
        result = try_ssh_fn(password)

        if result["outcome"] == "error":
            print(f"[ERROR] {result.get('message', '')}")
            consecutive_errors += 1
            time.sleep(2)

            if consecutive_errors >= 3:
                print("[!] 3 erreurs consécutives — pause 30s")
                time.sleep(30)
                consecutive_errors = 0
        else:
            consecutive_errors = 0

        yield password, result