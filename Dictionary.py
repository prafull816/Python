# Dictionary in Python

""""
Dictionaries are used to store data  valuesin key:value pairs 
They are unordered, mutable(changeble) and don't allow duplicate keys 

Ex. 

dict = {

"name" : "Prafull"
"grade" : "A"
"marks" : [98,78,80]
}


dict["name], dict["grade"], dict["marks"]
dict["key"]= "value" # to assign or add new

"""

dict = {

    "name" : " Prafull Wahtule",
    "sub" : ["Python","C","Java"],
    "topic" : ("dict", "Set"),
    "age" : 22,
    "marks" : 92.40
}
print(dict["name"])
print(dict["sub"])
print(dict["topic"])
print(dict["age"])
print(dict["marks"])



# Nested Dictionaries


student = {

    "name" : "Prafull Wahatule",
    "sub" : {
        "phy" : 98,
        "math" : 90,
        "chem" : 65

    }
}

print(student)




# Dictionaries Methods


# There are multiple methods your can work on it 

student1 = {

    "name" : "Prafull Wahatule",
    "sub" : {
        "phy" : 98,
        "math" : 90,
        "chem" : 65

    }
}

print(len(student1))
print(list(student1))



