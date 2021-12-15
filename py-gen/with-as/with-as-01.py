# to show a with...as: statement
# we don't have to close the files as with cleans up for us
with open('test.txt', 'r') as myfile:
    lines = myfile.readlines()
    # show the list of strings with newline indicators
    print(lines)
    for line in lines:
        #  we can strip off the newline indicator
        print(line.strip())

#  variables from within the with...as: are still available
print('Here are the lines:', lines)

# but the file is closed so we get an error
page = myfile.readlines()

