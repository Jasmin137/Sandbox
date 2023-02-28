# PASSWORD STARS

LENGTH = 6


def main():
    password = input("Enter password: ")
    while len(password) < LENGTH:
        print("Password is short. Try again!")
        password = input("Enter password: ")
    print("*" * len(password))


main()
