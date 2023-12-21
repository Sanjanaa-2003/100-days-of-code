names_string=input("Enter the list of names:")
names = names_string.split(',')
import random
# num_items = len(names)
# random_choice=random.randint(0,num_items-1)
random_choice=random.randint(0,len(names)-1)
person_who_is_going_to_pay = names[random_choice]
print(person_who_is_going_to_pay+" is going to pay for the next treat.")

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work,
# you must enter all the names as names followed by comma then space. e.g. name, name, name
#HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]
#
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output
# Michael is going to buy the meal today!
# Hints
# You might need the help of the len()
# function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
#
# Remember that Lists start at index 0!