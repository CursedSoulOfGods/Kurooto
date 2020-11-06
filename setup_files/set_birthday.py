import datetime
import os
birthday_date = input("Enter your birthdate here! Format (M-D-YY). Read the docs for more info on the format!\n")
try:
    datetime.datetime.strptime(birthday_date, "%m-%d-%y")
    bday_store_loc = os.path.normpath(os.path.join((os.path.dirname(os.path.abspath(__file__))), "user\\user_info"))
    bday_store_loc = bday_store_loc.replace("\\setup_files", "")

    bd_file = open(bday_store_loc + "\\bday.KRT", 'w')
    bd_file.write(birthday_date)
    bd_file.close()
    print("Done!")
except ValueError:
    print("Restart and enter data as instructed in a valid form!")