import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Generate a random password with specified length and character types."""
    # Base character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all selected character sets
    all_characters = lowercase + uppercase + numbers + symbols

    # Ensure at least one character type is selected
    if len(all_characters) == 0:
        raise ValueError("At least one character type must be selected.")

    # Generate password by randomly picking characters from the selected set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Builder!")

    # User input for password specifications
    try:
        length_input = input("Enter the desired password length (default is 12): ").strip()
        length = int(length_input) if length_input else 12
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'

    try:
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
