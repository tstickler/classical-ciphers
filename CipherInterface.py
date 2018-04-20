###############################################################################
# Programmer: Tyler Stickler                                                  #
# File name: CipherInterface.py                                               #
# Description: Parent class for all the ciphers to inherit from.              #
###############################################################################

class CipherInterface:
    def __init__(self):
        self.data = []

    def set_key(self, key):
        return False

    def encrypt(self, plain_text):
        return ""

    def decrpyt(self, cipher_text):
        return ""
