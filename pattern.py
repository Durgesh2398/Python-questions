for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()

size = 15
for a in range(int(size / 2), size + 1, 2): 
    for b in range(1, size - a, 2):  
        print(" ", end = "") 
    for b in range(1, a + 1): 
        print("*",end="") 
    for b in range(1, (size - a) + 1): 
        print(" ", end = "") 
    for b in range(1, a): 
        print("*", end = "") 
    print("") 
for a in range(size, -1, -1): 
    for b in range(a, size): 
        print(" ", end = "") 
    for b in range(1, (a * 2)): 
        print("*", end = "") 
    print("")