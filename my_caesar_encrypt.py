# Title: My Caesar Cipher - Encrypting
# Context: Computational Thinking with Algorithms, GMIT, 2020
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 09-02-2020


def encr(plain_text, offset):
    '''
    Encrypts the _plain text_ by shifting the letters by _offset_ according to ASCII table.
    '''

    cipher_msg = ""  # creation of empty string

    for i in plain_text:
        # loop for upper case letters only
        if ord(i) in range(65, 91):  # upper case letters in ascii are between 65(A) and 90(Z)
            num_value = ((ord(i) + offset - 65) % 26) + 65
            # update the encrypted message
            cipher_msg = cipher_msg + chr(num_value)

        # loop for lower case letters only
        elif ord(i) in range(97, 123):  # upper case letters in ascii are between 97(a) and 122(z)
            num_value = ((ord(i) + offset - 97) % 26) + 97
            # update the encrypted message
            cipher_msg = cipher_msg + chr(num_value)

        # loop for all other ASCII characters
        else:
            cipher_msg = cipher_msg + i  # update the encrypted message

    return print(cipher_msg)


# sample testing
encr("Aa Bb - Yy Zz", 1)  # Expected return: Bb Cc - Zz Aa
