import random
import string
import secrets


def generate_random_character(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_secure_password(length=12):
    if length < 8:
        raise ValueError("Password must be eight characters or longer.")

    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    specials = "!@#$%^&*"  
    non_alphanumerics = specials + string.punctuation

    password = [
        secrets.choice(lowers),
        secrets.choice(uppers),
        secrets.choice(digits),
        secrets.choice(specials),
    ]

    if length > len(password):
        all_chars = lowers + uppers + digits + non_alphanumerics
        password += [secrets.choice(all_chars) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)
