code = "GL"
key = "IE"

arr = []
for i in range(len(code)):
    diff = abs(ord(code[i]) - ord(key[i]))
    arr.append(diff)
    
print(arr)

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ans = ""

for x in arr:
    ans = ans + alpha[x]
    
print(ans)