#Open a text file to read or write
file = open('test.txt')
# print(file.read()) Reads the whole file
# print(file.read(2)) # Only reads 1st two characters in the file ... ab


# print(file.readline()) # reads one single line ... abc

# Print line by line using readline method
line = file.readline()
while line != "":
  print(line)
  line = file.readline()
file.close()



file2 = open('test2.txt')

# line2 = file2.readlines()...['abc\n', 'bvdsf\n', 'cat\n', 'dog\n', 'elephant\n']
# print(line2) # Readlines will be stored in a list

for item in file2.readlines():
  print(item)

file2.close()

