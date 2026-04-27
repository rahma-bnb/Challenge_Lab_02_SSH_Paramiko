import time
import ipaddress

def is_allowed_host(host):
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_loopback:
            return True
        if ip in ipaddress.ip_network("192.168.56.0/24"):
            return True
        return False
    except ValueError:
        return False


def brute_sequential(host, try_ssh_fn, passwords):
    if not is_allowed_host(host):
        raise ValueError("Host non autorisé (lab uniquement)")

    passwords = passwords[:10]  # maximum 10 essais

    for password in passwords:
        result = try_ssh_fn(password)
        print(f"Trying: {password} → {result}")
        time.sleep(1)