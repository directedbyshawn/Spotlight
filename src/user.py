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

    def __get_vpn_password(self):
        return self.__vpn_password

    def __set_vpn_password(self, vpn_password):
        self.__vpn_password = vpn_password

class UserDoesNotExistError(Exception):

    colored_message = colored("ERROR: Name used to create user object cannot be found in credentials file.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)
