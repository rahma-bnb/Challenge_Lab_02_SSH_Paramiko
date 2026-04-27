import paramiko
import logging

logging.getLogger("paramiko").setLevel(logging.CRITICAL)

def read_ssh_banner(host, port=22, timeout=3.0):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            port=port,
            username="invalid",
            password="invalid",
            timeout=timeout,
            allow_agent=False,
            look_for_keys=False
        )
    except paramiko.AuthenticationException:
        pass

    banner = None
    transport = client.get_transport()
    if transport:
        banner = transport.remote_version

    client.close()
    return banner


# Test
if __name__ == "__main__":
    host = input("Host: ").strip()
    banner = read_ssh_banner(host)

    if banner:
        print("SSH Banner:", banner)
    else:
        print("No banner received")