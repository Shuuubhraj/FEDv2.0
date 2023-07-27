import time
import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# ASCII art for the pre-load screen
banner_art = '''
███████╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗
█████╗  █████╗  ██║  ██║
██╔══╝  ██╔══╝  ██║  ██║
██║     ███████╗██████╔╝
╚═╝     ╚══════╝╚═════╝   v2.0   
                            
By : Rajput Shubhraj Singh
FED: File Encryption Decryption [ using CBC mode] (AES)
'''

# Print the ASCII art to create the pre-load screen
print(banner_art)

def choose_file(file_category):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def choose_encrypted_file(file_category):
    root = tk.Tk()
    root.withdraw()
    time_left = 5
    while time_left > 0:
        print(f"Select a file to decrypt in ({time_left} seconds left)...", end='\r')
        time.sleep(1)
        time_left -= 1
    print("\nSelect the encrypted", file_category, "to decrypt.")
    file_path = filedialog.askopenfilename()
    return file_path

def choose_save_location(file_category, is_encrypted=True):
    root = tk.Tk()
    root.withdraw()
    if is_encrypted:
        time_left = 5
        while time_left > 0:
            print(f"Select a location to save the encrypted {file_category} in ({time_left} seconds left)...", end='\r')
            time.sleep(1)
            time_left -= 1
    else:
        time_left = 4
        while time_left > 0:
            print(f"Select a location to save the decrypted {file_category} in ({time_left} seconds left)...", end='\r')
            time.sleep(1)
            time_left -= 1
    print("\nSelect a location to save the", file_category, "in (0 seconds left)...")

    default_file_name = "encrypted_" if is_encrypted else "decrypted_"
    file_extension = os.path.splitext(os.path.basename(file_category))[-1]
    file_path = filedialog.asksaveasfilename(initialfile=default_file_name + os.path.basename(file_category))
    return file_path

def is_valid_file(file_path, file_type):
    valid_extensions = {
        "1": [".jpg", ".png"],
        "2": [".mp3"],
        "3": [".mp4", ".mkv"],
        "4": [".pdf"]
        # You can add more categories and their extensions here.
    }
    extension = file_path[file_path.rfind("."):]
    return extension in valid_extensions.get(file_type, [])

def encrypt_file(file_path, key, cipher_mode):
    cipher = AES.new(key, cipher_mode)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    ciphertext = cipher.iv + cipher.encrypt(pad(file_data, AES.block_size))
    return ciphertext

def decrypt_file(ciphertext, key, output_path, cipher_mode):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, cipher_mode, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_path, 'wb') as file:
        file.write(decrypted_data)

def log_encryption_details(file_name, encrypted_file_name, encrypted_file_path, key, is_encryption=True):
    if is_encryption:
        current_time = time.localtime()
        formatted_time = time.strftime("%a-%b-%d %I:%M:%S %p", current_time)
        year = time.strftime("%Y", current_time)
        with open('logs.txt', 'a') as log_file:
            log_file.write("=" * 70 + "\n")
            log_file.write(f"File Name: {file_name}\n")
            log_file.write(f"Encrypted File Name: {encrypted_file_name}\n")
            log_file.write(f"Encrypted File Path: {encrypted_file_path}\n")
            log_file.write(f"Encryption Key: {key}\n")
            log_file.write(f"Timestamp: [{formatted_time}] [{year}]\n")
            log_file.write("=" * 70 + "\n")

while True:
    print("\nWhat file do you want to encrypt?\n")
    print("1. Photo (.jpg, .png)")
    print("2. Music (.mp3)")
    print("3. Video (.mp4, .mkv)")
    print("4. PDF (.pdf)")
    print("5. Decrypt a file")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice in ["1", "2", "3", "4"]:
        print()
        if choice == '1':
            file_category = "Photo (.jpg, .png)"
        elif choice == '2':
            file_category = "Music (.mp3)"
        elif choice == '3':
            file_category = "Video (.mp4, .mkv)"
        else:
            file_category = "PDF (.pdf)"

        print(f"Selected: {file_category}")

        file_path = choose_file(file_category)
        if not is_valid_file(file_path, choice):
            print("Invalid file type. Please select a file matching the chosen category.")
            continue

        encrypted_file_path = choose_save_location(file_path, is_encrypted=True)
        cipher_mode = AES.MODE_CBC
        encryption_key = input("Enter the 16-digit encryption key: ")
        try:
            if len(encryption_key) != 16:
                raise ValueError("Encryption key must be 16 characters long.")
            ciphertext = encrypt_file(file_path, encryption_key.encode(), cipher_mode)
            with open(encrypted_file_path, 'wb') as file:
                file.write(ciphertext)
            print(f"{os.path.basename(encrypted_file_path)} encrypted and saved.")
            log_encryption_details(os.path.basename(file_path), os.path.basename(encrypted_file_path), encrypted_file_path, encryption_key)
        except ValueError as e:
            print("Invalid encryption key. Please provide a 16-digit key.")
        except FileNotFoundError:
            print("File not found.")
    elif choice == "5":
        print()
        file_category = "file"
        print(f"Selected: Decrypt a {file_category}")

        encrypted_file_path = choose_encrypted_file(file_path)
        if not encrypted_file_path:
            print("No encrypted file selected.")
            continue

        decrypted_file_path = choose_save_location(encrypted_file_path, is_encrypted=False)
        cipher_mode = AES.MODE_CBC
        decryption_key = input("Enter the 16-digit decryption key: ")
        try:
            if len(decryption_key) != 16:
                raise ValueError("Decryption key must be 16 characters long.")
            with open(encrypted_file_path, 'rb') as file:
                ciphertext = file.read()
            decrypt_file(ciphertext, decryption_key.encode(), decrypted_file_path, cipher_mode)
            print(f"{os.path.basename(encrypted_file_path)} decrypted and saved.")
        except ValueError as e:
            print("Invalid decryption key. Please provide a 16-digit key.")
        except Exception as e:
            print("Error occurred while decrypting the file.")
            # You can print the specific error message if needed.
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please select a valid option.")

    # Add two lines gap between old and new sessions
    print("\n\n")
