
A = [1,8,3,2,9,5,6,7,4]
print(A)
print(A[3])
print(A[1:4])
print(A[-2])

A.pop(3)
print("pop ",A)

A.remove(1)
print("Remove = ",A)

A.sort()
print("Sort : ",A)

A.reverse()
print("reverse : ",A)

A.append(10)
print("Append : ",A)

A.insert(2,11)
print("insert : ",A)
