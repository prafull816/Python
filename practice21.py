# Search for a number x in this tuple using loop:
# (1,2,4,53,56,78,97,96,35,73,4,7,8)


num = (1,2,4,53,56,78,97,96,35,73,4,7,8)
print(num)
x=96
idx = 0
while idx < len(num):
    if(num[idx]==x):
        print("found at index",idx)
    else:
        print("Finding...")
    idx +=1