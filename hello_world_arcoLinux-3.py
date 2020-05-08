#! /usr/bin/python
print ('Hello World')
print (3 * 4)
print (7 * 9)
print (9 * 9)
print ( 3 * 7 / 9 * 98)

a = (1 + 2 +3 + 
    4 + 5 + 6 + 
    7 + 8 + 9)
print (a)
for i in range(1,11):
    print(i)
    if i == 5:
        break

def double(num):
    """Function to double the value"""
    return 2*num
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

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
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

x = (1 == True)
y = (1 == False)
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

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2,3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels ={'a', 'e', 'i', 'o', 'i'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)


