while True:
    user_input = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: "))
    if user_input == 1:
        user_password = input("Please enter your password to encode: ")
        new_password = ""
        for num in user_password:
            new_password += str(int(num)+3)
        print("Your password has been encoded and stored!\n")
    elif user_input == 2:
        print(f"The encoded password is {new_password}, and the original password is {user_password}.\n")
    elif user_input == 3:
        break


