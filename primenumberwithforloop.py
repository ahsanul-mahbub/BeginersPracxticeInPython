a = int(input("Enter a number : "))
for i in range(2,a):
    if a % i == 0:
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
    
    
    
'''
___________________
output
Enter a number : 7
It is a prime number 


Enter a number : 6
It is not a prime number 
