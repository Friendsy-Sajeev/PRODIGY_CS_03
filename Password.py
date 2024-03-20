import re

def assess_password_strength(password):
    # Check length
    length_score = min(2, len(password) // 8)  # Assigns a score between 0 and 2 based on length

    # Check uppercase and lowercase letters
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    letter_score = 2 if has_uppercase and has_lowercase else 0

    # Check numbers
    has_numbers = any(char.isdigit() for char in password)
    number_score = 2 if has_numbers else 0

    # Check special characters
    has_special_chars = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    special_char_score = 2 if has_special_chars else 0

    # Calculate total score
    total_score = length_score + letter_score + number_score + special_char_score

    # Provide feedback based on the total score
    if total_score >= 7:
        return "Strong password"
    elif total_score >= 4:
        return "Moderate password"
    else:
        return "Weak password"

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
