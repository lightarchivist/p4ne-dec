class BadNameException(Exception):
    def __str__(self):
        return 'Name error!'

    def __repr__(self):
        return str(type(self))
try:
    myname=input('What is my name?  ')
    if myname != 'rob':
        raise BadNameException
    
    open('rob.txt')
except BadNameException as e:
    # print will print the __str__ method for the object which is usually useful description
    print(e)
except Exception as e:
    # print will print the __str__ method for the object which is usually useful description
    print('Another exeption raised, but we caught it')



