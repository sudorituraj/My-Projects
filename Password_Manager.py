import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        write_key()
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def generate_or_load_salt():
    if not os.path.exists("salt.key"):
        salt = os.urandom(16)
        with open("salt.key", "wb") as salt_file:
            salt_file.write(salt)
    else:
        with open("salt.key", "rb") as salt_file:
            salt = salt_file.read()
    return salt

def get_fernet_from_master_password(master_password):
    salt = generate_or_load_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return Fernet(derived_key)

master_pwd = input("What is the master password? ")
if master_pwd != "ritu":
    print("Entered Master Password Is Incorrect!")
    exit()
else:
    print("Master Password is correct")
    fer = get_fernet_from_master_password(master_pwd)

def view():
    if not os.path.exists("pwd.txt"):
        print("No saved passwords found.")
        return

    with open("pwd.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, encrypted_passw = data.split("|")
                try:
                    decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                    print("User:", user, ", Password:", decrypted_passw)
                except Exception as e:
                    print("Error decrypting password:", e)

def add():
    name = input("Username: ")
    pwd = input("Enter the Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open("pwd.txt", "a") as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Credentials added successfully.")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add or q to quit)? ")
    
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
