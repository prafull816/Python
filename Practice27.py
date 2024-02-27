# WAF to print the lenght of a list.(list is the paramerter)

list = ["a","c","f","r","s",]
list2 = ["a","c","f","r","s","j","r"]

def print_len(list):
    print(len(list))

    print_len(list)
    print_len(list2)

