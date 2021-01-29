'''

    This is the script to be ran by the user. No other file
    will need to be run by a normal user. Every part of this
    program can started by this script. When ran, the user
    will be provided with a number of options, each being a
    different component of Spotlight.

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
    print("Welcome to Spotlight!")
    print_lines(1)
    print("If this is your first time using the software, choose")
    print("option 1 to setup a new user profile.")
    print_lines(1)

    time.sleep(3)

    print("----- Options -----")
    print("1. Run setup")
    print("2. Add info (VPNs, Proxies, Account logins, etc...)")
    print("3. Find Users")
    print("4. Promote Account")
    print("5. Exit")

    print("")
    print("")

    #input validation on option number
    good_option = False
    while (not good_option):

        continue_check = True

        try:
            option = int(input("Enter your option number: "))
        except:
            print(colored("ERROR: Please enter an integer value.", "red"))
            continue_check = False

        if (continue_check):
            if (option != 1 and option != 2 and option != 3 and option != 4 and option != 5):
                print(colored("ERROR: Entered number is not an option", "red"))
            else:
                good_option = True
        else:
            pass

    #performs operation based on user option
    handle_operation(option)

def handle_operation(option):
    if (option == 1):
        cls()
        exec(open("setup.py").read())
    elif (option == 2):
        cls()
        exec(open("src/add.py").read())
    elif (option == 3):
        pass
        #print something about how many windows should be opened and then do os.system to run seperate instances of the script
    elif (option == 4):
        pass
        #same thing as option 3
    else:
        exit()

main()
