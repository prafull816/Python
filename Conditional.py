
# indentation = proper spacing in python
"""
1] if-elif-else
Syntac:

if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN

"""
age = int(input("age : "))
print(age)

if(age>=18):
    print("You are Eligible for Voting.")

elif(age<18):
    print("You are not Eligible for Voting.")
else:
    print("You are child.")


# Traffic light code
    
light = input("light : ")
if(light == "red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yello"):
    print("Look")
else:
    print("Light is broken")



# Grades of students
marks = int(input("marks: "))
print("marks is : ", marks)

if(marks>=95):
    print("Congrats you got gread A")

elif(marks>=80):
    print("Congrats you got gread B")

elif(marks>=60):
    print("Congrats you got gread C")

elif(marks>=40):
    print("Congrats you got gread D")

else:
    print("Fail")



"""
single line if / ternary operator
Syntax:
<var> = <val1> if <condition>else<val2>

food = input ("food: "):
eat = "yes" if food == "cake" else "no"
print(eat)


Syntax:
<stt1>if<c0ondition>else<stt2>
food = input ("food :")
 print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")
"""

food = input("food: ")
eat = "yes" if food == "cake" else "no"
print(eat)

food = input ("food :")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


# Clever if / Ternary Operator 
# Syntax:
# <var> = (false_val, true_val)[<condition>]

age = int(input("age : "))
vote = ("yes", "no")[age>=18]


#

sal  = float(input("salary :"))
tax = sal*(0.1,0.2)[sal<=50000]
print(tax) 




# Nestedn if else

if(age>=18):
    if(age>=80):
        print("Cannot drive")
    else:
        print("can drive")
else:
    print("Cannot drive")