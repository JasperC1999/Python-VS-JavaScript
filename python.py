


# --------------- PYTHON DATA TYPES -------------------
#------------------------------------------------------


# string = "string"
# print(string + ' is ' + str(type(string)))

# number = 1
# print(str(number) + ' is ' + str(type(number)))

# decimal = 1.4
# print(str(decimal) + ' is ' + str(type(decimal)))

# boolean = True
# print(str(boolean) + ' is ' + str(type(boolean)))

# array = []
# print(str(array) + ' is ' + str(type(array)))

# object = {}
# print(str(object) + ' is ' + str(type(object)))

# null = None
# print(str(null) + ' is ' + str(type(null)))


#------------------PYTHON CONDITIONALS --------------------
#----------------------------------------------------------

#------------PART ONE ----------------------------------
# num1 = 1
# num2 = 2


# if num1 == num2 : # 'is' also works
#   print(str(num1) + ' is equal to ' + str(num2))

# if num1 != num2 : # 'is not' also works
#   print(str(num1) + ' is not equal to ' + str(num2))

# if num1 < num2 :
#   print(str(num1) + ' is less than ' + str(num2))

# if num1 > num2 :
#   print(str(num1) + ' is greater than ' + str(num2))


# #------------PART TWO ----------------------------------


# variable = 'string'

# if str(type(variable)) == "<class 'int'>" :
#   print('variable is type int')
# elif str(type(variable)) == "<class 'str'>" :
#   print('variable is type str')
# else :
#   print('variable is not type int or type str')


#--------------- PYTHON LOOPS --------------------------
#-------------------------------------------------------


# list = ['JavaScript', 'Python', 'Jasper', 'Tim', 'Jay']

# ####################
# for string in list :
#   print(string)

#############################
# for n in range(len(list)) :
#   print(n)


#----------------PYTHON FUNCTIONS--------------------------
#----------------------------------------------------------


# def add(a, b) :
#   return a + b

# print(add(1, 2))


#--------------ROCK PAPER SCISSORS EXAMPLE-----------------
#----------------------------------------------------------

# TO-DO: WRITE ROCK PAPER SCISSORS FUNCTION----------------

# def rockPaperScissors(n) :
#   permutations = []
#   plays = ['R', 'P', 'S']
#   def loop(string) :
#     if (len(string) == n) :
#       permutations.append(string)
#       return
#     for play in plays :
#       loop(string + play)
#   loop('')
#   return permutations


# print(rockPaperScissors(3))