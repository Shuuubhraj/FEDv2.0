File Encryption and Decryption (FED) v2.0
Python Version :  Python 3.x (The "x" in Python 3.x refers to any version within the Python 3 series.)

[DESCRIPTION]
This Python script is a simple command-line tool that allows you to encrypt and decrypt files using the AES encryption algorithm with Cipher Block Chaining (CBC) mode. The tool uses the tkinter library for file selection dialogs and the Crypto.Cipher module from the pycryptodome package for encryption and decryption operations.

[USAGE]
Run the script, and it will display a pre-load screen with an ASCII art banner.
The script will present you with a menu to choose the desired operation:
- Encrypt a file of a specific category (Photo, Music, Video, or PDF).
- Decrypt a previously encrypted file.
- Exit the script.

If you choose to encrypt a file, the script will prompt you to select the file you want to encrypt. After selecting the file, it will then ask you to choose a location to save the encrypted file. You will also need to provide a 16-digit encryption key for the AES algorithm.

If you choose to decrypt a file, the script will prompt you to select the encrypted file you want to decrypt. After selecting the file, it will then ask you to choose a location to save the decrypted file. You will also need to provide the 16-digit decryption key used during encryption.

The script will log the encryption details, including the original file name, encrypted file name, encrypted file path, and encryption key, in a file called logs.txt within the script's directory.

[SUPPORTED FILE TYPES]

Photo: .jpg, .png
Music: .mp3
Video: .mp4, .mkv
PDF: .pdf

[DISCLAIMER]

This script is provided as-is and without warranty. Use it at your own risk.
Ensure that you keep the encryption keys safe and secure. Losing the keys will result in permanent data loss.

[AUTHOR]

Name: Rajput Shubhraj Singh
GitHub: https://github.com/yourusername

[ACKNOWLEDGEMENTS]

Special thanks ❤️ to the developers of tkinter and pycryptodome for their excellent libraries.
