# Clayton Smiley - 9/28/2018
# MCS260 project1:
# encryption and decryption of a string
# reminder to self: turn in a .txt file



def encryption(S, n):
    placeholder = ""
    for character in S:
        if character != '' and character != ' ':
            encoded = ord('a') + ((ord(character)-ord('a')+n) % 26)
            placeholder += chr(encoded)
        else:
            placeholder += " "

    placeholder += str(n)

    return placeholder


def decryption(W):
    last_number = int(W[-1])  # last index of given word
    W = W[0:-1]  # pop the number off of the string
    placeholder = ""
    for character in W:
        if character != '' and character != ' ':
            decoded_char = ord('a') + ((ord(character)-ord('a')-last_number + 26) % 26)
            character = chr(decoded_char)
            placeholder += character
        else:
            #  this else case only executes if it is a space character
            placeholder += " "
    return placeholder


def main():
    print(encryption("hello world", 9))
    a = encryption("hello world", 1)
    print(decryption(a))


main()
