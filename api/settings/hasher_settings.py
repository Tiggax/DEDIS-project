from django.contrib.auth.hashers import Argon2PasswordHasher

class OptimalArgon2PasswordHasher(Argon2PasswordHasher):
    salt_length = 16
    tag_length = 32
    time_cost = 3
    parallelism =4


PASSWORD_HASHERS = [
    "api.settings.default.OptimalArgon2PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]