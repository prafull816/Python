#WAF to print the elements of a list in a single line.(list is the parameter)


list = [1,2,3,4,5,9,8,7,6,5,4]

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(list)
print()