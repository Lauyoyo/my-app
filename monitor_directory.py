import os
import time

def monitor_directory(directory):
    """
    Monitor folder changes
    :param directory: target directory
    """
    if not os.path.exists(directory):
        print(f"directory '{directory}' does not exist。")
        return

    print(f"Start monitoring directory: {directory}")
    before = set(os.listdir(directory))

    while True:
        time.sleep(5)  # Check every 5 seconds
        after = set(os.listdir(directory))
        added = after - before  # New file
        if added:
            print(f"New file: {added}")
        before = after

if __name__ == "__main__":
    # Setting a monitoring Directory
    target_directory = "/Users/Lauyoyo/my-app/public"  

    # Start monitoring
    monitor_directory(target_directory)