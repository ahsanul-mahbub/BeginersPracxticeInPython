t = int(input())
while(t>0):
    n = int(input())
    x = 0
    a = list(map(int,input().split()))
    for i in range(0,n-1):
     
        if (a[i] > a[i+1]):
            x = 1
            print("No")
            break
        
    if(x == 0): print("Yes")
    t -= 1   
    
    # https://www.codechef.com/START40D/problems/RATINGINPRAC
