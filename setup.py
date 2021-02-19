'''

    This script will create a new spotlight profile for
    you. The purpose of profiles is to store data for each
    account promoted by the service. For each instagram
    you wish to promote, you must set up a new user
    profile, which will store logins for vpns, proxys,
    and support accounts. If you wish to add more support
    accounts to an existing profile, run add.py

    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------

                           v1.0
                     @dirctedbyshawn

    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------

'''

import time, random, os
from termcolor import colored
from src.functions import *

def main():

    time.sleep(2)

    print("...")

    time.sleep(3)

    print_lines(5)
    print("Welcome to the Spotlight Setup")
    print_lines(1)
    print("To begin, create a username. All of your logins for promotion")
    print("accounts, proxys, vpns etc will be stored under a username")
    print("and password. Therefore whenever you want to run a script, all")
    print("you have to do is sign in with your login. All login information")
    print("is encrypted, and its encryption strength scales with your")
    print("password strength.")

    time.sleep(10)

    print("...")

    time.sleep(3)

    print_lines(5)

    #creates credentials directory if it does not already exist
    if (not os.path.exists("credentials")):
        os.mkdir("credentials")

    #user creates login name (with input validation)
    good_username = False
    while (good_username == False):
        try:
            #gets new username
            username = str(input("New Username: "))

            #determines if it has been taken
            if (os.path.exists("credentials/" + username )):
                print(colored("ERROR: Username taken.", "red"))
            elif (len(username) < 3):
                print(colored("ERROR: Please choose a username longer than 3 characters.", "red"))
            elif (not only_letters_and_nums(username)):
                print(colored("ERROR: Please choose a username that only contains letters and numbers.", "red"))
            else:

                #creates directories used to store login information
                os.mkdir("credentials/" + username)
                os.mkdir("credentials/" + username + "/promotion")
                os.mkdir("credentials/" + username + "/finder")

                file = open("credentials/" + username + "/password.txt", "w")
                file.close()

                file = open("credentials/" + username + "/vpn_login.txt", "w")
                file.close()

                good_username = True
        except:
            print(colored("ERROR: Unknown error. Try another username."), "red")

    #user creates password (with input validation)
    good_password = False
    while (good_password == False):
        try:
            #gets password
            password = str(input("Password: "))

            if (len(password) < 8):
                print(colored("ERROR: Please choose a password longer than 8 characters.", "red"))
            else:
                good_password = True

                #writes password to file
                file = open("credentials/" + username + "/password.txt", "w")
                file.write(sha256(password))
                file.close()

        except:
            print(colored("ERROR: Unknown error. Try another password.", "red"))

    time.sleep(2)

    print("...")

    time.sleep(3)

    print("Account successfully created!")

    time.sleep(1)

    print("...")

    time.sleep(3)

    print("To add necessary logins (VPN, Proxy, Account, etc...), go back to")
    print("run.py and choose the add info option.")

    time.sleep(5)

    print_lines(100)

    exit()

main()
