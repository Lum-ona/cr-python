# VARIABLES
# - the type of variable is determined the value of that variable
name = 'Bruce' # String
age = 10  # index
isRaining = True # Boolean
gdp = 3.5 # float

# LIST
# - creating a list needs a square bracket[]
names = [] # empty list
temperatures = [12,34,54,34,64,2,14,46,31,3,31,23,23]
# - use the index number of an item to access an item in a list
# print(temperatures[0]) # get the first item
# print(temperatures[-1]) # get the last item
# print(temperatures[3: 7]) # get items from index number 3 to 6
# print(temperatures[2: -1]) # get all the items from index number 2 to the last one
# - add an item to the list in 2 ways, append(item) or insert(index, item)
temperatures.append(36) # 36 gets added at the end of the list
temperatures.insert(4, 57) # 57 gets added at index 4
# - you can delete an item from a list in two ways, del or pop
del temperatures[0] # item at index 0 gets deleted
deletedItem = temperatures.pop(5) # item at index 5 gets deleted... and it also gets returned..
                # basically, the deleted item is now stored in the variable deletedItem ( optionally to save)
# - Update an item in a list
temperatures[5] = 30 # the item at index 5 get updated to value 30
#  - know the length of a list by wrapping the list in len() method
# print(len(temperatures))


# # FOR LOOP
# # - use a loop to print each item individually
# for item in temperatures: 
#     print(item) # item is like a variable that gets reassigned to a new item 
#     # every time the loop loops untilt the loop ends
# # - u can range to print each item individually
# for index in range(len(temperatures)):
#     print(temperatures[index]) # index is a variable that gets reasigned to a 
#     # new index number every time the loop loops until the loop ends

# # CONDITIONAL STATEMENTS
# #  - if (condition): dos
# if(len(temperatures) < 10):
#     print('Its a short list')
# else: 
#     print('Its a long List')

# # - if/elif/else
# if (temperatures[0] == 34):
#     print('The day started hot!!')
# elif (temperatures[0] < 25):
#     print("The Day started really cold!1")
# else: 
#     print('Was an easy morning')

# # - nested if/elif/else
# if(temperatures [7] != 56):
#     print('maybe a cool or maybe excreemly hot afternoon')
#     if ( temperatures[7] <= 56):
#         print('It was a cool day')
#         # Add elif
#     else:
#         print('It was a hot day')
#         # if() Add ifs

# FUNCTIONS
# - functions in python need to be decleared (def)
# def nameOfTheFunction(parameters(optional)): dos
def primeNumbersDiv():
    # access each item individually.
    print('DIVISIBLITY TEST')
    for temp in temperatures:
        # - divisibility : can only be divided by one and itself.. dividing it with any other number will get a reminder
        # temp is the dividend
        # The divisior needs to be equal or less than the dividend
        for divisior in range(2, temp):
            if temp % divisior == 0:
                break
            else:
                print(f'Its a prime number: {temp}')
            break
primeNumbersDiv()

def primeNumbersMult():
    print('MULTIPLICATION TEST')
    # accessing each item 
    for index in range(len(temperatures)):
        product = temperatures[index]
        not_prime_numbers = []
        for multiplicand in range(2, product):
            for multiplier in range(2, product):
                if(multiplicand * multiplier == product):
                    not_prime_numbers.append(product)
                    break
            break
        if product not in not_prime_numbers:
            print(f'Its a prime number: {product}')
primeNumbersMult()
    




 

