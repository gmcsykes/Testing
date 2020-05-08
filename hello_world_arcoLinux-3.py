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