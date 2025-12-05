#!/usr/bin/env python3
import os
import subprocess
import sys

VENV_DIR = "fastapi-env"
REQ_FILE = "req.txt"

def run_command(cmd, check=True):
    """Parancs futtatása shell-ben."""
    print(f"Futtatom: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if check and result.returncode != 0:
        print(f"Hiba a parancs futtatásakor: {cmd}")
        sys.exit(1)

def main():
    # 1️⃣ Ellenőrizzük, hogy létezik-e a venv
    if not os.path.isdir(VENV_DIR):
        print(f"{VENV_DIR} nem található, létrehozás...")
        run_command(f"python3 -m venv {VENV_DIR}")

    # 2️⃣ Ellenőrizzük, hogy req.txt létezik-e
    if os.path.isfile(REQ_FILE):
        print(f"{REQ_FILE} megtalálva, telepítés...")
        # pip telepítés a virtuális környezetben
        pip_path = os.path.join(VENV_DIR, "bin", "pip")
        run_command(f"{pip_path} install -r {REQ_FILE}")
    else:
        print(f"{REQ_FILE} nem található, kihagyva a telepítést.")

    # 3️⃣ Aktiválás és uvicorn indítás
    # Pythonból aktiválni a venv-et nem kell, elég a python bin útját használni
    uvicorn_path = os.path.join(VENV_DIR, "bin", "uvicorn")
    if not os.path.isfile(uvicorn_path):
        print("Uvicorn nincs telepítve. Telepítsd a req.txt-ben vagy külön!")
        sys.exit(1)

    print("API indítása uvicorn-nal...")
    run_command(f"{uvicorn_path} main:app --reload")

if __name__ == "__main__":
    main()
