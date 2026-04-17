# 📦 auth-bruteforce-poc
Educational Python tool for testing web login mechanisms using wordlists in controlled lab environments.

## 📖 About the Script

This [project](https://github.com/ctrl-sid2099/auth-bruteforce-poc/blob/main/Brute-Force.py) is a Python-based login testing tool (Proof of Concept) designed to demonstrate how authentication mechanisms can be tested using automated requests and wordlists.

It simulates repeated login attempts against a web application by sending HTTP POST requests with different password combinations. The tool is intended for educational purposes and should only be used in controlled environments such as local test servers or security labs.

## ⚙️ How It Works

### 1) Input Configuration

  - The user provides:
  - Target login URL
  - Username
  - Password wordlist

### 2) Wordlist Processing
The script reads passwords file from a path given by the user

### 3) Session Handling
A persistent session is created using:

    requests.Session()

This allows the script to:

  - Maintain cookies
  - Mimic real user behavior

### 4) Sending Login Requests

For each password:

  - A POST request is sent to the login form
  - Form data (username & password) is included

### 5) Header Simulation
A User-Agent header is added to make requests appear like a normal browser and avoid basic filtering.

### 6) Response Analysis

The script determines success by:

  - Checking for redirects (response.history)
  - Ensuring the failure message is not present in the response

### 7) Output
  
  - Displays each attempted password
  - Stops execution when a valid password is found


## 📄 Working Screenshot

### 1) Start The Local Server

        python server.py

<img width="808" height="524" alt="server" src="https://github.com/user-attachments/assets/0f049e7b-c73f-4f5d-ad54-ac5b125029c1" />

### 2) Check default credentials for user admin

<img width="1082" height="615" alt="failed" src="https://github.com/user-attachments/assets/74a6d3c7-86ff-4c7b-a433-5e49dad1f118" />

### 3) Make A Wordlist File

<img width="706" height="433" alt="wordlists" src="https://github.com/user-attachments/assets/ac75ad46-d272-41b2-b1e6-3cd7969d164c" />

### 4) Execute The Brute-Force tool

<img width="636" height="412" alt="successfull" src="https://github.com/user-attachments/assets/a2546f74-accc-483d-ba39-67ee0ebc7907" />


## ⚠️ Disclaimer

These scripts are intended for educational purposes only and were tested in controlled, legal lab environments. The author is not responsible for any misuse or unethical use of this code.

## 👤 Author

ctrl-sid2099
