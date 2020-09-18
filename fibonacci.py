# fibonacci iteration
# TCA - O(n)
def fibIter(n):
    if n == 0:
        return
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib1 = 0
    fib2 = 1
    fib = 1
    while n >= 2:
        fib = fib1 + fib2
        fib2 = fib1
        fib1 = fib
        n= n-1
    return fib
    
n = fibIter(10)
print(n)
        
# fibonacci Recursion
# TCA - O(2^n)        
def fibRec(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibRec(n-1) + fibRec(n-2)
        
    
n = fibRec(10)
print(n)
        