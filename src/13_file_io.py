"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

filename = open('foo.txt', mode='r')
for x in filename:
    print(x)

filename.close()

# with  
filename = 'foo.txt' 
 
with open(filename) as f_obj:
    contents = f_obj.read() 
 
print(contents) 




# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open(file = "bar.txt", mode = 'w')
bar.write('Mary had a little lamb')
bar.write('Four score and seven years ago')
bar.write('Run Forest run')
bar.close()