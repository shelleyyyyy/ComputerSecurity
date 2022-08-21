
# Help received: All class materials, and I googled python syntax that I didn’t know

code = "registrationisnowopenfortheeventwhichwillbeheldnextfridayregisterbytomorrowtobeenteredintoaraffleforagiftcardprize"
# key = "VMICIS"
key = "vmicis"

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
default = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

def shift(sh):
    for x in range(len(num)):
        old = num[x]
        new = old - sh
        
        if new < 0:
            new = new + 26
            
        num[x] = new
        
def find_shift(char):
    shift(a.index(char))
        
    

def make_key():
    global key, code
    # key = code
    while True: 
        if len(key) < len(code):
            key = key + key
        else:
            break


def encode():
    global key, code, default, num
    make_key()
    answer = ""
    for x in range(len(code)):
        find_shift(key[x])
        # print(num)
        aIndex = a.index(code[x])
        numIndex = num.index(aIndex)
        answer = answer + a[numIndex]
        num = default
    print(answer)
    

encode()