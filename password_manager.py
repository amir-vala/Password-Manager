import bcrypt 
import random
import string 
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

# --------------------------- Global Variables ---------------------------

# Maximum attempts for password entry
i = 5

# Stores hashed password for authentication
passhash = b''

# Application state (True if authenticated)
appst = False

# Lists to store encrypted passwords and keys
encryptedPass = []
keys=[]

# --------------------------- Functions ---------------------------

def searckkey(username):
    """
    Retrieve the encryption key associated with a username.
    """
    try:
        with open("key.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): 
        print("[ERROR] Could not read key file.")
        return None
    
    if username in data:
        ans = data[username]["KEY"]  # Retrieve stored key
        ans = base64.b64decode(ans)  # Decode Base64 to get original bytes
        return ans
    else: 
        print("[ERROR] Key not found!")
        return None

def searchpass(username):
    """
    Retrieve the encrypted password associated with a username.
    """
    try: 
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): 
        print("[ERROR] Could not read password file.")
        return None
    
    if username in data:
        ans = data[username]["password"]  # Retrieve stored password
        ans = base64.b64decode(ans)  # Decode Base64 to get original bytes
        return ans  # Return decrypted password bytes
    else: 
        print("[ERROR] Password not found!")
        return None

def savekey(usrnm, key):
    """
    Save encryption keys to a JSON file.
    """
    try:
        with open("key.json", "r") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[WARNING] Key file not found, creating a new one.")
        data = {}
    
    for i in range(len(usrnm)):
        data[usrnm[i]] = {
            "KEY": base64.b64encode(key[i]).decode(),
        }
    
    with open("key.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def randpass(usr, leng):
    """
    Generate a random password, excluding specified characters.
    """
    allchar = list(set(string.ascii_letters + string.digits + "!@#$%^&*()-_=+/~`") - set(usr))
    random_string = ''.join(random.choices(allchar, k=leng))
    return random_string

def encrypt(message, key, iv):
    """
    Encrypt a message using AES encryption in CBC mode.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message_padded = pad(message.encode(), AES.block_size)  # Padding message
    encrypted = cipher.encrypt(message_padded)
    return base64.b64encode(iv + encrypted).decode()

def decrypt(encrypted_message, key):
    """
    Decrypt an AES-encrypted message.
    """
    try:
        raw_data = base64.b64decode(encrypted_message)
        iv = raw_data[:16]
        encrypted_data = raw_data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return decrypted.decode('utf-8') 
    except Exception:
        print("[ERROR] Decryption failed!")
        return None

def savepass(usrnm, passd):
    """
    Save passwords in an encrypted format to a JSON file.
    """
    try:
        with open("passwords.json", "r") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[WARNING] Password file not found, creating a new one.")
        data = {}
    
    for i in range(len(passd)):
        data[usrnm[i]] = {
            "password": base64.b64encode(passd[i].encode()).decode(),
        }
    
    with open("passwords.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def main(appstd):
    """
    Main function to manage the password manager menu.
    """
    if appstd == True:
        while True:
            print("\n=================== PASSWORD MANAGER ===================")
            print("1 - Generate New Password")
            print("2 - Retrieve Existing Password")
            print("0 - Exit")
            print("======================================================")
            
            try:
                x = int(input("Enter your choice: "))
            except ValueError:
                print("[ERROR] Invalid input! Please enter a valid option.")
                continue
            
            if x == 1:
                try:
                    x1 = int(input('Password length: '))
                    x2 = input('Characters to exclude: ')
                    x3 = int(input('Number of passwords to generate: '))
                    passwords = [randpass(x2, x1) for _ in range(x3)]
                    print("\nGenerated Passwords:")
                    for p in passwords:
                        print("-", p)
                    
                    print('\n1 - Save | 2 - Cancel')
                    choice = int(input())
                    if choice == 1:
                        username = [input(f'Enter username for password {i+1}: ') for i in range(x3)]
                        for i in range(x3):
                            KEY = os.urandom(32) 
                            IV = os.urandom(16)
                            keys.append(KEY)
                            encryptedPass.append(encrypt(passwords[i], KEY, IV))
                        savepass(username, encryptedPass)
                        savekey(username, keys)
                except ValueError:
                    print("[ERROR] Invalid input!")
            elif x == 2:
                usrnm = input('Enter your username: ')
                enpass = searchpass(usrnm)
                enkey = searckkey(usrnm)
                if enpass and enkey:
                    decrypted_password = decrypt(enpass, enkey)
                    if decrypted_password:
                        print(f"Password for {usrnm}: {decrypted_password}")
            elif x == 0:
                break
