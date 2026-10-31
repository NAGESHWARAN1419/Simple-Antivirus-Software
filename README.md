# Simple Antivirus Software | Python

A beginner-friendly, signature-based antivirus simulator developed using Python. This project demonstrates how antivirus software can identify potentially malicious files using SHA-256 hashing and a database of known malware signatures.

## About the Project

This project was developed to understand the basic working principles of antivirus software and malware detection.

The scanner examines files inside a specified folder, calculates their SHA-256 hash values, and compares those hashes against known malware signatures stored in a signature database.

If a file's hash matches a known signature, the scanner identifies it as potentially malicious and moves it into a quarantine folder.

## Features

- **File Scanning:** Scans files inside a specified test folder.
- **SHA-256 Hashing:** Generates SHA-256 hashes for scanned files.
- **Signature-Based Detection:** Compares file hashes against known malware signatures.
- **Malware Detection:** Identifies files whose hashes match the signature database.
- **Quarantine System:** Moves detected files into a quarantine folder.
- **Safe File Identification:** Identifies files that do not match the stored signatures.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| os | File and directory operations |
| hashlib | SHA-256 hash generation |
| shutil | Moving detected files into quarantine |

## Project Structure

```text
Simple-Antivirus-Software/
│
├── scanner.py
├── signatures.txt
├── test_folder/
│   └── safe.txt
│
├── quarantine/
│
└── README.md
```

## How It Works

The antivirus scanner follows these steps:

1. Reads known malware hashes from `signatures.txt`.
2. Opens files inside the test folder.
3. Calculates the SHA-256 hash of each file.
4. Compares the calculated hash with the stored signatures.
5. If a match is found, identifies the file as potentially malicious.
6. Moves the detected file into the quarantine folder.
7. If no match is found, identifies the file as having no matching signature.

### Detection Workflow

```text
        Start Scanner
              |
              v
      Read Malware Signatures
              |
              v
       Scan Test Folder
              |
              v
       Calculate SHA-256
              |
              v
      Compare With Database
              |
         +----+----+
         |         |
       Match     No Match
         |         |
         v         v
    Malware     Safe from
    Detected    Known Signatures
         |
         v
     Quarantine
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/NAGESHWARAN1419/Simple-Antivirus-Software.git
```

### 2. Navigate to the Project Folder

```bash
cd Simple-Antivirus-Software
```

If the project files are inside the `Basic_Antivirus_Project` directory, navigate into it:

```bash
cd Basic_Antivirus_Project
```

### 3. Run the Scanner

```bash
python3 scanner.py
```

## Sample Output

Example of the expected scanner output:

```text
[+] Safe File: safe.txt
[!] Malware Detected: malware.txt
[+] File moved to quarantine
```

*Actual output depends on the files present in the test folder and the signatures stored in the database.*

## Learning Outcomes

Through this project, I gained practical experience with:

- Understanding signature-based malware detection.
- Generating SHA-256 file hashes using Python.
- Comparing file hashes against a signature database.
- Performing file and directory operations.
- Understanding the purpose of antivirus quarantine systems.
- Applying Python automation to basic cybersecurity tasks.

## Limitations

- Uses signature-based detection only.
- Detects only files matching hashes in the signature database.
- Cannot identify unknown malware or zero-day threats.
- Scans only the configured test folder.
- Does not provide real-time protection.
- This is an educational simulation, not a replacement for commercial antivirus software.

## Disclaimer

This project was developed for educational purposes and cybersecurity learning in a controlled lab environment.

It is not intended to replace professional antivirus or endpoint protection software.

## Author

**Nageshwaran N**
