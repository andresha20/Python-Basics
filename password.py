def validate_password():
    while True:
        try:
            password = input("Enter the password: ")
            if password == 'admin':
                print("Password correct. Access granted.")
                break 
            else:
                raise ValueError("Incorrect password. Try again.")
        except ValueError as error:
            print(error)

validate_password()
