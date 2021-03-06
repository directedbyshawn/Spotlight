'''

    This class is used to access the chrome browser to
    connect to the internet. It is basically the same as
    the nerodia browser class, however I addded some methods
    and other features to make browsing instagram easier.

    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------

                           v1.0
                      directedbyshawn

    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------
    ---------------------------------------------------

'''

import time, random, os
import undetected_chromedriver as uc
from nerodia.browser import Browser as Brwse
from nordvpn_connect import initialize_vpn, get_current_ip, connect_to_server, close_vpn_connection, rotate_VPN
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from functions import *
from termcolor import colored

class Browser():

    def __init__(self, account, email, user):
        self.__browser_status = False
        self.__vpn_status = False
        self.__account = account
        self.__email = email
        self.__user = user
        self.driver = None
        if (user == None):
            self.__vpn_email = None
            self.__vpn_password = None
        else:
            self.__vpn_email = user.get_vpn_email()
            self.__vpn_password = user.get_vpn_password()

    def get_browser_status(self):
        return self.__browser_status

    def __set_browser_status(self, status):

        #ensures that status is of boolean type
        if type(status) != bool:
            raise TypeError("ERROR: Status must be boolean")
        else:
            self.__browser_status = status

    def get_vpn_status(self):
        return self.__vpn_status

    def __set_vpn_status(self, status):

        #ensures that status is of boolean type
        if (type(status) != bool):
            raise TypeError("ERROR: Status must be boolean")
        else:
            self.__vpn_status = status

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_account(self):
        return self.__account

    def set_account(self, account):
        self.__account = account

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def start(self):

        #ensures that browser is not already open before opening
        if (self.is_browser_open()):
            raise BrowserNotOpenError
        else:

            #initiates web browser
            self.driver = uc.Chrome()

            #sets browser status to true, indicating that the browser is active
            self.__set_browser_status(True)

            print(self.__browser_status)

    def stop(self):

        #throws an exception if the browser is not open
        if (not self.is_browser_open()):
            raise BrowserNotOpenError()
        else:

            #closes nerodia web browser
            self.driver.close()

            #sets browser status to false, indicating that the browser is no longer active
            self.__set_browser_status(False)

    def goto(self, link):

        #makes sure that link is a string, and that the browser is open
        if (type(link) != str):
            raise TypeError(colored("ERROR: Link must be a string", "red"))
        elif (not self.is_browser_open()):
            raise BrowserNotOpenError()
        else:
            self.driver.get(link)

    def back(self):

        '''
        #makes sure browser is open and throws exception otherwise
        if (self.is_browser_open()):
            self.driver.back()
        else:
            raise BrowserNotOpenError()

        '''

    def forward(self):

        '''

        #makes sure browser is open and throws exception otherwise
        if (self.is_browser_open()):
            self.driver.forward()
        else:
            raise BrowserNotOpenError()

        '''

    def is_browser_open(self):
        return (self.get_browser_status == True and self.driver != None)

    def vpn_start(self):

        #ensures that vpn is not already running, and if so throws an exception
        if (self.get_vpn_status() == True):
            self.vpn_stop()
            raise VPNError()
        else:
            settings = initialize_vpn("United States", self.__vpn_email, self.__vpn_password)
            rotate_VPN(settings)

    def vpn_stop(self):

        #ensures that vpn is currently running, and if not throws an exception
        if (self.get_vpn_status() == False):
            raise VPNError()
        else:
            settings = initialize_vpn("United States", self.__vnp_email, self.__vpn_password)
            close_vpn_connection(settings)

    def change_vpn(self):

        #ensures that vpn is connected, and throws an exception if not connected
        if (self.get_vpn_status() != True):
            raise VPNError()
        else:
            settings = initialize_vpn("United States", self.__vpn_email, self.__vpn_password)
            close_vpn_connection(settings)
            time.sleep(10)
            rotate_VPN(settings)

    def clear_cache(self):
        #navigate to chrome settings and clear cache and browser history
        pass

    def __str__(self):
        #returns string with data about browser instance
        pass


class BrowserNotOpenError(Exception):

    colored_message = colored("ERROR: Browser not open.", "red")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)

class VPNError(Exception):

    colored_message = colored("ERROR: VPN is trying to be opened while closed, or vice versa.")

    def __init__(self, message = colored_message):
        self.message = message
        super().__init__(self.message)
