def suma(n):
    
    if n == 1:
        s = 1
    else:
        s = n + suma(n-1)
    
    return s

print(suma(100))