review.py
######### REVIEW FOR EXAM 1
# Made by Hao Zheng

# uncomment and play around with the code as you see fit

##### DATA TYPES

# int
# any whole number 1, 4, 6, -1, 0
# operators:
# +(addition) -(subtraction) *(multiplication) /(division) **(exponent)
# //(int division, only takes the whole number of quotient)
# %(modulo, takes remainder of quotient)

# float
# decimal number 1.3, 482.5, -134.4, 0.0
# operators:
# same as int but I do not reccommend you use // or %

# str
# use ' or " around your value to make it a string
# 'bruh' "bruh"
# be careful with cases like "0", "0.0", "False" THESE ARE ALL STRINGS

# bool
# True or False
# operators and, not, or

# list
# collection of values, see below
# [0,5,5,8,4,4]
# ["452", "346", "sfjfg"]

var = 12 # change this around
# print(type(var)) # this will tell you the type of var

# casting
# put the value inside the casting function
# str(value), int(value) etc...
# MAKE SURE INPUT IS VALID int("9.34") will NOT cast to float, it will throw error
# float case to int will truncate the decimal
# casting to bool will only return false if the value is a "zero" or "nothing" value
# ex 0, 0.0, "", [] will cast to False, anything else is True
# print(type(int("923")))

##### PRINTING AND FORMATTING

# print sep, end
# sep determines what will separate the arguments of print(), default is " "
# end determines what goes at the end of the print(), default is "\n" (newline)

# uncomment and play around with these print statements
# print("inut", 789, "this is a string", sep="bruh", end="\n\n")
# print("b", 78)

# fstring
# formatting of variables in string
# f"this is a string {data} rest of string"
# can also round decimals, uncomment and see code below

x = 10.2347138591
y = 20.3857985475
# print("x is", round(x, 3), "y is", y)
# print(f"x is {x:.3f} y is {y}")

##### VARIABLE ASSIGNMENT

# order of assignment
# python reads from top to bottom
# move line yy = xx to above xx = 3 and see what happens
# also see how the variable changes
xx = 3
yy = xx # currently 3
xx = 6
# print(xx, yy)

##### USER INPUT

# input method
# take user input as a str value
# inp = input("type something: ")
# print(inp)
# print(type(inp)) # should be str

# cast input value
# cast the inupt value to the desired data type
# inp2 = int(input("input int here: "))
# print(inp2)
# print(type(inp2))

##### CONDITIONAL STATEMENTS

# if elif else
# conditional statements take in a boolean expression and if true
# will run what is inside the conditional control statement
# treat the if keyword as a sort of "start" of a new set conditional statements
# uncomment to try this out
# userIn = int(input("input grade "))
# if userIn >= 90:
#     print("A")
# elif userIn >= 80: # switch between if and elif and see the difference
#     print("B")
# elif userIn >= 70: # switch between if and elif and see the difference
#     print("C")
# else:
#     print("bruh")
# print("end")

##### LOOPS

# for
# iterates through an iterable object, like a list
lisRange = range(20)
lisNum = [1, 7, 4, 6, 9, 6, 34, 9]
lisStr = "I am also iterable"
for i in lisNum: # see what happens when using lisNum, lisRange, and lisStr
    # print(i)
    pass

# while
# loops until the conditional statement is False
iter = 0
while iter < 10:
    # print(iter)
    iter += 1

# nested loop example
outside = 0
inside = 0
while outside < 3:
    # print("out", outside)
    while inside < 4:
        # print("in", inside)
        inside += 1
    inside = 0
    outside += 1



##### LIST OPERATIONS

# think of strings as kind of like a list of characters
# BE CAREFUL WITH THIS AS STRINGS ARE IMMUTABLE (cannot be changed)
listNum = [x**2 for x in range(20)] # dont worry about how this works, its just making a list
listStr = "abcdefghijklmnop skfjfgkasfhg"
listChar = list(listStr) # each individual character is its own element in a list
# print(listNum)
# print(listStr)
# print(listChar)
# notice how listStr is still of type str
# print("listNum type:", type(listNum))
# print("listStr type:", type(listStr))
# print("listChar type:", type(listChar))

# concatenation
# you can just use the + operator
# be aware of the order you concatenate
anotherList = [6, 7, 8, 9, 5]
# print(listNum + anotherList)
# print(anotherList + listNum)

# access
# indexing starts at 0
# ex 4th element is at index 3
idx = 0 # change this around
# print(listNum[idx])
# print(listStr[idx])
# print(listChar[idx])
# you can also change the values in the list
# see what happens when you try to change listStr, which is a string
listNum[idx] = 0
# listStr[idx] = "b" # this will throw error because type str is immutable
listChar[idx] = "b"
# print("After value change:")
# print(listNum)
# print(listChar)

# splicing
# take a sublist of your list
start = 0
end = 5
# print(listNum[start:end])
# print(listStr[start:end])
# print(listChar[start:end])

# append
# adds one value to the end of list
# print("Before append():", listNum)
# listNum.append(123)
# print("After append():", listNum)

# pop
# removes item at given index and returns the value of that item
idxP = 0
# print("Before pop():", listNum)
# print("Value removed:", listNum.pop(idxP)) # if no argument is given it will pop last element
# print("After pop():", listNum)

# remove
# removes the FIRST occurence of item
# print("Before remove():", listNum)
# listNum.remove(9)
# print("After remove():", listNum)
# add some more 9's and see result

# list copying
# lists are done by reference in python
listNum2 = listNum
# listNum2 = listNum.copy() # switch between this and listNum2 = listNum to see difference
# print("listNum before:", listNum)
# print("listNum2 before:", listNum2)
listNum2[0] = 312984
# print("listNum after:", listNum)
# print("listNum2 after:", listNum2)

# 2d lists (matrix)
# list of lists
# same rules apply, getting index of outer list returns the inner list
listMatrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
idxOut = 0
idxIn = 0
# print(listMatrix[idxOut])
# print(listMatrix[idxOut][idxIn])
# a nested loop can be useful for iterating though matrices
# for list in listMatrix: # list is a row in the matric
#     for item in list: # item is an element in that row
#         print(item)

##### FUNCTIONS

# function parameters
def func(smth, thing="bruh"): # default parameters
    print("bruh", smth, thing)
# func("hi")
# func("b", "thing2")

# function return
# the function will essentiall take on the value it returns
def func2(x):
    print("I did smth")
    return x**2
# print(func2(5) + 2)



##### IMPORTS

# from vs import keyword
# compare result when using different keyword
import math
# from math import sin # use * to import everything
# print(math.sin(1))
# print(sin(1))

