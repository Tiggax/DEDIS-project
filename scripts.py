import subprocess
import os
from pathlib import Path

def manage(*args):
    proc = subprocess.run(["python3","-m", "poetry", "run", "python3", "manage.py"] + list(args))
    print(proc.stderr)
    print(proc.stdout)
    print(f"Finished: {proc.returncode}")


def dev():
    manage("runserver")

def migrate():
    manage("migrate")
    manage("makemigrations")

def setup_HTMX():
    print("Setting up HTMX")

    htmx = Path("static/htmx.min.js")
    if htmx.exists():
        print("htmx already installed")
        return
    
    static_folder = Path("static")
    if not static_folder.exists():
        os.mkdir(static_folder)

    
    download_file(
        "https://unpkg.com/htmx.org@2.0.3",
        "htmx.min.js",
    )

def download_file(url: str, name: str) -> None:
    print(f"Downloading..\n{name}\n from:\n{url}")
    proc = subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            url,
            "-o",
            f"static/{name}"
        ]
    )
    if proc.returncode != 0:
        raise SystemExit(1)
    
def setup_prod():
    print("Setting up Production")
    print("setting HTMX")
    setup_HTMX()
    print("add static files")
    dir = os.getcwd()
    print(f"Working DIR: {dir}")
    manage("collectstatic")
    print("setting migrations")
    migrate()


def prod():
    print("Starting server...")
    manage("runserver")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
