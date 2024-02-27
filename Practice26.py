# WAP to find the factorial of first n numbers. (using for)


n = 6
fact = 1
i = 1
while i <= n:
 fact *= i
 i += 1
print("Factorial = ", fact)

#using for loop

n = 5
fact = 1
for i in range(1, n+1):
 fact *= i
print("factorial is",fact) 