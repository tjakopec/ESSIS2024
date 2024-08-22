# single quotes '
# double quotes "

# we use single quotes https://docs.ckan.org/en/ckan-2.1.5/python-coding-standards.html

print('Hello world')

# variable
# integer (int)
years = 2
print(id(years))
print(years == 2)
print(type(years))

# Other variable types
# str
name = 'Marijana'
print('name=', name, 'is', type(name))
print(name)
print(name[0])
print(name[5:])
print(name[:6])
print(name[2:6])
print(name[len(name) - 1])

# int
x = 7
print('x=', x, 'is', type(x))
print('x=', 7, 'is', type(7))

# float
x = 7.7
print('x=', x, 'is', type(x))
print('x=', 7.7, 'is', type(7.7))

# complex
x = 7 + 2j
print('x=', x, 'is', type(x))
print('x=', 7 + 2j, 'is', type(7 + 2j))

# bool
x = True
print('x=', x, 'is', type(x))
print('x=', True, 'is', type(True))

# Single line comment
'''
Multiline comment
'''

"""
Multiline comment
"""

# multiline print with new line escape char (\n)
print('First line\nSecond line')
# ASCII art: https://www.asciiart.eu/
print('|\\---/|\n| o_o |\n \\_^_/')
# format print
print("Python".center(80))
# text concatenation
print('|\\---/|' + '\n' +
      '| o_o |' + '\n' +
      ' \\_^_/')
# All letters UPPERCASE
print('lorem ipsum'.upper())
# print two numbers separated with space
print(2, 2)
# print names with comma as separator
print('Dora', 'Lada', 'Mara', sep=', ')
# print name 7 times
print('Nataša' * 7)
# print name and put dot at the end
print('Tomislav', end='.')

# OPERATORS

# arithmetic operators + - * / % // **

# There is no ++ --      WHICH IS USUAL IN OTHER LANGUAGES

x = 3.8 + 2  # adding
print(x)

x = 9 - 3  # subtracting
print(x)

x = 3.8 * 2.737363635  # multiplying
print(x)

x = 1 / 3  # dividing
print(x)

x = 3 % 2  # modulo - remainder after integer division
print(x)

x = 1 // 3  # integer division
print(x)

x = 2 ** 3  # math function power
print(x)

#
# Comparison operators == < > <= => !=
#

x = 2  # value assignment

print(x == 2)  # equality check
print(x > 2)  # other >=  <=
print(x != 2)  # not equal

#
# Logical operators (bool) and or not
#

x, y = 1, 2

print(x == 1 and y == 2)

print(x > 0 or y < 10)

print(not (x != 1 and y != 2))

#
#
#
name = 'Martin'
years = 18

adult = years >= 18

if adult:
    print(name, ' is adult')

# more common way
if years >= 18:
    print(name, ' is adult')

n1 = 5
n2 = 7
n3 = 6
biggest = -100  # whe should use the smallest int

if n1 >= n2 and n1 >= n3:
    biggest = n1
elif n2 >= n1 and n2 >= n3:
    biggest = n2
else:
    biggest = n3
print('The biggest number is', biggest)

# lists
temperature = [8, 7, 13, 16, 17, 12]
print(type(temperature), temperature)

print(temperature)
print(temperature[0])
print(temperature[4:])
print(temperature[:4])
print(temperature[2:4])
print(temperature[-1])

# iterating the list
for temp in temperature:
    print(temp)

# dictionaries

temperature = {
    'midnight': 8,
    'night': 7,
    'morning': 13,
    'noon': 16,
    'afternoon': 17,
    'evening': 12,
}
print(type(temperature), temperature)

temperature['noon'] = 14
print(temperature)
print(temperature['noon'])


# methods

def add_numbers(num1, num2):
    foo = num1 + num2
    return foo - 1


print(add_numbers(2, 3))

# using modules
# this should be at the beginning of the file!
import random
from random import randint

print(random.random())

print(randint(1, 100))

# working with files

file = open('domains.txt', 'r')
domains = file.readlines()
for domain in domains:
    print(domain.strip())



# input / output from user

domain = input('Please write domain name: ')


print('You typed:',domain)