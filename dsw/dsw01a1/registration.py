user = {}
#Registration
print("\nREGISTRATION\n")
user['first_name'] = str(input("What is your first name: "))
user['last_name'] = str(input("What is your last name: "))
user['email_address'] = str(input("Enter your email address: "))
user['password'] = str(input("Enter password: "))
user['confirm_password'] = str(input("Confirm password: "))

if '@' not in user['email_address']:
    print("Invalid email")

if user['password'] != user['confirm_password']:
    print("Passwords dont match")

if len(user['password']) < 8:
    print("Password length less than 8 characters")

#login
print("\nLOGIN\n")
login_user_email_address = str(input("Email address: "))
login_user_password = str(input("Password: "))

if '@' not in login_user_email_address:
    print("Invalid email")
elif login_user_email_address == user['email_address']:
    if login_user_password == user['password']:
        print("login Successful")
