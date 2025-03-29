import hashlib
import os
import json

def calculate_hash(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def store_hash(file_path, hash_log):
    file_hash = calculate_hash(file_path)
    if file_hash is None:
        return
    
    hash_log[file_path] = file_hash
    with open("hash_log.json", "w") as log_file:
        json.dump(hash_log, log_file, indent=4)
    print(f"Stored hash for {file_path}: {file_hash}")

def check_integrity(file_path, hash_log):
    if file_path not in hash_log:
        print(f"No previous hash stored for {file_path}.")
        return
    
    current_hash = calculate_hash(file_path)
    if current_hash is None:
        return
    
    if hash_log[file_path] == current_hash:
        print(f"Integrity Check Passed for {file_path}")
    else:
        print(f"WARNING: File {file_path} has been modified!")

if __name__ == "__main__":
    hash_log = {}
    if os.path.exists("hash_log.json"):
        with open("hash_log.json", "r") as log_file:
            hash_log = json.load(log_file)
    
    file_to_monitor = input("Enter the file path to monitor: ")
    choice = input("Enter 's' to store hash or 'c' to check integrity: ")
    
    if choice == 's':
        store_hash(file_to_monitor, hash_log)
    elif choice == 'c':
        check_integrity(file_to_monitor, hash_log)
    else:
        print("Invalid choice.")

