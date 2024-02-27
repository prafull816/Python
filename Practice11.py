# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list = [1,2,3,4,3,2,6]
list2 = [1,2,3,4]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrom")
else:
    print("Not Palindrom")

     