###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: Playfair.py                                                      #
# Description: This cipher uses a letter matrix to encrypt or decrypt. The    #
#              user defined key will be a word which will make up the first   #
#              part of the 5x5 matrix. All duplicates will be stripped and    #
#              all Js will be replaced Is.                                    #
###############################################################################

import CipherInterface


class Playfair(CipherInterface.CipherInterface):
    def __init__(self):
        self.key = ""
        self.matrix = [[0 for x in range(5)] for y in range(5)]

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

    # Build the 5x5 matrix based on the key
    # Input: User defined key
    # Output: None. Sets the matrix for the object
    def construct_key_matrix(self, key):
        matrix = self.matrix

        # Determine which letters of the key should be in the matrix
        # Prevent duplicates, replace j with i
        seen = []

        for c in key:
            if c not in seen:
                if c == "j":
                    c = "i"
                seen.append(c)

        # Build matrix with key
        x = 0
        for i in range(0, 5):
            for j in range(0, 5):
                # If seen still contains characters, pop and place them.
                # Otherwise build the matrix in alphabetical order with letters
                # that haven't appeared earlier in the matrix.
                # Always exclude in the matrix j, i takes its place.
                if seen:
                    matrix[i][j] = seen.pop(0)
                else:
                    for k in range(x, 26):
                        letter = chr(k + 97)
                        if letter not in key and letter != "j":
                            matrix[i][j] = letter
                            x = k + 1
                            break

        self.matrix = matrix

    # Encrypt the given plain text based on the matrix
    # Input: A string of plain text
    # Output: The resulting cipher text
    def encrypt(self, plain_text):
        plain = "".join(plain_text.split()).lower()
        matrix = self.matrix

        # Create the pairs of plain text
        plain_pairs = []
        while plain:
            # Grab the first two letters of the plain text
            first_two_letters = plain[:2]

            # If there was only 1 letter left in the plain text, append an x
            # so that it becomes a pair
            if len(first_two_letters) == 1:
                first_two_letters += "x"

            # If the two letters in the pair are equal, make the second letter
            # an x and only move forward by 1 letter.
            # Otherwise, add the pair to the list of pairs
            if first_two_letters[0] == first_two_letters[1]:
                plain_pairs.append(first_two_letters[0] + "x")
                plain = plain[1:]
            else:
                plain_pairs.append(first_two_letters)
                plain = plain[2:]

        cipher = []
        for pair in plain_pairs:
            letter_one = pair[0]
            letter_two = pair[1]

            # Handles j appearing in the plain text
            # j is not in the matrix but will be represented by i
            if letter_one == "j":
                letter_one = "i"
            if letter_two == "j":
                letter_two = "i"

            letter_one_coords = (-1, -1)
            letter_two_coords = (-1, -1)

            for i in range(0, 5):
                for j in range(0, 5):
                    # Find the coords of the letters
                    if matrix[i][j] == letter_one:
                        letter_one_coords = (i, j)
                    if matrix[i][j] == letter_two:
                        letter_two_coords = (i, j)

                # If both coords have been found, do the build the cipher text
                # and break from the loop
                if letter_one_coords != (-1, -1) \
                        and letter_two_coords != (-1, -1):
                    # Same row
                    if letter_one_coords[0] == letter_two_coords[0]:
                        # Stay in same row, move 1 column right of first letter
                        col_to_move = letter_one_coords[1] + 1

                        # Wrap to column 0 if at the end
                        if col_to_move == 5:
                            col_to_move = 0

                        # Append letter right of first plain text
                        cipher.append(
                            matrix[letter_one_coords[0]][col_to_move])

                        # Stay in same row, move 1 column right of second
                        # letter
                        col_to_move = letter_two_coords[1] + 1

                        # Wrap to column 0 if at the end
                        if col_to_move == 5:
                            col_to_move = 0

                        # Append letter right of second plain text
                        cipher.append(
                            matrix[letter_one_coords[0]][col_to_move])

                    # Same column
                    elif letter_one_coords[1] == letter_two_coords[1]:
                        # Stay in the same column, move 1 row down of first
                        row_to_move = letter_one_coords[0] + 1

                        # Wrap to row 0 if at the end
                        if row_to_move == 5:
                            row_to_move = 0

                        # Append letter down of the first plain text
                        cipher.append(
                            matrix[row_to_move][letter_one_coords[1]])

                        # Stay in the same column, move 1 row down of second
                        row_to_move = letter_two_coords[0] + 1

                        # Wrap to row 0 if at the end
                        if row_to_move == 5:
                            row_to_move = 0

                        # Append letter down of the second plain text
                        cipher.append(
                            matrix[row_to_move][letter_two_coords[1]])

                    # Different row and column
                    else:
                        cipher.append(
                            matrix[letter_one_coords[0]][letter_two_coords[1]])
                        cipher.append(
                            matrix[letter_two_coords[0]][letter_one_coords[1]])
                    break

        # Join the cipher list to make the cipher text string
        cipher_text = "".join(cipher)
        return cipher_text

    # Decrypt the given cipher text based on the matrix
    # Input: A string of cipher text
    # Output: The resulting plain text
    def decrpyt(self, cipher_text):
        cipher = cipher_text
        matrix = self.matrix

        # Create the pairs of cipher text
        cipher_pairs = []
        while cipher:
            # Grab the first two letters of the cipher text
            first_two_letters = cipher[:2]

            # Append the letters to the list of pairs and set the cipher
            cipher_pairs.append(first_two_letters)
            cipher = cipher[2:]

        plain = []
        for pair in cipher_pairs:
            letter_one = pair[0]
            letter_two = pair[1]

            letter_one_coords = (-1, -1)
            letter_two_coords = (-1, -1)

            for i in range(0, 5):
                for j in range(0, 5):
                    # Find the coords of the letters
                    if matrix[i][j] == letter_one:
                        letter_one_coords = (i, j)
                    if matrix[i][j] == letter_two:
                        letter_two_coords = (i, j)

                # If both coords have been found, do the build the cipher text
                # and break from the loop
                if letter_one_coords != (-1, -1) \
                        and letter_two_coords != (-1, -1):
                    # Same row
                    if letter_one_coords[0] == letter_two_coords[0]:
                        # Stay in same row, move 1 column right of first letter
                        col_to_move = letter_one_coords[1] - 1

                        # Wrap to column 0 if at the end
                        if col_to_move == -1:
                            col_to_move = 4

                        # Append letter right of first plain text
                        plain.append(
                            matrix[letter_one_coords[0]][col_to_move])

                        # Stay in same row, move 1 column right of second
                        # letter
                        col_to_move = letter_two_coords[1] - 1

                        # Wrap to column 0 if at the end
                        if col_to_move == -1:
                            col_to_move = 4

                        # Append letter right of second plain text
                        plain.append(
                            matrix[letter_one_coords[0]][col_to_move])

                    # Same column
                    elif letter_one_coords[1] == letter_two_coords[1]:
                        # Stay in the same column, move 1 row down of first
                        row_to_move = letter_one_coords[0] - 1

                        # Wrap to row 0 if at the end
                        if row_to_move == -1:
                            row_to_move = 4

                        # Append letter down of the first plain text
                        plain.append(
                            matrix[row_to_move][letter_one_coords[1]])

                        # Stay in the same column, move 1 row down of second
                        row_to_move = letter_two_coords[0] - 1

                        # Wrap to row 0 if at the end
                        if row_to_move == -1:
                            row_to_move = 4

                        # Append letter down of the second plain text
                        plain.append(
                            matrix[row_to_move][letter_two_coords[1]])

                    # Different row and column
                    else:
                        plain.append(
                            matrix[letter_one_coords[0]][letter_two_coords[1]])
                        plain.append(
                            matrix[letter_two_coords[0]][letter_one_coords[1]])
                    break

        # Join the plain text list to make the plain text string
        plain_text = "".join(plain)
        return plain_text
