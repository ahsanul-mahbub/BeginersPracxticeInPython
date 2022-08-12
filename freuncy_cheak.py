t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    lst = list(map(int,input().split()))
    x = (lst.count(a)/n)*(lst.count(b)/n)
    print(x)
