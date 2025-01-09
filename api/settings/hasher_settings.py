from django.contrib.auth.hashers import Argon2PasswordHasher

class OptimalArgon2PasswordHasher(Argon2PasswordHasher):
    time_cost = 1
    parallelism = 1
    memory_cost = 47104


PASSWORD_HASHERS = [
    "api.settings.hasher_settings.OptimalArgon2PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]