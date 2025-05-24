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

