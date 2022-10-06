# Write Faster Code ![Stars](https://img.shields.io/github/stars/Simpson-Computer-Technologies-Research/WriteFasterCode?color=brightgreen) ![Watchers](https://img.shields.io/github/watchers/Simpson-Computer-Technologies-Research/WriteFasterCode?label=Watchers)

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

# License
MIT License

Copyright (c) 2022 Tristan Simpson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
