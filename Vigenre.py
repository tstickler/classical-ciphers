###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: Vigenre.py                                                       #
# Description: The Vigenre cipher uses a 26x26 letter matrix comprised of     #
#              of the 26 Caesar ciphers. The key will be a series of letters  #
#              which map to rows of the matrix. Then the plain text letters   #
#              map to the columns of the matrix. Finding the intersection of  #
#              the key letter and plain text letter will give the cipher text #
#              letter to build encryption or decrypt the cipher text.         #
###############################################################################

import CipherInterface


class Vigenre(CipherInterface.CipherInterface):
    def __init__(self):
        self.key = ""
        self.matrix = [[]]

    # Build the 26x26 matrix
    # Input: None
    # Output: None. Sets the matrix for the object.
    def build_rows(self):
        self.matrix = [[0 for x in range(26)] for y in range(26)]
        for i in range(0, 26):
            for j in range(0, 26):
                char_to_add = j + i + 97
                if char_to_add > 122:
                    char_to_add -= 26
                self.matrix[i][j] = (chr(char_to_add))

        return

    # Determine if the key is valid or not
    # Input: User defined key
    # Output: True of False if the key is valid
    def set_key(self, key):
        key = key.lower()

        # Check if key is a-z lowercase
        for c in key:
            if 97 <= ord(c) <= 122:
                continue
            else:
                # If the user didn't give a correct key, return false
                return False

        # If we make it out of the loop without returning, key is fine
        self.key = key
        return True

    # The key needs to be modified to be the same length as the text
    # Input: A string of text
    # Output: A key matching the length of the input
    def modify_key(self, in_text):
        key = self.key
        text = in_text

        length_of_key = len(key)
        length_of_text = len(text)

        # If the key is smaller than the plain text, duplicate it until it is
        # equal or greater than the size of the plain text
        while length_of_key < length_of_text:
            key += self.key
            length_of_key = len(key)

        # If the key is greater than the plain text, remove letters from the
        # back to make the lengths equal
        if length_of_key > length_of_text:
            num_to_remove = length_of_key - length_of_text
            key = key[:-num_to_remove]

        return key

    # Encrypt the given plain text based on the key
    # Input: A string of plain text
    # Output: The resulting cipher text
    def encrypt(self, plain_text):
        cipher_text = ""

        # Strip all whitespace from the plain text
        plain = "".join(plain_text.split())

        # Modify key to match plain text length
        key = self.modify_key(plain)

        # Find the spot in the matrix to begin encryption
        for i in range(0, len(plain)):
            # Row - Subtract 97 to find proper spot in the matrix
            matrix_index_for_key = ord(key[i]) - 97

            # Column - Subtract 97 to find proper spot in the matrix
            matrix_index_for_plain = ord(plain[i]) - 97

            # Build cipher text
            cipher_text += \
                self.matrix[matrix_index_for_key][matrix_index_for_plain]

        return cipher_text

    # Decrypt the given cipher text based on the key
    # Input: A string of cipher text
    # Output: The resulting plain text
    def decrpyt(self, cipher_text):
        key = self.modify_key(cipher_text)
        cipher = cipher_text
        plain_text = ""

        # Find the spot in the matrix to begin encryption
        for i in range(0, len(key)):
            # The letter of the cipher text we need to find in the matrix
            letter = cipher[i]

            # Row - Subtract 97 to find proper spot in the matrix
            matrix_index_for_key = ord(key[i]) - 97

            # Look through the matrix at row found in previous step for the
            # letter of the cipher text
            for j in range(0, 26):
                # When the letter is found, use the index it is at to determine
                # which letter of plain text it maps to
                if self.matrix[matrix_index_for_key][j] == letter:
                    # Build the plain text
                    plain_text += chr(j+97)

                    break

        return plain_text
