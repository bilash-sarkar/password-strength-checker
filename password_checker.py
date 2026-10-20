"""
Password Strength Checker
A simple beginner-friendly cybersecurity project.

It checks a password against basic rules and tells you how strong it is.
Your password is never saved or sent anywhere.
"""

import getpass
import string

# A tiny list of very common (very weak) passwords.
COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "111111", "123456789", "iloveyou", "admin", "welcome",
    "letmein", "monkey", "dragon", "football", "password1",
}


def check_password(password):
    """Return (score, label, tips) for the given password.

    score  -> number from 0 to 6
    label  -> Weak / Medium / Strong
    tips   -> list of suggestions to improve the password
    """
    score = 0
    tips = []

    # Rule 1: length
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        tips.append("12 or more characters is even better.")

    # Rule 2: character variety
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add lowercase letters (a-z).")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add uppercase letters (A-Z).")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add numbers (0-9).")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add special characters like ! @ # $ %.")

    # Rule 3: common passwords are always weak
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips.insert(0, "This is a very common password. Never use it!")

    # Convert the score into a label
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    return score, label, tips


def main():
    print("=== Password Strength Checker ===")
    print("(Your typing will be hidden for safety.)\n")

    password = getpass.getpass("Enter a password to check: ")

    if not password:
        print("You did not type anything. Please run the program again.")
        return

    score, label, tips = check_password(password)

    print(f"\nScore    : {score}/6")
    print(f"Strength : {label}")

    if tips:
        print("\nHow to improve:")
        for tip in tips:
            print(f"  - {tip}")
    else:
        print("\nGreat job! This looks like a strong password.")


if __name__ == "__main__":
    main()
