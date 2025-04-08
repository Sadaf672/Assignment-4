import random
import string

def password_generate(name: str, digit: int) -> str:
    if len(name) < 3:
        return "Error: Name must be at least 3 characters long."
    if digit <= 0:
        return "Error: Password length must be greater than 0."

    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = []

    name_part = name[:3] if len(name) >= 3 else name
    password.append(name_part)

    for _ in range(digit):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    return "".join(password)

name = input("Enter Your Name: ").strip()
digit = int(input("Enter the number of characters for your password: "))
print(password_generate(name, digit))