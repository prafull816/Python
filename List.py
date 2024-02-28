"""
List in Python
A built-on data type that stores set of 
it can store elements of different types(integer, float, string, etc.)

marks = [80,41,87,94,93,56]  # marks[0], marjs[1]...
student = ["Karan", 85,"Delhi"] # student[0], student[1]...
student[0]="Arjun" # allowed in puthon
len(student)  #returns length
"""



marks = [80,98,79,67,90,89,86]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1]) 


student = ["Prafull",7875789496,"prafullwahatule@gmail.com"]
print(student[0])



#   List Slicing
"""
list_name[starting_idx : ending_idx] # ending idx is not included

marks[ 80,56,48,89,49,50]
marks[1:4] is [56,48,89,49]
marks[:4] is same as marks[0:4] 
marks[1:]is same as marks [1 : len(marks)]
marks[-3:-1] is [89,49,50]


"""

marks1 = [80,56,48,89,49,50]
print(marks1)
print(marks1[1:4])
print(marks1[:4])
print(marks1[1:])
print(marks1[-3:-1])




#List Methods
"""
list = [2,1,4]
list.append(4) # adds one elements at the end) [ 2,1,4,4]
list.sort () # sorts in ascending order [1,2,4]
list.sort(reverse=True) # sortsin descending order [4,2,1]
list.reberse() # reverses list [4,1,2] 
list.insert(idx, el) # insert element at index
list.remove(1) 

"""

list = [2,1,4]
print(list.append(4))
print(list.sort ())
print(list.sort(reverse=True))
print(list.reberse())
print(list.insert([0],[3]) )





