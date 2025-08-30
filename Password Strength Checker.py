import re

def check_password_strength(password):
    # Rules
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None

    # Count errors
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    strength = 5 - sum(errors)

    # Rating
    if strength == 5:
        return "Strong ✅"
    elif strength >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

# Run program
if __name__ == "__main__":
    pwd = input("Enter a password: ")
    print("Password Strength:", check_password_strength(pwd))
