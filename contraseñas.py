import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Introduce la longitud de la contraseña que deseas: "))

generated_password = ""

for _ in range(password_length):
    generated_password += random.choice(characters)

def print_password(password):
    print(f"Tu contraseña generada es: {password}")

print_password(generated_password)
