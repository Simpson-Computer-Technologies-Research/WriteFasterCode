# // Good practices for writing fast code!

# // Import time libarary
import time

# // Declare the variables
x, y, n, m = (True,)*4

# // The supposed "Slower" function
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


# // The supposed "Faster" function
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


# Call the functions
if __name__ == "__main__":
    print(" >> Starting... This may take a moment...")
    slow()
    fast()
    print("""
        As you can see the fast() function is mucher faster than the slow() one because
        the fast() function managed it's statements better
        """)  
