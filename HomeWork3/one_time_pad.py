from operator import xor

# Help Recieved Cole Corson, Cameron Miller, Googled Python Syntax 

def one_time_pad(code, key):
    pt = ""
    i = 0
    for x in code:       
        pt = pt + chr(xor(ord(x), ord(key[i])))
        if i == (len(key) - 1):
            i = i - len(key)
        i = i + 1
        
    return pt;


key = "ABCDEFGHIJKL"
code = "VOL QLY GU UD UGRSKL GVU"

print(one_time_pad(code, key))
