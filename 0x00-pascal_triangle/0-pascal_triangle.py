#!/usr/bin/python3
"""pascal Triangle"""

def pascal_triangle(n):

    #iterate through every line and print entries in it.
    for line in range(0, n):

        for i in range(0, line + 1):
            print(binomialCoeff(line , i), " ", end = "")
        print()

def binomialCoeff(n, k) :
    res = 1
    if (k > n - k):
        k = n -k
    for i in range(0, k):
     res = res * (n - i)
     res = res // (i + 1)

    return res

n = 7
pascal_triangle(n)
