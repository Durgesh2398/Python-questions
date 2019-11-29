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

#-------------------------------------------------
# Program to print full pyramid
num_rows = int(input("Enter the number of rows"))
for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
        print(end=" ")
    for j in  range(0, i+1):
        print("*", end=" ")
    print()

#------------------------------------------------
    #Program to print Left Half Pyramid
num_rows = int(input("Enter the number of rows"))
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()

#------------------------------------------------
#Program to print Right Half Pyramid
num_rows = int(input("Enter the number of rows"))
k = 8
for i in range(0, num_rows):
    for j in range(0, k):
        print(end=" ")
        k = k - 2
for j in range(0, i+1):
    print("* ", end="")
print()

#---------------------------------------------
# Program to print One More Star Pattern Pyramid
print("Program to print star pattern: \n")
rows = input("Enter maximum stars you want display on a single line")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
    for i in range (rows, 0, -1):
        for j in range(0, i -1):
            print("* ", end='')
        print("\r")


#---------------------------------------------
print("Program to print star pattern in different style: \n")
num_rows = int(input('Please enter the number of rows'))
for i in range (0,num_rows):
    for j in range (num_rows,i,-1):
        print("* ", end="")
    print()


#---------------------------------------------
num_rows = int(input("Please enter the number of rows"))
for i in range(num_rows,0,-1):
    for j in range(0, num_rows-i):
        print(end=" ")
for j in range(0,i):
    print("* ", end=" ")
print()


#-----------------------------------------------
for row in range(7):
    for col in range(5):
        if ((col==0 or col ==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()