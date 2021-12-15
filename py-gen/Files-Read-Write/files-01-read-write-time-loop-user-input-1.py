import time

with open('results1.txt','w') as output_file:
    for index in range(3):
        textline = input('Please enter a line of text: ')
        time_now = time.asctime(time.localtime(time.time()))
        # write the time and the line to the file
        output_file.write(f'Time: {time_now} The message is: "{textline.strip()}"\n')


