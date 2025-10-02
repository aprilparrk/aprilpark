# File: homework1.py
# --- Varialbes and Data Types ---#

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) #b is a float, a real number with decimals

c =3j
print(c)
print(type(c)) #c is a complex, consisting a real part and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, which is made of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list of numbers

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary that stores data in key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple which is an ordered, immutable collection of items

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list that contains strings

i = True
print(i)
print(type(i))# i is a bool

j = None
print(j)
print(type(j))# j is a NoneType, which represents empty space

k = [True, "blue", 12]
print(k)
print(type(k))# k is a list which contains strings

l = str(14)
print(l)
print(type(l))#l is a string, which is made of characters

m = 1e4
print(m)
print(type(m))#m is a float, a real number with decimals

n = {2, 1, 3}
print(n)
print(type(n))

# 1. I found 9 different data types
# 2. integer, float, complex, string, list, dictionary, tuple, bool, nontetype
# 3. d and l are both strings
# b and m are both floats
# e, h, k are lists
# 4. The data type of l was string because the str() turned 14, which is an integer, into a string data type.
# 5. A dataype not listed was set, which is unordered, mutable collections of unique items

print(10 > 9)#True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9)#False, 10 is not less than or equal to 9
print(bool("abc"))#True, non-empty string is considered True
print(bool(123))#True, non-empty number is considered True
print(bool(["apple", "cherry", "banana"]))#True, non-empty list is considered True
print(bool(True))#True, as boolean is True
print(bool(False))#False, as boolean is False
print(bool(0))#False, because 0 is considered False in Python
print(bool(""))#False, because it's an empty string
print(bool(" "))#True, because it's a non-empty string
print(bool(()))#False, because it's an empty tuple
print(bool([]))#False, because it's an empty list
print(bool({}))#False, because it's an empty dictionary
print(bool(True and False))#False, since both aren't True, it's False
print(bool(True and True))#True since both are True
print(bool(False and False))#False since both bools are False
print(bool(True or False))#True because at least one value is True
print(bool(True or True))#True because at least one value is True
print(bool(False or False))#False because both values are False
print(bool(not(False)))#True because not False is True
print(bool(not(True)))#False because not True is False

#1. An empty string returns False, while a non-empty string returns True
#2. bool(0) because I didn't know previously that 0 is falsey 
#3. print(10>=10) will return True because 10 is greater than or equal to 10
#4. print(10>10) will return False because 10 is not greater than 10

print(10 +5) #15, performs addition
print(10-5)#5, performs substraction
print(2*4)#8, performs multiplication 
print(6/3)#2.0, performs division
print(5%2)#1, performs division
print(3**2)#9, exponentials
print(15//2)#7, performs floor division
print(5==2)#False, 5 is not equal to 2
print(10 != 10)#False, 10 is equal to 10
print(2<5)#True, 2 is less than 5
print(12>5)#True, 12 is greater than 5
print(5<=6)#True, 5 is less than or equal to 6
print(1 >=10)#False, 1 is not greater than or equal to 10

x = 5
x += 5
print(x)

x = 5
x -= 4
print(x)

x = 5
x *= 3
print(x)

#1. The and operator returns True only if both conditions are True
#print(10 > 3 and 2 > 1) True
#print(10 > 3 and 2 < 1) False
#2. The or operator returns True if at least one condition is True
#print(3 > 4 or 1 < 2) True
#print(3 > 4 or 5 > 6) False
#3. The not operator reverses the value
#print(not(False)) True
#print(not(True)) False

#1. / performs division and returns a float, while // performs floor divion, meaning it returns the quotient rounded down to the nearest whole number
#2. // returns the quotient, while % returns the remainder of the division
#3. You would use % to calculate the remainder. For example, print(10 % 3) would print 1
#4. The = operator assigns a value to a variable

my_string = "hello"
print(my_string) #prints: hello
print(my_string[0]) #prints: h
print(my_string[1]) #prints: e
print(my_string[2]) #prints: l
print(my_string[3]) #prints: l
print(my_string[4]) #prints: o
print(my_string[-1]) #prints: o
print(my_string[1:3]) #prints: el
print(my_string[0:5:2]) #prints: hlo
print(len(my_string))#prints: 5
print(my_string + " goodbye")#prints: hello goodbye
print(my_string * 7)#prints: hellohellohellohellohellohellohello

#1. Slicing is taking a portion of a sequence. I sliced my string in print(my_string[1:3]) and print(my_string[0:5:2]) 
name = "Oski"
print("Hello, my name is", name)#prints "Hello, my name is Oski"

name = "Oski"
print(f"Hello, my name is {name}")#prints "Hello, my name is Oski"
#4. The first example adds multiple arguements together, while the second example uses the f-string, which allows variable in the string itself.

# cd
# changes directories. Use it to move from one folder to another
# cd Desktop

# ls
# lists the contents of the directory
# ls

# ls -a
# lists the contents of the directory, including the hidden contents
# ls -a

# mkdir
# makes and names a new directory
# mkdir april

# cat
# concatenate, meaning it can read and combine files on terminal
# cat datatypes.py

# pwd
# print working directory, meaning it shows the pull path to the current file
# pwd

# cd ..
# Goes up one directory
# cd ..

# cd .
# Stays in the current directory
# cd .

# cd ~
# Moves to home directory
# cd ~

# cp
# copies files into a new file
# cp lecture_notes.py lecture_notes_copy.py

# mv
# moves the file to a directory
# mv homework1.py documents/

# rm
# permanently deletes file
# rm homework1.py

# clear
# clears terminal screen, but the files remain
# clear

# grep
# searches inside the file
# grep "Hello" homework1.py

# 1. 
# rmdir removes empty directory
# rmdir april

# nano allows to edit text on terminal
# nano homework1.py

# uniq removes duplicate files
# uniq homework1.py

#2. ls only lists the visible files, while ls -a lists all the files including the hidden ones
#3. Hidden files are files not shown by default. They are typically used for system configuration, settings, or application preferences
#4. 
#-l long lists the detailed information
# ls -l

#-R recursively lists subdirectories
# ls -R

#-t sorts by modification time
# ls -lt

