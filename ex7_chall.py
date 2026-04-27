import random
import time

def sleep_with_jitter(min_s, max_s):
    delay = random.uniform(min_s, max_s)
    time.sleep(delay)
    
if __name__ == "__main__":
    print("Sleeping with jitter...")
    sleep_with_jitter(1, 2)
    print("Done")