import os

def hello_world():
    name = os.getenv("USER_NAME", "default_user")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    hello_world()
