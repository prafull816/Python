# Create a new file "practice.txt" using python. add the following data in it:
"""
hi everyone
we are learning file i/o
using java
i like programming in java.
"""

with open("practice.txt","w") as f:
     f.write("hi everyone\n we are learning file I\O \n")
     f.write("using java.\n i like programmming in java")