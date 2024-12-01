import subprocess
import os
from pathlib import Path

def manage(*args):
    subprocess.run(["python", "manage.py"] + list(args))


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