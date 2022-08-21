
arr = [1, 2, 3, 4, 6, 12, 103, 206, 309, 412, 618, 1236]

# arr2 = []

# for x in arr:
#     arr2.append(pow(5, x))
    
# arr3 = []

# for x in arr2:


    
#     arr3.append(x % 1237)
    
# print(arr3)



for x in arr:
    z = pow(5, x)
    y = z % 1237
    print("5^", x, "= ", z, y)
    print("mod 1237 = ", y)