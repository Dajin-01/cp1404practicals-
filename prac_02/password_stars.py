def get_password():
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Password is too short, please enter at least 8 characters.")
        password = input("Enter your password: ")
    return password


def print_asterisks(password):
    print('*' * len(password))


def main():
    password = get_password()
    print_asterisks(password)


main()

