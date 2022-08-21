
# Help Recieved Cole Corson, Cameron Miller, Googled Python Syntax 

def encrypt(key, pt):

    si = ["000", "001", "010", "011", "100", "101", "110", "111"]

    sb1 = [
        ["101", "010", "001", "110", "011", "100", "111", "000"],
        ["001", "100", "110", "010", "000", "111", "101", "011"]
    ]

    sb2 = [
        ["100", "000", "110", "101", "111", "001", "011", "010"],
        ["101", "011", "000", "111", "110", "010", "001", "100"]
    ]

    l0 = ""
    r0 = ""

    for x in range(len(pt)):
        if x > ((len(pt) / 2) - 1):
            r0 = r0 + pt[x]
        else:
            l0 = l0 + pt[x]
            

    def expand(r0):
        r1 = r0[0]
        r1 = r1 + r0[1]
        r1 = r1 + r0[3]
        r1 = r1 + r0[2]
        r1 = r1 + r0[3]
        r1 = r1 + r0[2]
        r1 = r1 + r0[4]
        r1 = r1 + r0[5]
        
        return r1

    def xor(n1, n2):
        n3 = ""
        for x in range(len(n1)):
            if n1[x] != n2[x]:
                n3 = n3 + "1"
            else:
                n3 = n3 + "0"
                
        return n3;


    e = expand(r0)

    xe = xor(e, key)

    s0 = ""
    s1 = ""

    for x in range(len(xe)):
        if x < (len(xe) / 2):
            s0 = s0 + xe[x]
        else:
            s1 = s1 + xe[x]


    y1 = int(s0[0])
    x1 = s0[1] + s0[2] + s0[3]
    x1i = si.index(x1)

    y2 = int(s1[0])
    x2 = s1[1] + s1[2] + s1[3]
    x2i = si.index(x2)



    r1 = sb1[y1][x1i] + sb2[y2][x2i]

    r1 = xor(r1, l0)

    l1 = r0

    return(l1 + r1)

def decrypt(key, pt):
    
    si = ["000", "001", "010", "011", "100", "101", "110", "111"]

    sb1 = [
        ["101", "010", "001", "110", "011", "100", "111", "000"],
        ["001", "100", "110", "010", "000", "111", "101", "011"]
    ]

    sb2 = [
        ["100", "000", "110", "101", "111", "001", "011", "010"],
        ["101", "011", "000", "111", "110", "010", "001", "100"]
    ]

    l0 = ""
    r0 = ""


        
    for x in range(len(pt)):
        if x > ((len(pt) / 2) - 1):
            l0 = l0 + pt[x]
        else:
            r0 = r0 + pt[x]
            

    def expand(r0):
        r1 = r0[0]
        r1 = r1 + r0[1]
        r1 = r1 + r0[3]
        r1 = r1 + r0[2]
        r1 = r1 + r0[3]
        r1 = r1 + r0[2]
        r1 = r1 + r0[4]
        r1 = r1 + r0[5]
        
        return r1

    def xor(n1, n2):
        n3 = ""
        for x in range(len(n1)):
            if n1[x] != n2[x]:
                n3 = n3 + "1"
            else:
                n3 = n3 + "0"
                
        return n3;


    e = expand(r0)


    xe = xor(e, key)

    s0 = ""
    s1 = ""

    for x in range(len(xe)):
        if x < (len(xe) / 2):
            s0 = s0 + xe[x]
        else:
            s1 = s1 + xe[x]


    y1 = int(s0[0])
    x1 = s0[1] + s0[2] + s0[3]
    x1i = si.index(x1)

    y2 = int(s1[0])
    x2 = s1[1] + s1[2] + s1[3]
    x2i = si.index(x2)



    r1 = sb1[y1][x1i] + sb2[y2][x2i]

    r1 = xor(r1, l0)

    l1 = r0

    return(l1 + r1)
    

key = "110011000"
pt = "101011111010"
keys = ["11001100", "01100110", "00110011", "00011001"]

def rounds_e(pt, keys):
    for x in keys:
        new_pt = encrypt(x, pt)
        pt = new_pt
        
    return pt

def rounds_d(pt, keys):
    for x in reversed(keys):
        new_pt = decrypt(x, pt)
        pt = new_pt
        
    return pt

e = rounds_e(pt, keys)
d = rounds_d(e, keys)

print("plain text:", pt)
print("encrypted: ", e)
print("decrypted: ", d)


