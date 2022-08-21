
# answer
# CYBERDEFENSEFUNDAMENTALS : shift 19

# Help received: All class materials, and I googled python syntax that I didn’t know

# code = "zlooldp vkhoohbn"
code = "ZLOOLDPVKHOOHBN"

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def shift(sh):
    for x in range(len(num)):
        old = num[x]
        new = old + sh
        
        if new > 25:
            new = new - 26
            
        num[x] = new
    
def decrypt():
    bool = input("Is the shift value known? (y/n): ")
    
    if bool == 'n':
        for s in range(26):
            answer = ""
            for x in code:
                try:
                    alphaIndex = alpha.index(x)
                    numIndex = num.index(alphaIndex)
                
                    answer = answer + alpha[numIndex]
                except:
                    answer = answer + '?'
                
            print(answer, ": shift-", s)
            
            shift(1)
    else:
        s = input("Enter the shift: ")
        shift(int(s))
        answer = ""
        for x in code:
            alphaIndex = alpha.index(x)
            numIndex = num.index(alphaIndex)
            
            answer = answer + alpha[numIndex]
            
        print(answer, ": shift-", s)
        
        
decrypt()
