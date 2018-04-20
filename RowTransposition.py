###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: RowTransposition.py                                              #
# Description: The Row Transposition cipher splits the text into rows and     #
#              will then reorder the columns of letters based on the key. The #
#              key MUST be a number with a sequence ie 34215. It doesn't have #
#              to be in order but the numbers have to increase up to the max. #
###############################################################################

import CipherInterface
import math


class RowTransposition(CipherInterface.CipherInterface):
    def __init__(self):
        self.key = ""

    # Determine if the key is valid or not
    # Input: User defined key
    # Output: True of False if the key is valid
    def set_key(self, key):
        # Key should be between 2 and 9 characters
        if key.isdigit() and 1 < len(key) < 10:

            key_list = []

            for c in key:
                # There should be no 0s in the eky
                if c == "0":
                    return False

                if c in key_list:
                    # Key should not have duplicates
                    # If a duplicate was found, invalid key
                    return False
                else:
                    # Build the key
                    key_list.append(c)

            # Makes sure the key has a 1,2,3... somewhere in it
            # Goes from 1 to length of list + 1 to check all values present
            for i in range(1, len(key_list) + 1):
                found = False

                # Search key_list to see if it contains the number
                for j in key_list:
                    if int(j) == i:
                        found = True
                        break

                # Return false if the number was not found
                # Invalid key
                if not found:
                    return False

            # Makes sure the key is greater than length of 1
            # If we haven't returned false by now, valid key
            if len(key_list) > 1:
                self.key = "".join(key_list)
                return True
        else:
            # Key had a non digit or was not of proper size
            return False

    # Encrypt the given plain text based on the key
    # Input: A string of plain text
    # Output: The resulting cipher text
    def encrypt(self, plain_text):
        key = self.key
        plain = list(plain_text.lower().replace(" ", ""))
        num_rows = math.ceil(len(plain) / len(key))

        # Make sure all rows will be filled equally
        while len(plain) % (len(key) * num_rows) != 0:
            plain.append("x")

        length_of_plain = len(plain)

        # Create the rows from plain text
        rows = [[0 for x in range(int(length_of_plain / num_rows))]
                for y in range(num_rows)]

        for i in range(0, num_rows):
            for j in range(0, len(key)):
                rows[i][j] = plain.pop(0)

        # Create the columns from the rows
        cols = [[0 for x in range(num_rows)]
                for y in range(int(length_of_plain / num_rows))]

        for i in range(len(key)):
            for j in range(num_rows):
                cols[i][j] = rows[j][i]

        # Order the columns should be arranged
        key_order = []
        for i in range(1, len(key) + 1):
            for j in range(0, len(key)):
                if i == int(key[j]):
                    key_order.append(j)

        # Create cipher text
        cipher_list = []
        for c in key_order:
            num = int(c)
            cipher_list.append(cols[num])

        for i in range(len(cipher_list)):
            cipher_list[i] = "".join(cipher_list[i])

        cipher_text = "".join(cipher_list)

        return cipher_text

    # Decrypt the given cipher text based on the key
    # Input: A string of cipher text
    # Output: The resulting plain text
    def decrpyt(self, cipher_text):
        key = self.key
        cipher = list(cipher_text)
        num_rows = int(len(cipher) / len(key))
        length_of_cipher = len(cipher)

        # Create the columns
        cols = [[0 for x in range(num_rows)]
                for y in range(int(length_of_cipher / num_rows))]

        for i in range(len(key)):
            for j in range(num_rows):
                cols[i][j] = cipher.pop(0)

        # Build list with cipher text
        cipher_list = []
        for c in key:
            num = int(c)
            cipher_list.append(cols[num - 1])

        # Create the rows from cipher list
        rows = [[0 for x in range(int(length_of_cipher / num_rows))]
                for y in range(num_rows)]

        for i in range(0, num_rows):
            for j in range(0, len(key)):
                rows[i][j] = cipher_list[j][i]

        # Build the plain text
        for i in range(len(rows)):
            rows[i] = "".join(rows[i])

        plain_text = "".join(rows)

        return plain_text
