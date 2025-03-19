import random

def generate_otp() -> str:
    return "{:06d}".format(random.randint(0, 999999))
