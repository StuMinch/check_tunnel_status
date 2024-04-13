import time
from subprocess import call

def check_tunnel(max_attempts=10):
    for attempt in range(1, max_attempts + 1):
        exit_code = call(["python3", "tunnel_check.py"])
        if exit_code == 1:
            # Retry after 5 seconds
            time.sleep(5)
        else:
            print(f"Tunnel check successful on attempt {attempt}.")
            return True

def chrome_test():
    call(["python3", "test_chrome_latest.py"])

if check_tunnel():
    chrome_test()
else:
    print("Skipping chrome_test() due to tunnel check failures.")
