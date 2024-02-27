# String and numeric balues can operate together with *

# a,b=2,3
# txt="@"
# print(2*txt*3)


# string and string can operate with *

A,B="2",3
txt="@"
print((A+txt)*B)

# Numeric values can operate with all arithmetic operators


A,B=2,3
C=4
print(A+B*C)


# Arithmetic exepression with integer and float will result in float


A,B=10,3
C=A*B
print(C)

# Result of division operator with two integers will be float


A,B=2.2,3
C=A//B
print(C, A/B)

# Floor gives closest integer, which is lesser than or equal to the float value 
# REsult of (A//B) is same as floor(A/B)


A,B=12,5
C=A//B
print(C)

A,B=-12,5
C=A//B
print(C)

A,B=12,-3
C=A//B
print(C)



#  REMAINDER IS NEGATIVE WHEN DENOMINATOR IS NEGATIVE

A,B=-5,2
C=A%B
print(C)

A,B=5,2
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C)



