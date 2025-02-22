import os
import time

def monitor_directory(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    print(f"Start monitoring directory: {directory}")
    before = set(os.listdir(directory))
    timeout = int(os.getenv("MONITOR_TIMEOUT", "30"))  # 监控超时时间（秒）

    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(5)
        after = set(os.listdir(directory))
        added = after - before
        if added:
            print(f"New file: {added}")
        before = after

    print(f"Monitoring ended after {timeout} seconds.")

if __name__ == "__main__":
    target_directory = os.getenv("TARGET_DIRECTORY", "./public")
    monitor_directory(target_directory)
