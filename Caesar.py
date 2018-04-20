###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: Caesar.py                                                        #
# Description: Caesar cipher is an encryption algorithm which changes letters #
#              using a numeric key from 1 - 25. The key tells us how far we   #
#              need to move. EX: With a key of 3, a would become d. All       #
#              letters are shifted and wrap around with z->a.                 #
###############################################################################

import CipherInterface


class Caesar(CipherInterface.CipherInterface):
    def __init__(self):
        self.key = ""

    # Determine if the key is valid or not
    # Input: User defined key
    # Output: True of False if the key is valid
    def set_key(self, key):

        # Valid key for Caesar is any integer digit > 0
        # Also if the key mod 26 is 0, it is invalid
        # A key of 0 or a multiple of 26 means no encrpytion happens
        if key.isdigit() and key != "0" and int(key) % 26 != 0:

            self.key = int(key) % 26

            return True
        else:
            # If the user didn't give a correct key, return false
            return False

    # Encrypt the given plain text based on the key
    # Input: A string of plain text
    # Output: The resulting cipher text
    def encrypt(self, plain_text):
        # Convert to lowercase so AbC will react the same as abc, etc.
        plain = plain_text.lower()
        cipher_text = ""
        key = self.key

        # Go through each letter in the plain text, convert to ascii, and
        # increment by the key
        for c in plain:
            # Don't encrypt spaces
            if c == " ":
                continue

            letter_ascii = ord(c)
            letter_ascii += key

            # Going out of bounds on the letter ascii > (z = 122), loop back to
            # beginning. EX: ascii of 123-26 = 97 = a
            if letter_ascii > 122:
                letter_ascii -= 26

            # Build the cipher text
            cipher_text += chr(letter_ascii)

        return cipher_text

    # Decrypt the given cipher text based on the key
    # Input: A string of cipher text
    # Output: The resulting plain text
    def decrpyt(self, cipher_text):
        cipher = cipher_text.lower()
        plain_text = ""
        key = self.key

        # Go through each letter in the cipher text, convert to ascii, and
        # decrement by the key
        for c in cipher:
            letter_ascii = ord(c)
            letter_ascii -= key

            # Going out of bounds on the letter ascii < (a = 97), loop back to
            # end. EX: ascii of 96+26 = 122 = z
            if letter_ascii < 97:
                letter_ascii += 26

            # Build the plain text
            plain_text += chr(letter_ascii)

        return plain_text
