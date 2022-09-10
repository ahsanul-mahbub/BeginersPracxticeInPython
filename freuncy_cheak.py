t = int(input())
for _ in range(t):
    n = map(int,input().split())
    lst = list(map(int,input().split()))
    for i in set(lst):
        print(i," ", lst.count(i))
    print()

# input
        5
        2
        5 9
        5
        1 5 5 5 9
        8
        2 5 5 2 9 9 9 12
        4
        12 12 18 18
        5
        12 15 10 5 9

# output
        9   1
        5   1

        1   1
        5   3
        9   1

        9   3
        2   2
        12   1
        5   2

        18   2
        12   2

        5   1
        9   1
        10   1
        12   1
        15   1
