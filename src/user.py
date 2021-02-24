'''

    This class represents each different account being
    promoted by the spotlight service. For each account
    you wish to promote, you will have a different user
    profile. The user profile will be connected to the
    accounts promoting your main instagram account, the
    accounts used to find instagram users to interact
    with, and anything else related to spotlight.

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
from functions import *
from termcolor import colored

class User():

    def __init__(self, name):

        #if files under name don't exist, exception is raised
        if (not os.path.exists("../credentials/" + name)):
            raise UserDoesNotExistError()
        else:
            self.__name = name
            self.__directory_path = "../credentials/" + name + "/"
        self.__password = None
        self.__vpn_email = None
        self.__vpn_password = None
        self.__logged_in = False

    def get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    def __get_password(self):
        return self.__password

    def __set_password(self, password):
        self.__password = password

    def get_vpn_password(self):
        return self.__vpn_password

    def __set_vpn_password(self, vpn_password):
        self.__vpn_password = vpn_password

    def get_vpn_email(self):
        return self.__vpn_email

    def __set_vpn_email(self, email):
        self.__vpn_email = email

    def get_login_status(self):
        return self.__logged_in

    def __set_login_status(self, status):
        self.__logged_in = status

    def log_in(self, password):

        #if user is already logged in, exception raised
         if (self.get_login_status()):
             raise AlreadyLoggedInError()

        password_correct = False

        #attemps to open file containing password
        try:
            password_file = open((self.__directory_path + "password.txt"), "r")
        except:
            pass






class PasswordFileNotFound(Exception):

    colored_message = colored("ERROR: Password file could not be opened.")

class UserDoesNotExistError(Exception):

    colored_message = colored("ERROR: Name used to create user object cannot be found in credentials file.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class AlreadyLoggedInError(Exception):

    colored_message = colored("ERROR: User log in attempt while already logged in.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)
