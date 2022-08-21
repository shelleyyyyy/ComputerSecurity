


import binascii


def make_keys(key):
    key = bin(int(binascii.hexlify(key),16))
    
    print(key)
    
make_keys("vmi")