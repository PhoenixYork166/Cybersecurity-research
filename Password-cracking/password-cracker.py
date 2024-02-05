import random
import string

# A function to accept 'password' as the argument
def crack_password(password):
    # Initial attempt = 0
    attempts = 0
    while True:
        # Randomly select CHAR
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
        attempts += 1
        if guess == password:
            return attempts
        
password = input("Enter the password to crack: ")

print("Cracking password...")
# Calling the crack_password that returns 'attempts'
attempts = crack_password(password)

print(f'The password was cracked in {attempts} attempts')
        