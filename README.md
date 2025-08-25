# Encry-Decry-nator
A basic python+cybersecurity project

🔐 Project Overview
Welcome to the Encryptor-Decryptor, a Python script designed for educational purposes to demonstrate the basic concepts of encryption and decryption. This project takes a user's password, generates a random "hash" and an "access token," and then allows the user to retrieve the original password using the token.

⚠️ Disclaimer: This project uses a simplified, insecure method for demonstration. It should not be used to protect real-world passwords.

✨ Features
Secure Input: Uses the getpass module to hide the password as it's being typed.

Password "Hashing": Generates a random, simulated hash value to represent the encrypted password.

Token Generation: Creates a unique, random access token required for decryption.

File Storage: Saves the generated hash and token to tokens.txt for later use.

Conditional Decryption: Allows password retrieval only if the correct access token is provided.

💻 How to Use
Save the Code: Save the provided Python code as encryptor.py.

Open a Terminal: Navigate to the directory where you saved the file.

Run the Script: Execute the script using the following command:

Bash

python encryptor.py
Follow the Prompts: Enter your password when prompted. The script will then display the generated hash and access token. To "decrypt" the password, enter the correct token.
