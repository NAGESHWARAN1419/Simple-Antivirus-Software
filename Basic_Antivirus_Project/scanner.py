import os
import hashlib
import shutil

folder = "test_folder"
quarantine_folder = "quarantine"

with open("signatures.txt", "r") as f:
    malware_hashes = f.read().splitlines()

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        data = f.read()
        sha256.update(data)

    file_hash = sha256.hexdigest()

    if file_hash in malware_hashes:

        print(f"[!] Malware Detected: {file}")

        shutil.move(file_path, quarantine_folder)

        print("[+] File moved to quarantine")

    else:
        print(f"[+] Safe File: {file}")
