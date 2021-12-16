# Exception is the mother class of all exceptions and includes
# the built-in exceptions.add()
# see https://docs.python.org/3/library/exceptions.html#bltin-exceptions
try:
    file=open('rob.txt')

except Exception:
    print('Something went wrong:')
else:
    print('It went good')
finally:
    print('finished try')

