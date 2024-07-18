import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r'\d', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Password strength levels
    strength_criteria = [
        length_criteria,
        digit_criteria,
        uppercase_criteria,
        lowercase_criteria,
        special_char_criteria
    ]
    strength_score = sum(strength_criteria)

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

    # Determine password strength
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")
