import paramiko
import socket
import logging

logging.getLogger("paramiko").setLevel(logging.CRITICAL)

def try_ssh_login(host, port, username, password, timeout=3.0):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            timeout=timeout,
            allow_agent=False,
            look_for_keys=False
        )
        return {"outcome": "success"}

    except Exception as e:
        return {"outcome": "failure", "error": str(e)}

    finally:
        client.close()

# Test
if __name__ == "__main__":
    host = input("Host: ").strip()
    port = int(input("Port [22]: ").strip() or "22")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    result = try_ssh_login(host, port, username, password)
    print("Result:", result)