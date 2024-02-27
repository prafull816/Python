# Loops in Python
"""
loops are used to repeat instructions.


"""

# While loops
# while condition:
    #same work

count=1
while count <=5 :
 
 print("hello",count)
 count += 1
# print("hello")
# print("hello") 
# print("hello")
# print("hello")
 

# Break and Continue
 """
 Break : used to terminate the loop when encountered.
 Continue : Terminates execution in the current iteration and continues execution of the loop with the next iteration.

 """
num = (1,2,4,53,56,78,97,96,35,73,4,7,8)
print(num)
x=96
idx = 0
while idx < len(num):
    if(num[idx]==x):
        print("found at index",idx)
        break
    else:
        print("Finding...")
    idx +=1



x = 0 
while x <=5:
   if(x==3):
      x += 1
      continue
      print(x)
      x  += 1
 



 # # Range() Function
      

      # Range functions returns a sequence fo numbers, starting from 0 by default and increments by 1(by default), and stops before a specified number.

      # range(start?, stop,step?)

seq = range(5)
for seq in range(5):
 print(seq)

for el in range(1,5):
 print(el)

for el in range(1,5,2):
 print(el)






 # Pass Statement in loops

 # Pass in a null statement that does notjing. it is used as a placeholder for future code.
 # for el  in range(10):
 # pass


for i in range(5):
  pass
  print("Some useful work")


# we can use pass steatment in if statement

for i in range(5):
  pass
if i<5:
  pass
print("Some useful work")

