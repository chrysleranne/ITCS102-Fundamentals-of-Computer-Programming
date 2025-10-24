c = 6
for a in range(1, c+1):
    print("  " * (c - a), end="")  
    
    for j in range(a, 1, -1):
        print(j, end=" ")
    print("1", end=" ")
    
    for k in range(2, a+1):
        print(k, end=" ")
    print() 
