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



## #PLAY!
number = (input("Give a number: ")) #LEARN! returns an error because needs to recognise whakautu as number
print(number + 100)

number = int(input("Give a number: ")) #CORRECT!
print(number + 100)

# longer option
message = (input("Give a number: ")) # ask
number = int(message) # convert to valid format
print(number + 100) # PASS



# calc percentages too
points = int(input("how many points have you got: ")) 

# set options in code rather than terminal
points = 105 
points = 95



# tuarua condition statement play
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



# tuatoru condition statement play 
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



# three conditions + nest as same as above but not optimised
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


# END
