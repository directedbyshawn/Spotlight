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

import time, os, hashlib, base64, six

def main():

    time.sleep(2)

    print("...")

    time.sleep(3)

    clear_console(5)
    print("Welcome to the Spotlight Setup")
    clear_console(1)
    print("To begin, create a username. All of your logins for support")
    print("accounts, proxys, vpns etc will be stored under a username")
    print("and password. Therefore whenever you want to run a script, all")
    print("you have to do is sign in with your login. All login information")
    print("is encrypted, and its encryption strength scales with your password strength.")

    time.sleep(10)

    print("...")

    time.sleep(3)

    clear_console(5)

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
                print("ERROR: Username taken.")
            elif (len(username) < 3):
                print("ERROR: Please choose a username longer than 3 characters.")
            elif (not only_letters_and_nums(username)):
                print("ERROR: Please choose a username that only contains letters and numbers.")
            else:

                #creates directories used to store login information
                os.mkdir("credentials/" + username)
                os.mkdir("credentials/" + username + "/promotion")
                os.mkdir("credentials/" + username + "/support")
                os.mkdir("credentials/" + username + "/finder")
                os.mkdir("credentials/" + username + "/email")

                file = open("credentials/" + username + "/password.txt", "w")
                file.close()

                file = open("credentials/" + username + "/vpn_login.txt", "w")
                file.close()

                good_username = True
        except:
            print("ERROR: Unknown error. Try another username.")

    #user creates password (with input validation)
    good_password = False
    while (good_password == False):
        try:
            #gets password
            password = str(input("Password: "))

            if (len(password) < 8):
                print("ERROR: Please choose a password longer than 8 characters.")
            else:
                good_password = True

                #writes password to file
                file = open("credentials/" + username + "/password.txt", "w")
                file.write(sha256(password))
                file.close()

        except:
            print("ERROR: Unknown error. Try another password.")

    time.sleep(2)

    print("...")

    time.sleep(3)

    print("Account successfully created!")

    time.sleep(1)

    print("...")

    time.sleep(3)

    print("To add necessary logins (VPN, Proxy, Account, etc...), run add.py")

    time.sleep(5)

    clear_console(100)

    exit()

def sha256(var):
	"""Return the SHA-256 hash of the string var."""

	if type(var) != str:
		raise TypeError('sha256() only accepts strings as input!')

	hash_obj = hashlib.sha256()
	hash_obj.update(var.encode('utf-8'))

	return hash_obj.hexdigest()

def clear_console(n):
    print("")
    for i in range(n):
        print("-----------------------------------------------")
    print("")

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    encoded_string = encoded_string.encode('latin') if six.PY3 else encoded_string
    return base64.urlsafe_b64encode(encoded_string).rstrip(b'=')

def decode(key, string):
    string = base64.urlsafe_b64decode(string + b'===')
    string = string.decode('latin') if six.PY3 else string
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

def only_letters_and_nums(string):

    #value to determine if there are other characters in the string besides numbers and letters
    value = True

    #list of all lowercase letters, uppercase letters, and numbers
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #iterates through string, if a character is detected that is not a number or letter, the value variable is changed
    for char in string:
        if (char not in lower and char not in upper and char not in nums):
            value = False

    return value

main()
