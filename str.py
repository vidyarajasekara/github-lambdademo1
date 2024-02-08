a = ["apples,oranges,bananas"]
print(a[0])
b = a[0]
print(b)
c = b.split(',')
print(c)

#1. string """
a = """aaaaaaaaaaaa,
  bbbbbbbbbbbb
  ccccccccc,
  dddddd"""
print(a)

#2.Square brackets can be used to access elements of the string.

a = "hello,world"
print(a[1], a[3])
print(a[5])

#3.Looping Through a String
s = "letter"
for a in s:
    print(a)

for b in "mail":
    print(b)

#4.string len
a = "Hello, World!"
print(len(a))

x="programming language"
print(len(x))

#5.#To check if a certain phrase or character is present in a string, we can use the keyword in.

a="This friday will be holiday"
print("friday" in a)

#6.#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

b="welcome to my home"
print("house" not in b)
print("home" not in b)

#7.You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
c="Wow,that was a great place to visit with your family"
print(c[0:4])
print(c[10:21])
print(c[0:5])
print(c[:3])
print(c[15:])
# negative indexing starting from the end -1 and ending index add -1
print(c[-6:-1])
print(c[-6:-2])
print(c[-6:])


b = "Hello, World!"
print(b[2:7])

b = "Hello, World!"
print(b[2:5])

# uppercase
c="Wow,that was a great place to visit with your family"
print(c.upper())
print(c.lower())
# #Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# #The strip() method removes any whitespace from the beginning or the end:

d = "  great place to visit  "
print(d.strip())

#Replace String
#The replace() method replaces a string with another string:
a="Running"
print(a.replace("R","T"))
#split
a='running,fast'
print(a.split(","))

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
a = "hello"
b = "everyone"
c = a+b
print(c)
#To add a space between them, add a " ":
c = a+" "+b
print(c)

c = a+","+b
print(c)

# we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

p = 100.95
f = 5
msg = "It cost around {} dollar"
print(msg.format(p))
print(type(msg))

a = "{} crocs cost {} "
print(a.format(f, p))

a = 2
b = 5
txt = "buy {1} oranges and {0} grapes"
print(txt.format(a, b))

#Escape Character
# s = "my name is "vidya""
# print(s)

# String Methods
st = "welcome"
print(st.capitalize())

st1 = "WELCOME"
print(st1.casefold())

st1 = "WELCOME WeLcOmE welcome"
print(st1.center(200))

print(st1.count("W"))

print(st1.encode())
d="hai"
print(d.encode())
# By default, Python uses utf-8 encoding
# UTF-8 is a variable-length character encoding standard used for electronic communication
# Unicode Transformation Format – 8-bit

#endswith()
a = "google"
print(a.endswith("e"))


#expandtabs()
a = "google\tsafari\t"
print(a.expandtabs())

#find()
w = "kangaroo"
print(w.find("r"))

#format() formatting for default, positional, keyword  and mixed arguments
print("{x} oranges {y} mangoes".format(x="yummy",y="juicy"))
print("{} oranges {} mangoes".format("yummy","juicy"))
print("{1} oranges {0} mangoes".format("yummy","juicy"))
print("{} oranges {y} mangoes".format(2,y="juicy"))

#format_map() A dictionary in Python is a data structure that stores the value in value:key pairs.
# z = {'a':,'b':}
# print('{a} {b}'.format_map(z))
points = {'a':5,'b':10}
print("{a},{b}".format_map(points))

#index()

txt = "cheese pizza"
print(txt.index("pizza"))

#isalnum()The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
a = "#$$%%^^"
b = "dghjky"
c = "10"
d = "1"
print(a.isalnum())
print(b.isalpha())

# string contains digit or numeric characters using isdecimal() returns true only for numbers from 0-9 where isdigit
#  isdigit()return for other unicode supported char as well
print(c.isdecimal())
print(d.isdigit())





#isidentifier()	Returns True if the string is an identifier
#islower()	    Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	    Returns True if all characters in the string are whitespaces
#istitle()	    Returns True if the string follows the rules of a title
#isupper()	    Returns True if all characters in the string are upper case
#join()	        Joins the elements of an iterable to the end of the string
#ljust()	    Returns a left justified version of the string
#lower()	    Converts a string into lower case
#lstrip()	    Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	    Returns a string where a specified value is replaced with a specified value
#rfind()	    Searches the string for a specified value and returns the last position of where it was found
#rindex()	    Searches the string for a specified value and returns the last position of where it was found
#rjust()	    Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	    Splits the string at the specified separator, and returns a list
#rstrip()	    Returns a right trim version of the string
#split()	    Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	    Returns a trimmed version of the string
#swapcase()	    Swaps cases, lower case becomes upper case and vice versa
#title()	    Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	    Converts a string into upper case
#zfill()	    Fills the string with a specified number of 0 values at the beginning




