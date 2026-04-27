def load_wordlist(path, max_entries=10):
    passwords = []
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            passwords.append(line)
            if len(passwords) >= max_entries:
                break
    return passwords


# Test
if __name__ == "__main__":
    wl = load_wordlist("wordlist.txt")
    print(f"Loaded {len(wl)} passwords:")
    for p in wl:
        print("-", p)
