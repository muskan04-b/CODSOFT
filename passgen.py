import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):


  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_numbers:
    characters += string.digits
  if include_special_chars:
    characters += string.punctuation

  if not characters:
    print("Error: At least one character type must be selected.")
    return None

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def main():
  """Main function to run the password generator."""

  length = int(input("Enter the desired password length: "))

  include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
  include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
  include_numbers = input("Include numbers? (y/n): ").lower() == "y"
  include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

  password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

  if password:
    print("Generated password:", password)

if __name__ == "__main__":
  main()