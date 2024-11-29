import subprocess

def manage(*args):
    subprocess.run(["python", "manage.py"] + list(args))


def dev():
    manage("runserver")

def migrate():
    manage("migrate")
    manage("makemigrations")