class BadAgeException(ValueError):
    def __str__(self):
        return 'Value entered not allowed.'

    def __repr__(self):
        return str(type(self))
try:
    allowedages=[21,39,58]
    myname=input('What is my age?')
    if int(myname) not in allowedages:
        raise ValueError
        # raise BadAgeException
    else:
        print('You got my age right. Well done!')
except BadAgeException as err:
    print(err)
