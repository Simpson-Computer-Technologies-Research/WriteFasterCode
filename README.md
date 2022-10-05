# Good practices for writing fast code! ![Stars](https://img.shields.io/github/stars/Simpson-Computer-Technologies-Research/Python-WriteFasterCode?color=brightgreen) ![Watchers](https://img.shields.io/github/watchers/Simpson-Computer-Technologies-Research/Python-WriteFasterCode?label=Watchers)

```py
# // Time libarary
import time

# // Global Variables
x, y, n, m = (True,)*4

```

# Slow Function
```py
def slow():
    """
    This function has an average of being 4.15 seconds slower 
    (average at 11.25 seconds)
    """
    r = 0
    start = time.time()
    
    # // 100,000,000 Iterations
    for _ in range(10**8):
        if x != False:
            if n == True and m == True:
                r+=1
                    
            if m  == True:
                r+=1
    print("\n - Slow: "+str(time.time()-start) +" -> "+str(r)+"r")

```

# Fast Function
```py
def fast():
    """
    This function has an average of being 4.15 seconds faster
    (average at 7.10 seconds)
    """
    r = 0
    start = time.time()
    
    # // Just return if not x
    if not x:
        return
    
    # // 100,000,000 Iterations
    for _ in range(10**8):
        if m:
            r+=1
            if n:
                r+=1
    print(" - Fast: "+str(time.time()-start) +" -> "+str(r)+"r")
```
