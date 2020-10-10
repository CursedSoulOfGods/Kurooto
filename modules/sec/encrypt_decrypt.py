from cryptography.fernet import Fernet
import os

path_to_base = os.path.dirname(__file__)
path_to_pin_key = path_to_base + "\/req\KS_PIN.EKEYKRT"


def load_key_pass_id():
    # loads the key
    return open(path_to_pin_key, "rb").read()


def encrypt_file(filename, key):
    # the key
    f = Fernet(key)
    # open file
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    # the key
    f = Fernet(key)
    # open the file
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data
