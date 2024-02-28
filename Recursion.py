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


# def show(n):
#  if(n == 0):
#   return
#   print(n)
#  show(n-1)

#  show(5)


def fact(n):
    if(n==1 or n==0):
        return 1
        return fact(n-1) * n
    print (fact(6))

    