# WAP to check idf a number entered by the user is odd or even.

num = int(input("Enter the number : "))
print(num)
rem = num % 2
if(rem % 2 == 0):
    print("number is even")
else:
    print("Number is odd")