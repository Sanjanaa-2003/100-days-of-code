# #To calculate the number of weeks left from current age if a person lives upto 90 years
# age = input("Enter your age:\n")
# age_as_int=int(age)
# life=90-age_as_int
# weeks_left=life*52
# print(f"You have {weeks_left} weeks left.")

a = int(input("Your current age: "))
years = 90
weeks = 52*90
days = 365*90
years_left = 90 - a
months_left = years_left*12
weeks_left = weeks - (a*52)
days_left = days - (a*365)
print(f"You have {years_left} years, {months_left} months, {weeks_left} weeks and {days_left} days left")

# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
#
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
#
# Example Input
# 56
# Example Output
# You have 1768 weeks left.
