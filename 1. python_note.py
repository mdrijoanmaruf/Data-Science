                # **********Variable**********

x = 4           #type int
y = "saif"      #type str

x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0

type(y)         # str

x = "saif"      # str in ""
x = 'saif'      # str in '' (Those are same meaning)

# varibale are case sessitive

x, y, z = 12 , 34.4 , "saif"        # Multiple values

# unpack a cullection:
fruits = ["Apple" , "Banana"]
x, y = fruits                       # x = apple , y = banana

# Outpur Variable:
x = "rijoan"
y = "maruf"
print(x ,y)     # will print rijoan maruf
print(x + y)    # will print rijoanmaruf

# Any variable is outside in function is Global variable

# Numbers:
x = 1           # int
y = 1.11        # float
x = "saif"      # str
x = 1j          # complex

# Random Number:
import random
x = random.randrange(1 , 10)        # random number 1 - 10 will store in x






                #********** String **********

# Multilne String
a = """This is 
Multi line of string"""

b = '''This is also
Multi line of sting'''

# Strings are array
a = "saif"  # index start with 0
a[1]        # a
a[0]        # s

# Looping through a string
for i in "saif":
    print(i)   # print  # s
                        # a
                        # i
                        # f

# String lenght:
y = len("saif")     # store lenght in y 

# Check string:
x = "my name is saif"
y = "saif" in x         # True
z = "rijoan" in x       # False

# Slicing String:
x = "Hello i am saif"
print(x[2:5])       # will print index 2 - 5
print(x[:5])        # will print index 0 - 5
print(x[2:])        # will print index 2 - end

# Nagetive indexing:
x = "saif"          # -4 -3 -2 -1 
                    #  s  a  i  f
                    #  0  1  2  3
x[-3 : -1]          # aif

# Modify String:
x.upper()           # convert intu upper case
x.lower()           # convert intu lawer case
x.split()           # remove whitespace form the begining or and
x.replace("s" , "x") # replace s to x . so saif will be xaif

# String Format:
age = 36
text = "My age is {}"
text.format(age)    # age vlaue will set in {} 

# Escape Characters:
    # \'        --> '
    # \\        --> \
    # \n        --> new line
    # \t        --> new tab

# String methods: Link: w3school

# Booeans:
bool("abc")         # True
bool(29)            # True
bool(False)         # False
bool(None)          # False
bool(0)             # False
bool("")            # False
bool(())            # False
bool([])            # False

# Logical Operators:
    # and , or , not
    
# Indntity Operators:
x , y = 10 , 10
x is y      # True
x is not y  # False

# Membership Operators:
x = ["apple" , "banana"]
print("banana" in x)        # True
print("banana" not in x)    # False
    
# Bitwise Operators:
    # & , | , ^ , << , >> 






                #********** Lists **********
                
mylist = ["apple" , "banana" , "jackfruit"]     # index start with 0
x = len(mylist)                                 # x = 3
list1 = ["abd" , 12 , True , "male"]            # Can store different data type

# List Constructor:
newlist = list(("saif" , "rihan" , "srabon"))   # newlist = ["saif" , "rihan" , "srabon"]

# Access Items:
newlist[0]      # saif
newlist[2]      # srabon

# Change list items:
newlist[0] = "rijoan"       # newlist = ["rijoan" , "rihan" , srabon]

# Insert New items:
newlist.insert(2 , "maruf")     # add "maruf" in 2 index

# Append Items:
newlist.append("mehedy")    # add "mehedy" in last of newlist

# Extend List:
list1 = ["saif" , "rijoan"]
list2 = ["srabon" , "rihan"]
list2.extend(list1)         # list2 = ["srabon" , "rihan" , "saif" , "rijoan"]

# Remove Specified item:
list2.remove("srabon")      # list2 = ["rihan" , "saif" , "rijoan"]

# Remove Specified index:
list2.pop(0)                # remove 1st index value
del list2[1]                # remove 2nd index. index 1
list2.pop()                 # remove all

# Clear the list:
list2.clear()               # will clear the list

# Sort list Alphanumerically:
list3 = ["sajib" , "rihan" , "azad" ]
list3.sort()                # ["azad" , "rihan" , "sajib"] 

# Reverse order:
list3.reverse()
print(list3)                # ["sajib" , "rihan" , "azad"]

# Copy a list:
newlist = list3.copy()      # newlist = ["sajib" , "rihan" , "azad"]

# Jion list:
list1 = ["saif" , "rioan"]
list2 = ["sajib" , "rihan"]
newlist = list1 + list2     # newlist = ["saif" , "rijoan" , "sajib" , "rihan"]







                # **********Tuple**********
# Store multiple items in single variable
# A tuple is a collection which is ordered and unchangeable
# Allaw duplicates and index start with 0
# Can contain defferent datatype
tuple1 = ("abc" , 34 , True)

# Tuple to List:
y = list(tuple1)        # y = ["abc" , 32 , True]

# List to Tuple:
x = tuple(tuple1)       # x = ("abc" , 34 , True)
 
# Unpacking tuples:
fruits = ("apple" , "banana")
(green , yellow) = fruits       # green = apple , "yellow" = "banana"







                # **********Dictionary**********
mydic = {
    "name" : "saif",
    "college" : "aiub",
}
# Now dictionary is orderd 
mydic["college"]        # aiub
# Duplicate is not allowed
mydic.keys()            # all key values
mydic.values()          # all values
mydic.items()           # all items

# Can change values:
mydic.update({"name" : "rijoan"})   # replace "saif" with "rijoan"

# Add items:
mydic["address"] = "dhaka"          # Add new items "address" : "dhaka"

# Remove Items:
mydic.pop("name")                   # Remove red items
del mydic["college"]                # Remove college items

# Copy Dictionary:
newdic = mydic.copy()               # newdic now contain mydic copy values

# A dictionary can contain another dictionary and etc.







                # **********Function**********
                
def myfunction(x):          # Function define
    print(x)
myfunction(100)             # Function call







                # **********File**********

f = open("new.c" , "w+")# file neame new.c and mode w+ = read and write
f.write("Hello wold")   # write file
f.read()                # read file
f.close()               # close file
                        # "a" --> will append end to file
# Create a new file:
# "x" --> acreate file and return error if file exist
# "a" --> append - will create file if it dose not exist

# Delete a file/folder:
import os
os.remove("new.c")      # remove the new.c file
# os.rmdir("x")         # remove x folder







                # **********Classes and object**********

class Person:           # create a class
    Name = "saif",      # class variable
    Rool = 346
    
    def infu(self):     # class method / function
        print(f"\nName: {self.Name}\nRool : {self.Rool}")
sajib = Person()        # creating object
saif = Person()

sajib.Name = "sajib"    # object value
sajib.Rool = 23534
sajib.infu()            # call method 







                # **********Exception Handaling**********

try:
    a = 1/0
except Exception as e:  # e is exception type
    print(e)
    print("This is exception")



