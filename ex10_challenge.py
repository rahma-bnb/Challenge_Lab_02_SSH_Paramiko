import logging

def mask_password(password):
    if len(password) <= 2:
        return "*" * len(password)
    return password[0] + "*" * (len(password) - 2) + password[-1]

logging.basicConfig(
    filename="brute_scan.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

def log_attempt(host, username, password, outcome):
    masked = mask_password(password)
    logging.info(
        "host=%s user=%s password=%s result=%s",
        host, username, masked, outcome
    )


# Test simple
if __name__ == "__main__":
    log_attempt("192.168.56.101", "msfadmin", "msfadmin", "failure")
    print("Log écrit dans brute_scan.log")
