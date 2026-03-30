import random
import string

def generate_password(length, use_numbers, use_symbols):
    # Start with a base of uppercase and lowercase letters
    characters = string.ascii_letters 
    
    # Add numbers and symbols based on user preference for complexity
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    # Generate the password by randomly choosing characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Welcome to the Password Generator ===")
    
    # 1. User Input
    try:
        length = int(input("Enter the desired length of the password (e.g., 12): "))
        
        if length <= 0:
            print("Please enter a positive number greater than 0.")
            return
            
        print("\nLet's set the complexity:")
        inc_numbers = input("Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
        inc_symbols = input("Include symbols (!@#$, etc.)? (y/n): ").strip().lower() == 'y'
        
        # 2. Generate Password
        password = generate_password(length, inc_numbers, inc_symbols)
        
        # 3. Display the Password
        print("\n---------------------------------------")
        print(f"Your Generated Password: {password}")
        print("---------------------------------------")
        
    except ValueError:
        print("Invalid input! Please enter a valid whole number for the length.")

if __name__ == "__main__":
    main()