
# Help received: All class materials, and I googled python syntax that I didn’t know

# a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

msg = "registrationisnowopenfortheeventwhichwillbeheldnextfridayregisterbytomorrowtobeenteredintoaraffleforagiftcardprize"
key = "compsxi"

# msg = "ballon"
# key = "monarchy"

msg_arr = []
for x in msg:
    msg_arr.append(x)
    
for x in range(len(msg_arr)):
    if x == 0:
        continue
    
    if msg_arr[x] == msg_arr[x - 1]:
        msg_arr.insert(x, 'a')

key_arr = []

for x in key:
    key_arr.append(x)
    
matrix = []

for x in key:
    a.pop(a.index(x))

a[len(a) - 1] = '?'
a[len(a) - 2] = '?'
        

def build_m():
    for y in range(5):
        row = []
        for x in range(5):
            if len(key_arr) > 0:
                row.append(key_arr.pop(0))
            else:
                row.append(a.pop(0))
        matrix.append(row)
        
def print_matrix():
    for x in matrix:
        print(x, "\n")
        
def encode_case_stacked(m, x1, y1, x2, y2):
    if x1 == 4 or x2 == 4:
        if x1 == 4:
            l1 = m[0][y1]
            l2 = m[x2 + 1][y2]
        else:
            l1 = m[x1 + 1][y1]
            l2 = m[0][y2]
    else:
        l1 = m[x1 + 1][y1]
        l2 = m[x2 + 1][y2]
    
    l = [l2, l1]
    return l
    
def encode_case_next_to(m, x1, y1, x2, y2):
    if y1 == 4 or y2 == 4:
        if y1 == 4:
            l1 = m[x1][0]
            l2 = m[x2][y2 + 1]
        else:
            l1 = m[x1][y1 + 1]
            l2 = m[x2][0]
    else:
        l1 = m[x1][y1  + 1]
        l2 = m[x2][y2 + 1]
    
    l = [l1, l2]
    return l
    
def encode_case_box(m, x1, y1, x2, y2):
    l1 = m[x1][y2]
    l2 = m[x2][y1]
    l = [l2, l1]
    return l
    
def find_index(m, k):
    for x in range(5):
        for y in range(5): 
            if m[x][y] == k:
                index = [x, y]
                return index
    index = [4, 4]
    return index

encoded_msg = []
def encode():
    p_c2 = ''
    while len(msg_arr) > 0:
        c1 = msg_arr.pop(0)
        try:
            c2 = msg_arr.pop(0)
            p_c2 = c2
        except:
            c2 = c1
            c1 = p_c2
        
        c1_index = find_index(matrix, c1)
        c2_index = find_index(matrix, c2)
        
        if c1_index[0] == c2_index[0]:
            n = encode_case_next_to(matrix, c1_index[0], c1_index[1], c2_index[0], c2_index[1])
            encoded_msg.append(n[0])
            encoded_msg.append(n[1])
        elif c1_index[1] == c2_index[1]:
            n = encode_case_stacked(matrix, c1_index[0], c1_index[1], c2_index[0], c2_index[1])
            encoded_msg.append(n[0])
            encoded_msg.append(n[1])
        else:
            n = encode_case_box(matrix, c1_index[0], c1_index[1], c2_index[0], c2_index[1])
            encoded_msg.append(n[0])
            encoded_msg.append(n[1])


build_m()

print_matrix()

encode()

final = ""
for x in encoded_msg:
    final = final + x

print(final)