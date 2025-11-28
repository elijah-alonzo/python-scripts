import random
import string

def generate_password(length=16, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    all_chars = letters + digits + symbols

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Password length: "))
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    pwd = generate_password(length, symbols)
    print(f"\nGenerated Password:\n{pwd}")
