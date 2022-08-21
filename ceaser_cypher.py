# shift cipher
# define encrypt and decrypt functions

def encrypt(str):
    # define alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # define shift
    shift = 3
    # define new string
    new_str = ""
    # loop through string
    for char in str:
        # if char is in alphabet
        if char in alphabet:
            # find index of char in alphabet
            index = alphabet.find(char)
            # add shift to index
            index += shift
            # if index is greater than 26
            if index > 26:
                # subtract 26 from index
                index -= 26
            # add char at index to new string
            new_str += alphabet[index]
        # if char is not in alphabet
        else:
            # add char to new string
            new_str += char
    # return new string
    return new_str


# def decrypt function to decrypt
def decrypt(str):
    # define alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # define shift
    shift = 3
    # define new string
    new_str = ""
    # loop through string
    for char in str:
        # if char is in alphabet
        if char in alphabet:
            # find index of char in alphabet
            index = alphabet.find(char)
            # subtract shift from index
            index -= shift
            # if index is less than 0
            if index < 0:
                # add 26 to index
                index += 26
            # add char at index to new string
            new_str += alphabet[index]
        # if char is not in alphabet
        else:
            # add char to new string
            new_str += char
    # return new string
    return new_str




e = "william shelley"

e = encrypt(e)

print(e)
print(decrypt(e))
