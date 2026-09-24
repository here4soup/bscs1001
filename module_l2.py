# /// 
# module name:      1001 lecture
# desc:             tasks and play for lecture per name, and any exercises
#
# version:          v1.0
# major versions:   2026 09 19    -   V1.0 Initial version
# dependencies: 
#   none
# keys: 
#       #PLAY!          (play with task)
#       #LEARN!         (learnings stated) 
#       #TODOLATER      (things to learn later)\
#       #CORRECT!       (this vsnippet is correctly working)
#       #PREF!          (this is my preferred method)
# ///

# =========================================================================================================
# =================
# tutorial
# =================



# ===== 1. format a derived number

num = 1 / 3 # set a look up
print(f"{num:.2f}") # format the output

## #PLAY! 
print(f"{num:.10f}") 

num = 0.255 # 
print(f"{num:.2f}") 
print(f"{num:.1f}") 
print(f"{num:.10f}") #LEARN! adds tail zeroes



# ===== 2. nested conditional statement

# system: initiate prompt
number = int(input("Give a number: ")) # task the system to prompt input

# user: whakautu in terminal

# system: process the response
if number >= 0: # nested conditional statement
    if number % 2 == 0: 
        print("Number is even")
    else: 
        print("Number is odd")
else: 
    print("Number was negative")



## --- #PLAY!
# ----- format and swap vales of variables
number = (input("Give a number: ")) #LEARN! returns an error because needs to recognise whakautu as number
print(number + 100)

number = int(input("Give a number: ")) #CORRECT!
print(number + 100)

# longer option
message = (input("Give a number: ")) # ask
number = int(message) # convert to valid format
print(number + 100) # PASS

x, y = input("Enter two numbers (with no punctuation): ").split()
# whakautu
print(x, y)
x, y = y, x # swap them
print(x, y) # see them swapped

a = b = c = 100 # makes all of these variables 100 i.e. shared reference
print(a, b, c)

# delete things from the environment
print(a)
del a
print(a)


# calc percentages too
points = int(input("how many points have you got: ")) 

# set options in code rather than terminal
points = 105 
points = 95



# ----- tuarua condition statement play
if points < 100: 
    points * 1.10
else: 
    points * 1.15

# conditional with a derivation #CORRECT!
if points < 100: 
    derived_points = points*1.00 # derive a new column, still calc
else: 
    derived_points = points*2.00

# print it
# o1 #CORRECT! #PREF!
print(f"You have {derived_points:.1f} points") # #LEARN! show the result. '(f' is Formatted String Literals
# o2
print("You have {} points.".format(derived_points)) # #LEARN! use .format
# o3
print("You have " + str(derived_points) + " points") # #LEARN! use string adding but have to set numeric value as string

print("You have ", str(derived_points), " points") # comma option


# ----- tuatoru condition statement play 
''' if points < 90: derived_points = points*1.00 
elif points >= 90 and < 100: derived_points = points*2.00 #INCORRECT
else: derived_points = points*3.00 '''

# set lookups
threshold_one       = 50
threshold_two       = 70
threshold_three     = 90
decimal_select = 0 #TODOLATER
points = 93
points = 73
points = 43

# two conditions
if points >= threshold_three: 
    print(f"equal to or more than {threshold_three:.0f}")
else:
    print(f"less than {threshold_three:.0f}")

# three conditions #CORRECT!
if points >= threshold_three:
    derived_points = points*3.00 
elif points >= threshold_two:
  derived_points = points*2.00
else:
  derived_points = points*1.00

print(f"You have {derived_points:.0f} points") 



# ----- three conditions + nest as same as above but not optimised
points = 73
if points >= threshold_three:
    derived_points = points*3.00 
elif points >= threshold_two:
    if points < threshold_three: # works like an AND condition with the elif above to ceate BETWEEN
        derived_points = points*100.00 
    else: derived_points = points*0 # does expected behaviour but isn't optimised
else:
  derived_points = points*1.00

print(f"You have {derived_points:.0f} points") 

#LEARN! we don't need this "between" option because IF will sequence through:
#  if [very hot porridge] then do [blow on porridge]. else [where not very hot porride] if medium hot porridge then [eat]. then assume all else is cold porridge



# other option to treat highs and lows #CORRECT! #PREF
points = 73
if points >= threshold_three:
    derived_points = points*3.00 
elif points < threshold_one:
  derived_points = points*1.00
else:
  derived_points = points*2.00

print(f"You have {derived_points:.0f} points") #still treats the medium score as expected


# ----- treating numbers
number = 10
number = 0
number = -5

if number < 0:
    print("tau tōraro")

if number > 0:
    print("tau tōraro kore")


# treatment examples
number = number * -1
number *= -1 # means number = number * -1. Ie SHORT way
number = -number # by itself

print(number)


print(f"The absolute value of te tau is {number}")

# assess via optional branch with else statement

if number < 0:
    number *= -1
    print("i tuku mai koe i tētahi >tau tōraro<") 
else: # replace "if number > 0:" with else. 
    print("i tuku mai koe i tētahi tau tōraro >kore<") # reo = non-negative


# LEARN! sensitive to horizontal white space; affects the code, indicates blocks to python. vertical okay


if number < 0:
    number *= -1 # treat the negative
    print("i tuku mai koe i tētahi >tau tōraro<") # negative
elif number > 0: # cant do else if, has to be elif.
    print("i tuku mai koe i tētahi tau tōraro >kore<") # reo = non-negative
print(f"The absolute value of number is {number}")



# some treatment options
number % 2  # divide by specified number and return the remainder. 
            # eg 6/2=0, but 5/2=1 (one is left over / can't be split)
            # can use this to identify even numbers and odd numbers



# assess whether tau taurua (even), tau taukē
if number == 0:
    print("zero") # tau kore?
elif number % 2 == 0: # modular operator?? modal operator?
    print("tētahi tau taurua!")
elif number % 2 != 0:
    print("tētahi tau taukē")
else:
    print("hmmm")

    # REMINDER! if you end with zero clause, then condition becomes unreachable

print(number)

# another eg
if number < 0:
    print("he tau tōraro")
elif number == 0:
    print("tau kore")
elif number % 2 == 0:
    print("he tau taurua!")
else: # you don't need an else statement SEE BELOW
    print("he tau taukē") 

# another eg
if number < 0:
    print("he tau tōraro")
elif number == 0:
    print("tau kore")
elif number % 2 == 0:
    print("he tau taurua!")
elif number % 2 != 0: # you don't need an else statement
    print("he tau taukē") 
# end



# --- nested conditional statements

age = int(input("e hia ōu tau?"))

# bad-practice eg
if age >= 40:
    if age <75:
        print("you can be Pirimia")
    else:
        print("you can't be Pirimia...")
else:
    print("you can't be Pirimia...")



# better practice eg: use logical operator
age = int(input("e hia ōu tau?"))
age = 57

if age >= 18 and age < 65:
    print("you can be Pirimia")
else:
    print("yeah nah")

# other ways of saying the same first sentence
# if age >= 18 and age < 65:
# if 18 <= age < 65

name = "Trump"
age = 89
name = "Mamdani"
age = 51

if name != "Trump" and (age >= 18 and age < 65):
    print("you can be Pirimia")
else:
    print("yeah nah")



# --- while statements
while True:
    age = int(input("e hia ōu tau? (0 stops the progamme)"))

    if age == 0:
        break
    
    if age >= 18 and age < 65:
        print("you can be Pirimia")
    else:
        print("yeah nah")


# =========================================================================================================
# =================
# exercise 1
# =================

print("Hi there!")
print("Haere mai ki te whare")
print("Kia pai Te Wiki o te Reo Māori")

#LEARN!
# SHIFT + ENTER = runs line
# CTRL + F5 = runs entire code


# END
