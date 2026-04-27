# ssh_probe.py
import paramiko
import logging

# Silence paramiko's noisy internal messages
logging.getLogger("paramiko").setLevel(logging.CRITICAL)

def try_login(host, port, username, password, timeout=3.0):
    client = paramiko.SSHClient()
    # Auto-accept the server's host key (fine for a local lab VM)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            host, port=port, username=username, password=password,
            timeout=timeout,
            allow_agent=False,   # Don't use your own SSH keys
            look_for_keys=False  # Only try the password we provide
        )
        return "success"
    except paramiko.AuthenticationException:
        return "failure"   # Wrong password — keep going
    except Exception as e:
        return f"error: {e}"   # Network problem — something went wrong
    finally:
        client.close()   # Always close the connection

host     = input("Host: ").strip()
port     = int(input("Port [22]: ").strip() or "22")
username = input("Username: ").strip()
password = input("Password: ").strip()

result = try_login(host, port, username, password)
print(f"Result: {result}")