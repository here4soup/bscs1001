# /// 
# module name:      1001 lecture
# desc:             tasks and play for lecture per name, and any exercises
#
# version:          v1.0
# major versions:   2026 09 24    -   V1.0 Initial version
# dependencies: 
#   none
# keys: 
#       #PLAY!          (play with task)
#       #LEARN!         (learnings stated) 
#       #TODOLATER      (things to learn later)
#       #REFRESH        (things to refresh later)
#       #MISSEDSTEP     (fix later)
#       #CORRECT!       (this vsnippet is correctly working)
#       #PREF!          (this is my preferred method)
# ///

# =========================================================================================================
# =================
# tutorial
# =================

# ===== 1. play with a loop 
sentence = "kei te pai koe?"
index = 0

while index < len (sentence):
    sub = sentence [ : index]
    print(sub)
    index += 1



# ===== 2. functions

def greet(message):
    print(message)

# argument
greet("taihoa!") # tēnei
greet("e moe!") 

# function
money_value = 5.89095

as_int = int(money_value) # tēnei
print(as_int)

# idk
s = "kia ora"

double_length = len(s)*2
print(double_length)

# sum function. rule/macro
def sum_of_value(first, second):
    print(first + second)

# not valid approach
sum_of_value(10,30) + sum_of_value(99, 77) # you would have to not use print statement. has a syntax error bc + is not defined

# correct path
def sum_of_value(first, second):
    return first + second # more useful generally. usable

sum_of_value(99,2)
value = sum_of_value(99,2) * 3
print(value)



# -----  function

def first_char(string):
    return string[0]

name = input("Ko wai tō ingoa?")

print(f"The first letter of your name is {first_char(name)}")



# -----  function

def product(a, b):
    return a * b

value = product(2, product(2,3))

print(value)

# -----  factorial #

def factorial(number):
    index = 2 
    result = 1
    while index <= number:
        result *= index
        index += 1

    return result

factorial(10)



# -----

def sum_of_values (a, b):
    return a + b # python has an ability to concatenate two strings IF they are both strings
                # you need to add type hints if you want to teach it to expect value of variable

sum_of_values ("abc", "ngā")

# finding type

number = 10 
number = 10.6
number = "ngā"
number = "TRUE" # not boolean! bool #TODOLATER

print(type(number)) #LEARN! python uses dynamic typing

def countdown(value: int): # easier to prevent errors
    while value >= 1:
        print(value)
        value -= 1

countdown("56")
countdown(56)


#PLAY
def factorial(n: int):
    print(n)

factorial(10.7)
#END

#PLAY
def join(first: int, second: int) -> float:  # pylance is a style detector for auto scroll
    return float(first + second)
join(5.666,7)
#END


def first_n_last_char(name: str): #TODOLATER doesnt work
    first = name[0]
    last = name [-1]
    return first + last

name = "bobby"
print(first_n_last_char)

print(name[2 : 88]) # prints what it can. 0 is first character
print(name[-3 : 5]) # can take a slice out of an empty string with this



# ----- making a datastructure
# Not like this
result1 = 0
result2 = 54
result3 = 6

# dynamic datastructure and lists
results = [3,4,5,7,8,2,4,5,74,32,6,0] # make a list
print(len(results))
print(results[2]) # 2 is the tuatoru one

results[2] = 1000 # replace the tuatoru value. #LEARN! doesnt work for strings

print(results[2]) # 2 is the tuatoru one 

# treat strings

name = "Hēmi"

nlist = list(name)
nlist[0] = nlist[0].upper()
#MISSEDSTEP
name = nlist
print(nlist)


result = [3,4,6,77] 
result.append(20000) # add one
print(result)
result += [4,333,567,777] # add multiple
print(result)
result.insert(2,100000000) # add a third item. push third item to fourth
print(result)
result.insert(2,"hello") # add a third item. push third item to fourth
print(result)

name = []
while True:
    name = input("give a name:")
    if not name:
        break
#MISSEDSTEP
name.append(name)

print(name)

# ----- using lists
numbers = [3,4,5,2,4]
numbers.pop(1) # index you want to remove
print(numbers)
numbers.remove(4) # define the item you want to remove. eg all 4
print(numbers) #LEARN! but if you don't have any of that item in the actual list, then will return an error. handle this with a function

#def safe_remove(numbers: list) #TODOLATER

# ---- sorting
results = [23,5.7,7.8,8]
results.sort()
print(results)

names = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
names.sort()
print(names)

# original order might be important
results =["Hēmi", "Neihana", "Arapera"]
results_sorted = sorted (results)
print(results)
print(results_sorted)

# ----- other sorting as WITH FOR loopS
# clumsy sort
names =["Hēmi", "Neihana", "Arapera", "Leaf"]
index = 0
while index < len (names):
    print(names[index])
    index += 1

# better options # visit each item one at a time. exactly once starting from first
for name in names:
    print(name)

# count the occurence in string
sentence = " a small dog was barking all night"
vowel = "aeiou"
number_of_vowels = 0

for letter in sentence :
    if letter in vowel:
        number_of_vowels += 1

print(number_of_vowels)

# ----- range function

for number in range(1,31):
    print(number)

number = list(range(1,31)) # make it a list
print(number)

# ----- 
numbers = [1,2,4,5,76,8,9,23,99]

nines = numbers.count(9)

print(nines)


# count freq of word
sentence = "haere mai, haere atu, haere, haere"
print(sentence)
words = sentence.count("haere") + 0

print(words)

# change one word anywhere
changed = sentence.replace("atu", "mai")
print(sentence)


# =================
#PLAY!
# =================


# =========================================================================================================

# =================
# exercise 2
# =================

# Fix the code
print("Simeoni")
print("Juhani")
print("Eero")
print("Lauri")
print("Aapo")
print("Tuomas")
print("Timo")

#fixed
names = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
names_sorted = names.sort()
print(names_sorted)

brothers = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
brothers_sorted = sorted (brothers)
print(brothers_sorted)

brothers = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
brothers_sorted = sorted (brothers)
print(brothers_sorted)
print(sorted(brothers))

#GOLD!
brothers = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
sorted_brothers = sorted(brothers)
index = 0
while index < len(sorted_brothers):
    print(sorted_brothers[index])
    index += 1

#exercise 3
#Sample output
"""Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream."""

#GOLD!
print("Row, row, row your boat,", "Gently down the stream.", "Merrily, merrily, merrily, merrily,", "Life is but a dream.", sep="\n")

#exercise 4
minutes_in_hour = 60
hour_in_day = 24
days_in_year = 365

time = ((minutes_in_hour * hour_in_day) * days_in_year)

print(time)

# END
