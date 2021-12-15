import time

# secs since epoch
print(time.time())

#local time
print(time.localtime(time.time()))

# prints only the hour number
print(time.localtime(time.time()).tm_hour)

# pause
print('I am going to sleep for 3 seconds...')
time.sleep(3)

# better
print(time.asctime(time.localtime(time.time())))
# same but simpler
print(time.ctime(time.time()))

