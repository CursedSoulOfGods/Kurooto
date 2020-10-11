import time
from encrypt_decrypt import load_key_pass_id, encrypt_file
import os
from cryptography.fernet import Fernet

# check current
path_to_req = os.path.dirname(__file__) + "\/req"
path_to_sec_type = path_to_req + "\sec_type.KRT"
path_to_pin_key = path_to_req + "\KS_PIN.EKEYKRT"
if "sec_type.KRT" in path_to_sec_type:
    lock_check = open(path_to_sec_type, "r")
    lock_type_current = lock_check.read()
    print("Current locking mechanism is " + lock_type_current)

# get user lock

choice = input("Do you want to authenticate Kurooto ?\n")
choice = choice.lower()

# setting up password lock

if 'yes' in choice:

    # writing the type

    lock_set = open(path_to_sec_type, "w")
    lock_set.write("face id and pin")
    lock_set.close()

    # getting password
    key = Fernet.generate_key()
    store_key = open(path_to_pin_key, 'wb')
    store_key.write(key)
    store_key.close()

    password = input("Please input the pin you want to use\n")
    confirm_password = input("Please confirm the PIN\n")

    if password == confirm_password:

        # saving pass
        path_to_pin = path_to_sec_type.replace("sec_type.KRT", "pin.EKRT")
        write_pin = open(path_to_pin, "w")
        write_pin.write(password)
        write_pin.close()

        # getting encryption key
        pin_key = load_key_pass_id(path_to_pin_key)

        # encryption of file

        encrypt_file(path_to_pin, pin_key)
        print("Done")

    elif password != confirm_password:
        print("Passwords don't match")

if 'no' in choice:
    lock_set = open(path_to_sec_type, "w")
    lock_set.write("none")
    lock_set.close()
    print("Ok! Exiting!")

