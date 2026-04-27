import time

def print_summary(stats):
    duration = stats["end"] - stats["start"]
    rate = stats["attempts"] / duration if duration > 0 else 0

    print("===== Scan Summary =====")
    print(f"Host: {stats['host']}")
    print(f"Attempts: {stats['attempts']}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Average attempts/s: {rate:.2f}")
    print(f"Result: {'SUCCESS' if stats['success'] else 'FAILURE'}")

    if stats.get("banner"):
        print(f"SSH Banner: {stats['banner']}")

    print("\nSafeguards applied:")
    print("- Local IPs only")
    print("- Maximum attempt limit")
    print("- Delays / jitter between attempts")


# Test
if __name__ == "__main__":
    stats = {
        "host": "192.168.56.101",
        "attempts": 8,
        "start": time.time(),
        "end": time.time() + 4,
        "success": False,
        "banner": "SSH-2.0-OpenSSH_4.7p1"
    }

    print_summary(stats)