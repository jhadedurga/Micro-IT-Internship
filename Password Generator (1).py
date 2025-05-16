import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    """
    Generates a secure password that includes at least one uppercase, one lowercase, 
    and optionally one digit and one special character if selected.

    Args:
        length (int): The desired length of the password.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """

    if length < (2 + include_digits + include_special_chars):
        return "Error: Password length too short for selected options."

    # Mandatory character groups
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits) if include_digits else ''
    special = random.choice(string.punctuation) if include_special_chars else ''

    # Remaining characters
    characters = string.ascii_lowercase + string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    remaining_length = length - len(lowercase + uppercase + digit + special)
    remaining_chars = [random.choice(characters) for _ in range(remaining_length)]

    # Combine and shuffle to avoid predictable patterns
    password_list = list(lowercase + uppercase + digit + special) + remaining_chars
    random.shuffle(password_list)
    return ''.join(password_list)

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    new_password = generate_password(password_length, use_digits, use_special_chars)
    print("Generated Password:", new_password)# password-generator