a,b= map(int, input().split())
if ( a> 12 or b > 60 or a < 0 or b < 0):
	print("input is wrong")
if a == 12:
	a = 0
if b == 60 :
	b = 0
c = 0.5*(a*60+b)
d=6*b
e = c - d
e = min(360-e,e)
print(e)
