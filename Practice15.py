# WAP to enter marks of 3 subjects form the user and store them in  a dictionar.
# Start with an empty dictionary and one bu one. Use subject name as key and marks as value.


marks = {}

a = int(input("enter phy : "))
marks.update({"phy" : a})

a = int(input("Enter math : "))
marks.update({"math" : a})

a = int(input("Enter chem : "))
marks.update({"chem" : a})

print(marks)