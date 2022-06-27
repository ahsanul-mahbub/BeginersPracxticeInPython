a = input()
A = [1,2]
B = [2,2]
C = [4,8]
D = [8,8]
#middle dots distace
if 'middle dots distace' in a:
    x = (B[0] - A[0])**2
    y = (B[1] - A[1])**2
    AB = x + y
    for i in range (1,AB+2):
        if i ** 2 == AB:
            print(int(AB**0.5))
            break
    else:
        print(AB)
    x = (C[0] - B[0])**2
    y = (C[1] - B[1])**2
    BC = x + y
    for i in range (1,BC+2):
        if i ** 2 == BC:
            print(int(BC**0.5))
            break
    else:
        print(BC)
            
    x = (D[0] - C[0])**2
    y = (D[1] - C[1])**2
    CD = x + y
    for i in range (1,CD+2):
        if i ** 2 == CD:
            print(int(CD**0.5))
            break
    else:
        print(CD)
    x = (A[0] - D[0])**2
    y = (A[1] - D[1])**2
    AD = x + y
    for i in range (1,AD+2):
        if i ** 2 == AD:
            print(int(AD**0.5))
            break
    else:
        print(AD)
            
#of the ear /// korner 
    x = (C[0] - A[0])**2
    y = (C[1] - A[1])**2
    AC = x + y
    for i in range(1,AC+2):
        if i ** 2 == AC:
            print('of the corner',int(AC**0.5))
            break
    x = (C[0] - A[0])**2
    y = (C[1] - A[1])**2
    BD = x + y
    for i in range(1,BD+2):
        if i ** 2 == BD:
            print('of the corner',int(BD**0.5))
            break
    if AB == BC == CD == AD:
        print('Equilateral Square')
    
    
    
    else:
        print()
        
