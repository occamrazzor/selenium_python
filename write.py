# With ensure file will be open and closed automatically
# Read the file test2.txt and store all the lines in list
# reverse the list
# write the list back to the file test2.txt

with open('test2.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test2.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
    
# Note this will reverse the lines in test2.txt file