# Set in python 
"""
Set is the collection of the unordered items.
Each element in the set must be unique and immutable.


nums = { 1,2,3,4}
set2 = {1,2,2,2}
# repeated elements stored only once, so it resolved to{1,2}
null_set = set()  # empty set syntax



#IMP Set are ignored dublicate value 
"""



collection = { 1,2,3,4,1,2,3,5,67,78,}
print(collection)
print(type(collection))
print(len(collection))


#Create Empty set

collection1 = set()  #empty set; Syntax
print(type(collection1))


# SET METHODS

# set.add(element) # adds an element
# set.remove(el) # remove an element 
# set.clear() # emppties the st 
# set.pop() # removes a random value
# set.union(set2) # combines both set values and returns new
# set.intersection(set2) # combines commman value and return new
# There are multiple method googel it

collection2 = set()
collection2.add(1)
collection2.add(3)
collection2.add(2)
collection2.add("Prafull")
print(collection2)


collection2.remove(1)
print(collection2)

collection2.clear()
print(collection2)

