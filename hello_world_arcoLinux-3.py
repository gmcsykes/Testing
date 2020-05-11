#! /usr/bin/python
print("Hello World")
print(3 * 4)
print(7 * 9)
print(9 * 9)
print(3 * 7 / 9 * 98)

a = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
print(a)
for i in range(1, 11):
    print(i)
    if i == 5:
        break


def double(num):
    """Function to double the value"""
    return 2 * num


print(double.__doc__)
website = "apple.com"
print(website)

# assigning a new variable to website
website = "programiz.com"
print(website)

a, b, c = 5, 3.2, "hello"

print(a)
print(b)
print(c)

x = y = z = "same"

print(x)
print(y)
print(z)

a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12C  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

x = 1 == True
y = 1 == False
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

drink = "Available"
food = "None"


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {"a": "apple", "b": "ball", "c": "cat"}  # dictionary
vowels = {"a", "e", "i", "o", "u"}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1 + 2j
print(a, "is complex number?", isinstance(1 + 2j, complex))

a = [1, 2.2, "python"]

a = [5, 10, 15, 20, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [1, 2, 3]
a[2] = 4
print(a)

t = (5, "program", 1 + 3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# generates an error
# Tuples are immutable
# t[0] = 10

# Python Strings

s = "Hello World!"

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Python Set

a = {5, 2, 3, 1, 4}
# printing se variable
print("a = ", a)

# data type of variable a
print(type(a))

a = {1, 2, 2, 3, 3, 3}
print(a)

d = {1: "value", "key": 2}
print(type(d))

print("d[1] = ", d[1])
print("d['key'] = ", d["key"])

# Example 1: Converting integer to float

num_int = 123
num_flo = 1.23
num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

# Example 2: Addition of string(higher) data type and integer(lower)
# generateds  an error from
# num_int = 123
# num_str = "456"

# print("Data type of num_int:", type(num_int))
# print("Data type of num_str:", type(num_str))

# print(num_int + num_str)

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))
