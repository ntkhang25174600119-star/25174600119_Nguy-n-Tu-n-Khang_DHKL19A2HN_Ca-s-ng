n = 10 
def fibonacci(): 
    global n 
    a = 0 
    b = 1 
    print(a, b, end="")
    
    count = 2 
    while count < n: 
        c = a + b
        a = b 
        b = c 
        count += 1 
fibonacci()