# WAP to find the greatest of 3 numbers entered by the user.

num1 = input ("Enter the First No : ",)
num2 = input ("Enter the second No : ")
num3 = input ("Enter the third No : ")

print(num1,num2,num3)

if(num1>num2 and num1>num3):
    print("num1 is greatest")
elif(num2>num1 and num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")