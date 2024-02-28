"""
File I/O in python

Python can be used to perform operations on a file.(rad and write data )


Types of all files

1] Text Files : txxt, .docx, .log etc. ( Store a tex data)
2] Binary Fles : mp4, .mov, .png, .jpeg etc.( Store non textual data)

"""
 

 #Open , read and close file
"""
Open , read and close file

We have to open afile before reading or writing.
f = open("file_name", "mode")

"""
# read file

f = open("txt.py","r")
data = f.read()
print(data)
print(type(data))
f.close( )

"""
'r' => open for reading (default)
'w' => open for writing, truncating the file first
'x' => create a new file and open it for writing
'a' => open for writing, appending to the end of the file if it exists
'b' => binary mode
't' => text mode(default)
'+' => open a dist file for updating (reading and writing)

"""


f = open("txt.py","r")
data = f.readline()
print(data)
print(type(data))
f.close()

# Writing to a file


f = open("txt.py", "a")
f.write("\n After That i will learn java")
f.close