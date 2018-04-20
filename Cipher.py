###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: Cipher.py                                                        #
# Description: This is the driver file. Its function is to read in the        #
#              options from the command line and then use the information to  #
#              determine which cipher to operate with.                        #
###############################################################################

import CipherInterface
import Caesar
import Railfence
import Vigenre
import Playfair
import RowTransposition
import argparse

# Creates a parser to allow us to handle command line arguments
parser = argparse.ArgumentParser(description="Encrypt or decrypt a file")
parser.add_argument("-c", "--cipher", help="cipher to use")
parser.add_argument("-k", "--key", help="key to use")
parser.add_argument("-e", "--encrypt", help="encrypt mode")
parser.add_argument("-d", "--decrypt", help="decrypt mode")
parser.add_argument("-o", "--out_file", help="name of new file")
args = parser.parse_args()

CIPHER = CipherInterface.CipherInterface()


def handle_input(cipher, key, in_file, out_file, mode):
    # Standardize the cipher
    the_cipher = cipher.lower()

    # Try to open files specified
    try:
        input_file = open(in_file, "r")
        output_file = open(out_file, "w")

        text = input_file.read()
        input_file.close()
    except IOError:
        # If there was an error opening the file, abort
        print("Error opening file")
        return

    # Execute Caesar cipher
    if the_cipher == "caesar":
        CIPHER = Caesar.Caesar()

        if CIPHER.set_key(key):
            if mode == "e":
                print("Using Caesar cipher to encrypt: {}".format(in_file))
                encrypt = CIPHER.encrypt(text)
                output_file.write(encrypt)

            elif mode == "d":
                print("Using Caesar cipher to decrypt: {}".format(out_file))
                decrypt = CIPHER.decrpyt(text)
                output_file.write(decrypt)

            output_file.close()
        else:
            print("Key: \"{}\" is not a valid key.\n "
                  "No encryption will occur.".format(key))

    # Execute Playfair cipher
    elif the_cipher == "playfair":
        CIPHER = Playfair.Playfair()

        if CIPHER.set_key(key):
            CIPHER.construct_key_matrix(key)
            if mode == "e":
                print("Using Playfair cipher to encrypt: {}".format(in_file))
                encrypt = CIPHER.encrypt(text)
                output_file.write(encrypt)

            elif mode == "d":
                print("Using Playfair cipher to decrypt: {}".format(out_file))
                decrypt = CIPHER.decrpyt(text)
                output_file.write(decrypt)

            output_file.close()
        else:
            print("Key: \"{}\" is not a valid key.\n "
                  "No encryption will occur.".format(key))

    # Execute Railfence cipher
    elif the_cipher == "railfence":
        CIPHER = Railfence.Railfence()

        if CIPHER.set_key(key):
            if mode == "e":
                print("Using Railfence cipher to encrypt: {}".format(in_file))
                encrypt = CIPHER.encrypt(text)
                output_file.write(encrypt)

            elif mode == "d":
                print("Using Railfence cipher to decrypt: {}".format(out_file))
                decrypt = CIPHER.decrpyt(text)
                output_file.write(decrypt)

            output_file.close()
        else:
            print("Key: \"{}\" is not a valid key.\n "
                  "No encryption will occur.".format(key))

    # Execute Row Transposition cipher
    elif the_cipher == "rowtransposition":
        CIPHER = RowTransposition.RowTransposition()

        if CIPHER.set_key(key):
            if mode == "e":
                print("Using Row Transposition cipher to encrypt: {}"
                      .format(in_file))
                encrypt = CIPHER.encrypt(text)
                output_file.write(encrypt)

            elif mode == "d":
                print("Using Row Transposition cipher to decrypt: {}"
                      .format(out_file))
                decrypt = CIPHER.decrpyt(text)
                output_file.write(decrypt)

            output_file.close()
        else:
            print("Key: \"{}\" is not a valid key.\n "
                  "No encryption will occur.".format(key))

    # Execute Vigenre cipher
    elif the_cipher == "vigenre":
        CIPHER = Vigenre.Vigenre()

        if CIPHER.set_key(key):
            CIPHER.build_rows()
            if mode == "e":
                print("Using Vigenre cipher to encrypt: {}".format(in_file))
                encrypt = CIPHER.encrypt(text)
                output_file.write(encrypt)

            elif mode == "d":
                print("Using Vigenre cipher to decrypt: {}".format(out_file))
                decrypt = CIPHER.decrpyt(text)
                output_file.write(decrypt)

            output_file.close()
        else:
            print("Key: \"{}\" is not a valid key.\n "
                  "No encryption will occur.".format(key))

    # User didn't enter a correct cipher
    else:
        print("Unknown cipher entered...")

# Handles argument input
if args.encrypt is not None and args.decrypt is not None:
    # User entered -e and -d, cant do both at once
    print("You need to choose encryption or decryption!")

elif args.encrypt is not None and \
                args.cipher is not None and \
                args.key is not None and \
                args.out_file is not None:
    # User entered all the proper info for encryption

    handle_input(args.cipher, args.key, args.encrypt, args.out_file, "e")
elif args.decrypt is not None and \
                args.cipher is not None and \
                args.key is not None and \
                args.out_file is not None:
    # User entered all the proper info for decryption

    handle_input(args.cipher, args.key, args.decrypt, args.out_file, "d")
else:
    # Some piece of info was missing
    print("You messed up somewhere... Try again.")
