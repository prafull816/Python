# Function in Python

"""
Block of statement that perform a specific task.
def fun_name(param1,param2...):
# some work 
returnval 
func_name(org1,org2...): # function call


Ex. 

def sum(a,b):
s = a+b
return s

print(sum(2,3))

"""

# a = 6 
# b = 7
# sum = a + b
# print(sum)

# # more line of code
# a = 6 
# b = 9
# sum = a + b
# print(sum)

# #more line of code

# a = 3
# b = 7
# sum = a + b
# print(sum)


# function

def cal_sum(a,b):
 sum = a+b
 print(sum)
 return sum

cal_sum(55,45)


cal_sum(10,20)


# Function 

def calc_sum(a,b,c):
 return a+b+c

sum1 = calc_sum(1,5,8)
print(sum1)


# Types of Function 
"""
1] Built-in Function
Ex.
len()
type()
range()


2] User defined Function

"""




# defualt parameter

def cal2_prod(a,b=15):
 print(a*b)
 return a*b

cal2_prod(5)