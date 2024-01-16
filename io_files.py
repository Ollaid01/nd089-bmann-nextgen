# Reading and Writing Files

# Using Files

my_file = open('./some_file.txt', 'r')  # open func return file object
file_data = my_file.read()  # read data
my_file.close()  # close file and free resource

# print data
# print(file_data)

# read another file (.py)
pyfile = open('./tuples.py', 'r')
file_data = pyfile.read()
pyfile.close()
print(file_data)


# Writing Files
pyfile = open('./tuples.py', 'w')
pyfile.write("Wrrrrrite  Hello There !")
pyfile.close()
print(file_data)

