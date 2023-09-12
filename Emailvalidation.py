import re

def Email_Valid(email):
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email):
        return True
    else:
        return False

user_email = input("Enter your email address: ")

if Email_Valid(user_email):
    # Email is valid, proceed to capture it in the database
    # ... capture email in the database logic ...
    print("Email is valid. Capturing in the database.")
else:
    print("Invalid email address. Please enter a valid email.")
