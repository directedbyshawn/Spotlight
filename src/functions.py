'''

    Basic functions used throughout the entirety
    of the project.

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

def print_lines(lines):

    '''

        Prints lines in the console to space out information.

        Parameters:
            lines (int) : lines of space to be printed in console

    '''

    print("")

    for i in range(lines):
        print("-----------------------------------------------")

    print("")

def cls():

    '''

        Clears console.

    '''

    os.system("cls" if os.name=="nt" else "clear")

def sha256(string):

	'''
        Returns the SHA-256 hash of the string provided.

        Parameters:
            string (str) : string to be hashed

        Returns:
            hashed_string (str) : hashed string

    '''

    #input validation
	if (type(string) != str):
		raise TypeError("ERROR: Type Error.")

    #hashs string
	hash_obj = hashlib.sha256()
	hash_obj.update(var.encode('utf-8'))
    hashed_string = hash_obj.hexdigest()


	return hashed_string

def only_letters_and_nums(string):

    '''

        Returns True or False depending on if the provided
        string contains only letters and numbers.

        Parameters:
            string (str) : string to be tested

        Returns:
            value (bool) : status of whether the string contains only letters and numbers

    '''

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

def encode(key, string):

    '''

        Encodes string using the vignere cipher algo.

        Parameters:
            key (str) : key to encode string
            string (str) : string to be encoded

        Returns:
            encoded_string (str) : encoded string

    '''

    #empty list to store encoded characters
    encoded_characters = []

    #loops through string and adds encoded characters to list
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_characters.append(encoded_c)

    #adds characters from list to string
    encoded_string = ''.join(encoded_characters)
    encoded_string = encoded_string.encode('latin') if six.PY3 else encoded_string
    encoded_string = base64.urlsafe_b64encode(encoded_string).rstrip(b'=')


    return encoded_string

def decode(key, string):

    '''

        Decodes string using the vignere cipher algo.

        Parameters:
            key (str) : key to decode string
            string (str) : string to be decoded

        Returns:
            decoded_string (str) : decoded string

    '''

    #decodes string from latin
    string = base64.urlsafe_b64decode(string + b'===')
    string = string.decode('latin') if six.PY3 else string

    #empty list to store decoded characters
    decoded_characters = []

    #loops through string and adds decoded characters to list
    for i in range(len(string)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        decoded_characters.append(decoded_c)

    #adds characters from list to string to be returned
    decoded_string = ''.join(decoded_characters)

    return decoded_string
