import re

def assess_password_strength(password):
    strength = 0

    # Check password length
    if len(password) >= 12:
        strength += 1
    elif len(password) >= 8:
        strength += 0.5

    # Check for complexity
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[@#$%^&+=]', password):
        strength += 1

    # Check for uniqueness (doesn't appear in a list of common passwords)
    common_passwords = {"password", "123456", "123456789", "qwerty", "abc123"}
    if password.lower() not in common_passwords:
        strength += 1

    # Generate feedback
    if strength <= 1:
        feedback = "Very Weak"
    elif strength <= 2:
        feedback = "Weak"
    elif strength <= 3:
        feedback = "Moderate"
    elif strength <= 4:
        feedback = "Strong"
    else:
        feedback = "Very Strong"

    return feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    print(f"Password strength: {assess_password_strength(password)}")
