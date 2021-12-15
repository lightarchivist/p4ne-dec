import time

# Ask the user if they want to continue
with open('results2.txt','w') as output_file:
    # set the variable to true, it will be a boolean
    textline = True
    # Keep doing the loop until the variable evaluates as False
    while textline:
        # read input from console, and put it in variable
        # Variable will now be a string
        textline = input('Please enter a line of text (enter nothing if you want to quit): ')
        # If the string contains anything (evaluates as True)
        if textline:
            time_now = time.asctime(time.localtime(time.time()))
            # write the time and the line to the file
            output_file.write(f'Time: {time_now} The message is: "{textline.strip()}"\n')


