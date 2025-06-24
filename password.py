import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all sets
    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result to remove predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage:
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
