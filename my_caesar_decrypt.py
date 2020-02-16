# Title: My Caesar Cipher - Decrypting 
# Context: Computational Thinking with Algorithms, GMIT, 2020
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 09-02-2020


def decr(cipher_text, offset):
    '''
    Decrypts the _cipher text_ by shifting the letters back (thus offset value in the code is negative) by _offset_ according to ASCII table.
    '''

    # create an empty string
    return_msg = ""

    for i in cipher_text:
        # loop for upper case letters only
        if ord(i) in range(65, 91):  # upper case letters in ascii are between 65(A) and 90(Z)
            num_value = ((ord(i) - offset - 65) % 26) + 65
            # update the decrypted message
            return_msg = return_msg + chr(num_value)

        # loop for lower case letters only
        elif ord(i) in range(97, 123):  # upper case letters in ascii are between 97(a) and 122(z)
            num_value = ((ord(i) - offset - 97) % 26) + 97
            # update the decrypted message
            return_msg = return_msg + chr(num_value)

        # loop for all other ASCII characters
        else:
            return_msg = return_msg + i  # update the decrypted message

    return print(return_msg)


# sample testing
decr("Bb Cc - Zz Aa", 1)  # expected return: Aa Bb - Yy Zz
