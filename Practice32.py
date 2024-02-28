#  Write a recursive function to print all element in alist 
# hint : use list and index as paramer=ters.


def print_list(list,idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","banana","apple"]
print_list(fruits)