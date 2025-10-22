""" def greet():
        print("Sushant")
        greet()  # Recursive call
    greet()"""

#if you run the above code, you will get the following error:
"""greet()  # Recursive call
    ~~~~~^^
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded"""

                                         #Head Recursion
def greet(count=0):
    if count == 4:
        return
    print("Sushant")
    greet(count + 1)  # Recursive call with incremented count

greet()



