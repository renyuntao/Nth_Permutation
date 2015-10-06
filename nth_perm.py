#!/usr/bin/env python
import math
def Nth_Perm(nth,num,arr):   #nth = The n'th permutation,num = the length of arr
    n = nth
    e = num
    temp = []
    while len(arr) != 0:
        division = math.factorial(e)/e
        pos = math.ceil(n/division)
        t = arr[pos-1]
        temp.append(t)
        e = e - 1
        arr.remove(t)
        oldDivision = division
        n = n - (oldDivision*(pos-1))
    ans.append(''.join(temp))

############### Example ##################
seq = ['A','B','C','D']
ans = []
Nth_Perm(3,4,seq)
print(*ans)
