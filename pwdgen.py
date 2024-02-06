import random
import string

# The int number sets the length of the password given.
# alphabet cats all the ascii letters, numbers, and symbols to be able to use them all in the generated password
def generate_password(length: int = 15):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

# Calls the password created by the above function.
password = generate_password()
print(f"Password: {password}")
