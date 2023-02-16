import getpass


def main():
    print("|*********************************************************|")
    print("|                                                         |")
    print("|******************* HAWK WELCOMES YOU *******************|")
    print("|                                                         |")
    print("|*********************************************************|")
    print("|  Authorization needed...                                |")
    print("***********************************************************")
    username = input("Username :")
    password = getpass.getpass('Password :')

    # Does credentials check
    print("|*********************************************************|")
    print("|    Welcome " + username)
    print("|               HAWK Watches you!                         |")
    print("***********************************************************")
    print("|                                                         |")
    print("|*********************** MAIN MENU ***********************|")
    print("|                                                         |")
    print("|*********************************************************|")
    print("|    1. Faces                                             |")
    print("|    2. Settings                                          |")
    print("***********************************************************")

main()