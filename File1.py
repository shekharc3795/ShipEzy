import os
#os.mkdir("/Users/sadhnasc/Documents/GitHub/ShipEzy/be/file_handling",)

# Open a file
fo = open("/Users/sadhnasc/Documents/GitHub/ShipEzy/be/Test.txt", "r+")
str = fo.readline()
print ("Read String is : ", str)
str = fo.readline()
print ("Read String is : ", str)
# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)

# Close opened file
fo.close()

# Rename a file from test1.txt to test2.txt
#os.rename( "/Users/sadhnasc/Documents/GitHub/ShipEzy/be/Test.txt", "/Users/sadhnasc/Documents/GitHub/ShipEzy/be/Tes