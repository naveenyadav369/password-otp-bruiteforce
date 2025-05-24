# password-otp-bruiteforce


import itertools
import string
import sys

def get_charset(choice):
    if choice == '0':  # OTP
        return '0123456789'
    elif choice == '1':  # Password
        return string.ascii_letters + string.digits + string.punctuation
    else:
        return None

def brute_force_crack(secret, charset, length):
    print(f"\nStarting brute-force cracking using charset of size {len(charset)} for length {length}.\n")

    attempt_count = 0
    for guess_tuple in itertools.product(charset, repeat=length):
        guess = ''.join(guess_tuple)
        attempt_count += 1
        print(f"Trying: {guess}", end='\r', flush=True)  # Verbose output on same line

        if guess == secret:
            print(f"\nCracked successfully after {attempt_count} attempts! The value is: {guess}")
            return guess

    print("\nFailed to crack the value.")
    return None

def main():
    print("Welcome to the interactive brute-force cracker!")
    choice = ''
    while choice not in ['0', '1']:
        choice = input("Choose what to crack (enter '0' for OTP or '1' for password): ").strip()
        if choice not in ['0', '1']:
            print("Invalid choice. Please enter '0' for OTP or '1' for password.")

    length = None
    while length is None:
        length_input = input(f"Enter the length of the {'OTP' if choice == '0' else 'password'} to crack (positive integer): ").strip()
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
        else:
            print("Invalid length. Please enter a positive integer.")

    secret = ''
    while len(secret) != length:
        secret = input(f"Enter the secret {'OTP' if choice == '0' else 'password'} of length {length}: ")
        if len(secret) != length:
            print(f"The {'OTP' if choice == '0' else 'password'} must be exactly {length} characters long.")
            continue

        # Validate characters
        valid_chars = get_charset(choice)
        if any(c not in valid_chars for c in secret):
            print(f"The {'OTP' if choice == '0' else 'password'} must only contain valid characters from the charset: {valid_chars}")
            secret = ''

    charset = get_charset(choice)
    brute_force_crack(secret, charset, length)

if __name__ == "__main__":
    main()




    # 🔐 Brute-Force Cracking Tool (Python)

This is a simple **Python-based brute-force cracker** that demonstrates how attackers might attempt to guess a secret **OTP** or **Password** using brute-force techniques.

## 🚀 Features

- 🧠 **Two Cracking Modes**:
  - `0` - OTP (Digits only: `0-9`)
  - `1` - Password (Full charset: letters, digits, special characters)
- 💬 **Interactive Command-Line Interface**
- 👀 **Live Attempt Display** — see each combination being tested
- 🔍 **Input Validation** — ensures secret value matches charset rules
- 📏 **Custom Length Support**

## 🛠️ How It Works

1. User selects what to crack: `OTP` or `Password`.
2. Inputs the length of the secret value.
3. Provides the actual secret to simulate a brute-force cracking scenario.
4. The program generates and tries all combinations using `itertools.product()`.
5. Displays each guess in real time and stops when the secret is cracked.

## 📌 Example Usage

```bash
Welcome to the interactive brute-force cracker!
Choose what to crack (enter '0' for OTP or '1' for password): 0
Enter the length of the OTP to crack (positive integer): 4
Enter the secret OTP of length 4: 1234

Starting brute-force cracking using charset of size 10 for length 4.
Trying: 0000
Trying: 0001
...
Cracked successfully after 1235 attempts! The value is: 1234


USE IN LINUX --------------
# 🔐 Password & OTP Brute-Force Cracker (Python)

This is a simple **Python-based brute-force tool** that demonstrates how attackers may attempt to guess a secret **OTP** or **password** using brute-force techniques.

---

## 🚀 Features

- 🔢 Crack numeric OTPs (0–9)
- 🔐 Crack passwords using full charset (A-Z, a-z, 0-9, symbols)
- 🧪 Live brute-force guessing with real-time feedback
- 📏 Customizable input length
- ✅ Validates user input to match charset
- 📜 Beginner-friendly and educational

---

## 📥 Installation & Usage

### 🔁 Clone the repository

```bash
git clone https://github.com/naveenyadav369/password-otp-bruiteforce.git
cd password-otp-bruiteforce
python password_cracker.py





    

