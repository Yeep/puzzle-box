import random
import string

with open('web/secrets/password', "wt") as f:
    f.write(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(20)))