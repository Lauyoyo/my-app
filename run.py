import os
import subprocess

def run_script(script_name):
    print(f"=== Start running {script_name} ===")
    result = subprocess.run(["python", f"src/{script_name}"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error:{result.stderr}")
    print(f"=== End running {script_name} ===\n")

if __name__ == "__main__":
    print("==== Start running My APP ===")

    run_script("hello_world.py")
    run_script("calculator.py")
    run_script("guess_number.py")
    run_script("monitor_directory.py")

    print("=== End running ===")
