def email():
    print("Welcome to email slicer...")

    email_input = input("Input your email address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

email()