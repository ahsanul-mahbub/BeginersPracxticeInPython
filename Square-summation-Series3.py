a = -1
b = 0
sum = 0
while( a < 9):
    a = a + 2
    b = a**2
    sum = sum + b
    if(b < 81):
        print(b,"+", end=" ")
    else:
        print(b, "", end=" ")
print("\nSum =",sum,end="")


# 1**2 + 3**2 + 5**2 + 7**2... + = ?
