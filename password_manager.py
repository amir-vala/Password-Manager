import bcrypt 
import random
import string 
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

i = 5
passhash = b'$2b$12$2TSbRdljVhMXT9mLmkwt5OnfaGFVDYwkRlcSlar4TxWLFjW1WX5cm'
appst = False
encryptedPass = []
keys=[]

def searckkey(username):
    try:
        with open("key.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): 
        print("\U000026A0 ERROR: Failed to read key file!")
        return None
    
    if username in data:
        ans = base64.b64decode(data[username]["KEY"])
        return ans
    else: 
        print("\U0001F50D Username not found! ❌")
        return None

def searchpass(username):
    try: 
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): 
        print("\U000026A0 ERROR: Failed to read password file!")
        return None
    
    if username in data:
        ans = base64.b64decode(data[username]["password"])
        return ans
    else: 
        print("\U0001F50D Password not found for this username! ❌")
        return None

def savekey(usrnm, key):
    try:
        with open("key.json", "r") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\U0001F4A3 No key storage found, creating a new one...")
        data = {}
    
    for i in range(len(usrnm)):
        data[usrnm[i]] = {"KEY": base64.b64encode(key[i]).decode()}
    
    with open("key.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def randpass(usr, leng):
    allchar = list(set(string.ascii_letters + string.digits + "!@#$%^&*()-_=+/~`") - set(usr))
    random_string = ''.join(random.choices(allchar, k=leng))
    return random_string

def encrypt(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message_padded = pad(message.encode(), AES.block_size)
    encrypted = cipher.encrypt(message_padded)
    return base64.b64encode(iv + encrypted).decode()

def decrypt(encrypted_message, key):
    raw_data = base64.b64decode(encrypted_message)
    iv = raw_data[:16]
    encrypted_data = raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted.decode('utf-8')

def savepass(usrnm, passd):
    try:
        with open("passwords.json", "r") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\U0001F4A3 No password storage found, creating a new one...")
        data = {}
    
    for i in range(len(passd)):
        data[usrnm[i]] = {"password": base64.b64encode(passd[i].encode()).decode(), "notes": "Some notes about this password"}
    
    with open("passwords.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def main(appstd):
    if appstd:
        while True:
            print("\n\U0001F4A1 Welcome to Password Manager \U0001F511")
            print("\n🔹 1 - Generate a new password")
            print("🔹 2 - Retrieve a password")
            print("🔹 0 - Exit")
            
            x = int(input("\nYour choice: "))
            if x == 1:
                x1 = int(input('\n🔢 How many characters do you want? '))
                x2 = input('\n❌ Which characters do you want to exclude? ')
                x3 = int(input('\n🔄 How many passwords do you need? '))
                passwords = [randpass(x2, x1) for _ in range(x3)]
                
                print('\n🎉 Generated Passwords:')
                for p in passwords:
                    print(f'👉 {p}')
                
                if int(input('\n✅ Do you want to save these passwords? (1-Yes, 2-No) ')) == 1:
                    username = [input(f'🆔 Username for password {i+1}: ') for i in range(len(passwords))]
                    keys = [os.urandom(32) for _ in range(len(passwords))]
                    encryptedPass = [encrypt(passwords[i], keys[i], os.urandom(16)) for i in range(len(passwords))]
                    savepass(username, encryptedPass)
                    savekey(username, keys)
                    print('\n✔ Passwords saved successfully!')
            elif x == 2:
                usrnm = input('\n🆔 Enter your username: ')
                enpass = searchpass(usrnm)
                enkey = searckkey(usrnm)
                if enpass and enkey:
                    decrypted_password = decrypt(enpass, enkey)
                    print(f"\n🔓 Password for {usrnm}: {decrypted_password}")
            elif x == 0:
                print("👋 Exiting... Goodbye!")
                break

while i > 0:
    if os.path.exists("apppass.json"):
        password = input("\n🔑 Enter your password: ")
        with open("apppass.json", "r") as file:
            data = json.load(file)
        
        passhash = base64.b64decode(data["user1"]["password"].encode())
        if bcrypt.checkpw(password.encode(), passhash):
            print("\n✅ Access Granted!")
            appst = True
            main(appst)
            break
        else:
            i -= 1
            print(f"\n❌ Wrong password! {i} tries left.")
    else:
        print("\n🎉 Welcome to Password Manager v1.0")
        password = input("Set a new password: ").encode()
        final_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        with open("apppass.json", "w") as file:
            json.dump({"user1": {"password": base64.b64encode(final_hash).decode()}}, file, indent=4)
        print("\n🔒 Password set successfully!")
