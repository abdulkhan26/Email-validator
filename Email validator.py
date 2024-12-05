email = input("ENTER YOUR EMAIL: ")
j, k, d = 0, 0, 0  # Flags for capital letters, spaces, and invalid characters

if len(email) >= 10:  # Check minimum length
    if email[0].isalpha():  # Check if the first character is an alphabet
        if "@" in email and email.count("@") == 1:  # Check presence and uniqueness of '@'
            domain = email.split("@")[1]
            if domain.split(".")[0] == "gmail":  # Check if the domain is 'gmail'
                if (email[-4] == "." or email[-3] == "."):  # Ensure '.' is in a valid position
                    if email.endswith(".com") or email.endswith(".in"):  # Validate email endings
                        if domain.count(".") == 1:  # Ensure exactly one dot in the domain
                            # Check for spaces, uppercase letters, and invalid characters
                            for i in email:
                                if i.isspace():
                                    print("There is a space in the email.")
                                    k = 1
                                elif i.isalpha() and i.isupper():
                                    print(f"There is a capital letter in the email at position {email.index(i)}")
                                    j = 1
                                elif i in ["_", ".", "@"]:
                                    continue
                                else:
                                    d = 1
                            
                            # Final validation
                            if k == 1 or j == 1 or d == 1:
                                print("Wrong email: contains spaces, capital letters, or invalid characters.")
                            else:
                                print("Right email!")
                        else:
                            print("Invalid email: there are more than one '.' in the domain.")
                    else:
                        print("Invalid email: it must end with '.com' or '.in'.")
                else:
                    print("Invalid email: '.' is not in the correct position.")
            else:
                print("Invalid email: domain is not 'gmail'.")
        else:
            print("Invalid email: '@' is missing or appears multiple times.")
    else:
        print("Invalid email: the first character must be an alphabet.")
else:
    print("Invalid email: it must be at least 10 characters long.")
