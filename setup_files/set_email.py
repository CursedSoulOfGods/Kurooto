import os
print("\nWelcome to Email Service Defaults")
print("As of now we only support Gmail but more services will be available soon\n")
print("In order to use Kurooto Email Service")
email = input("Enter your email:\n")
email_store_loc = os.path.normpath((os.path.join(os.path.dirname(__file__), "user/mail_service")))
email_store_loc = email_store_loc.replace("\\setup_files", "")
email_store = open(email_store_loc + "\email.KRT", 'w')
email_store.write(email)
email_store.close()
print("Done, read the docs for next steps")


