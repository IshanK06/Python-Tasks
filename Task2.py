import random
import string

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters 
    
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Welcome to the Password Generator ===")
    
    try:
        length = int(input("Enter the desired length of the password (e.g., 12): "))
        
        if length <= 0:
            print("Please enter a positive number greater than 0.")
            return
            
        print("\nLet's set the complexity:")
        inc_numbers = input("Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
        inc_symbols = input("Include symbols (!@#$, etc.)? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, inc_numbers, inc_symbols)
        
        print("\n---------------------------------------")
        print(f"Your Generated Password: {password}")
        print("---------------------------------------")
        
    except ValueError:
        print("Invalid input! Please enter a valid whole number for the length.")

if __name__ == "__main__":
    main()