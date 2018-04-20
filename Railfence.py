###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: Railfence.py                                                     #
# Description:  The railfence cipher is used by putting the plain text into   #
#               rows. The number of rows used is the key size. After the rows #
#               have been made, they will be combined into a single string.   #
#               We can decrypt by splitting the cipher text back into rows    #
#               and reading along the columns.                                #
###############################################################################

import CipherInterface


class Railfence(CipherInterface.CipherInterface):
    def __init__(self):
        self.key = ""

    # Determine if the key is valid or not
    # Input: User defined key
    # Output: True of False if the key is valid
    def set_key(self, key):

        # Valid key for railfence is any integer digit > 0
        if key.isdigit() and key != "0":

            self.key = int(key)

            return True
        else:
            # If the user didn't give a correct key, return false
            return False

    # Encrypt the given plain text based on the key
    # Input: A string of plain text
    # Output: The resulting cipher text
    def encrypt(self, plain_text):
        plain = plain_text
        cipher_text = ""
        key = self.key

        # Create the rails
        rails = []
        for i in range(0, key):
            rails.append("")

        # Add letters to the rails
        i = 0
        for c in plain:
            # Don't encrypt spaces
            if c == " ":
                continue

            # Add letter to the specified rail
            rails[i] += c

            # Move to next rail
            i += 1
            if i == key:
                i = 0

        # Build cipher text by combining the rails
        for i in rails:
            cipher_text += i

        return cipher_text

    # Decrypt the given cipher text based on the key
    # Input: A string of cipher text
    # Output: The resulting plain text
    def decrpyt(self, cipher_text):
        cipher = cipher_text
        plain_text = ""
        key = self.key

        # Find out how many letters are going to be in the rails
        length_of_cipher = len(cipher)
        letters_per_row = int(length_of_cipher / key)
        remainder = length_of_cipher % key

        # Create the rails
        rails = []
        for i in range(0, key):
            # Determines if a row should have an extra letter or not
            if remainder > 0:
                letter_for_remainder = 1
                remainder -= 1
            else:
                letter_for_remainder = 0

            # Set rail equal to the first letters_per_row + remainder in the
            # cipher
            rails.append(cipher[:letters_per_row + letter_for_remainder])

            # Cipher removes the characters that were added
            cipher = cipher[letters_per_row + letter_for_remainder:]

        # Loop through rails to build the plain text
        j = 0
        for i in range(0, length_of_cipher):
            # Get the first element of the rail into plain text
            plain_text += rails[j][:1]

            # Remove the first element from the rail
            rails[j] = rails[j][1:]

            # Move through each rail
            j += 1
            if j == key:
                j = 0

        return plain_text
