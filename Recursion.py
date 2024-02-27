"""
Recursion

when a function calls itself repeatedly.
# prints n to 1 backwards

def show(n):
if(n == 0):
return
print(n)
print(n-1)

"""


def show(n):
    print(n)
    show(n-1)


show(5)