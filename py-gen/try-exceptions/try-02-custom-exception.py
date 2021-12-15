class BadNameException(Exception):
    def __str__(self):
        return 'Name error!'

    def __repr__(self):
        return str(type(self))
try:
    myname=input('What is my name?  ')
    if myname != 'rob':
        raise BadNameException
except BadNameException as e:
    # print will print the __str__ method for the object which is usually useful description
    print(e)
    # the __repr__ method returns a more formal string that should 
    # ideally be valid Python for recreating simailar object otherwise some useful
    # text description.
    print(repr(e))
    # see https://docs.python.org/3/reference/datamodel.html#object.repr

