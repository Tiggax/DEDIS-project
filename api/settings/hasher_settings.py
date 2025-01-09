from django.contrib.auth.hashers import Argon2PasswordHasher

class OptimalArgon2PasswordHasher(Argon2PasswordHasher):
    time_cost = 1
    parallelism = 1
    memory_cost = 47104


