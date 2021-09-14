x = 1
a = 5
b = 5

while x <= b:
    y = 1
    while (y <= a):
        if(x >= y):
            print(y,"",end="")
        y = y + 1
    print()
    x = x + 1
    
#Output
#1
#1 2
#1 2 3 
#1 2 3 4 
#1 2 3 4 5
