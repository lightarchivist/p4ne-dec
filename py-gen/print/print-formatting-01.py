#  tHE BELOW ARE DIFFERENT METHODS TO FORMAT THE PRINTED OUTPUT
#  YOU SHOULD TRY TO USE NUMBER 4, THE f METHOD


""" 1 - USING SUBSTITUION"""
missing_word = 'weather'
print('The %s is good.'%('weather'))
print('The %s is good.'%(missing_word))


""" 2 - USING TEMPLATES"""
from string import Template
person1 = 'Harry'
person2 = 'Jo'
 
# template that requires two inputs p1 adn p2
n = Template('$p1 works with $p2.')
 
# and pass the parameters into the
# template string.
print(n.substitute(p1=person1, p2=person2))

""" 3 - THE .format METHOD. """
print('The {} is good.'.format('weather'))
print('The {} is good.'.format(missing_word))
print('Ron likes {a}, Anne likes {b}, but Kate likes {c1}'.format(a='red', b='blue', c1='green'))
print('The first {p} was alright, but the {p} {p} was tough.'.format(p = 'second'))

# see: https://www.python.org/dev/peps/pep-3101/

# The general syntax is:
# [[fill]align][sign][#][0][minimumwidth][.precision][type]

# Align flag options:
# '<' - Forces the field to be left-aligned within the available space (This is the default.)
# '>' - Forces the field to be right-aligned within the available space.
# '=' - Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form '+000000120'. This alignment option is only valid for numeric types.
# '^' - Forces the field to be centered within the available space.

# Sign option:(numbers only)
# '+' - indicates that a sign should be used for both positive as well as negative numbers
# '-' - indicates that a sign should be used only for negative numbers (this is the default behavior)
# ' ' - indicates that a leading space should be used on positive numbers

# '#' character means integers use the 'alternate form' for formatting. This means that binary, octal, and hexadecimal output will be prefixed with '0b', '0o', and '0x', respectively

# 'width' is a decimal integer defining the minimum field width. If not specified, then the field width will be determined by the content.

# If the width field is preceded by a zero ('0') character, this enables zero-padding. This is equivalent to an alignment type of '=' and a fill character of '0'.

# The 'precision' is a decimal number indicating how many digits should be displayed after the decimal point in a floating point conversion. For non-numeric types the field indicates the maximum field size - in other words, how many characters will be used from the field content. The precision is ignored for integer conversions.

# Types:
# ‘d’ for integers
# ‘f’ for floating-point numbers
# ‘b’ for binary numbers
# ‘o’ for octal numbers
# ‘x’ for octal hexadecimal numbers
# ‘s’ for string
# ‘e’ for floating-point in an exponent format

print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
print("Geeks: {a:5d},  Portal: {p:8.2f}".format(a = 453, p = 59.058))

a = 'It'
b = 'is'
c = 'quite'
d = 'delightful.'
print('{:_<30}{:<30}{:<30}{:<}'.format(a,b,c,d))

# [[fill]align][sign][#][0][minimumwidth][.precision][type]
a = 29
b = 12345678
c = 234.6789
d = 4.123
print('{:_>20}  {:0=+20}  {:^20.2f}  {:>.1f}'.format(a,b,c,d))


""" 4 - THE MORE MODERN f METHOD"""
missing_word = 'weather'
print(f'The {missing_word} is good.')
me=58
jo=49
print(f'Jo is {me - jo} years younger than me.')

e = 2.71828
 
print(f"The value of e is: {e:{2}.{5}}")
print(f"The value of e is: {e:{10}.{3}}")
print(f"The value of e is: {e:_>{15}.{5}}")
print(f"The value of e is: {e:->+{15}.{4}}")
print(f"The value of e is: {e:0=+{15}.{3}}")