# FILE-INTEGRITY-CHECKER

COMPANY: CODTECH IT SOLUTIONS 

NAME: HARIVIKAS M

INTERN ID: CTO4WP220

"DOMIAN: FRONT END DEVELOPHENT 

"DURATION: 4 WEEEKS 

MENTOR: NEELA SANTOSH 



**Description**

This is a simple Python-based file integrity checker that uses SHA-256 hashing to detect changes in monitored files. It allows users to store a file's hash and later check for modifications, ensuring file integrity.

**Features**

Computes SHA-256 hashes for files

Stores file hashes in a JSON log (hash_log.json)

Checks for file modifications by comparing stored hashes

Simple command-line interface

**Prerequisites**

Ensure you have Python 3 installed on your system.

**Installation**

Clone this repository and navigate into the project directory:

git clone https://github.com/your-username/file-integrity-checker.git
cd file-integrity-checker

**Usage**

Run the script with Python:

python3 file_integrity_checker.py

Follow the on-screen prompts:

Enter the file path to monitor.

Choose:

's' to store the file hash.

'c' to check the file's integrity.

**Example**

Storing a file hash:

Enter the file path to monitor: test_file.txt
Enter 's' to store hash or 'c' to check integrity: s
Stored hash for test_file.txt: 55742f8e967ae36dff4e49f66359d4097f904aae0133e4974e04f7b9ded9b92c

Checking file integrity:

Enter the file path to monitor: test_file.txt
Enter 's' to store hash or 'c' to check integrity: c
Integrity Check Passed for test_file.txt

If the file is modified, a warning is displayed:

WARNING: File test_file.txt has been modified!

**File Structure**

file_integrity_checker.py  # Main script
hash_log.json              # Stores file hashes
README.md                  # Documentation
**
License**

This project is licensed under the MIT License.

**Author**
HARIVIKAS M



**OUTPUT**

