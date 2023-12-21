height_of_students=input("enter heights:")
print(height_of_students)
#'10' '20' '30'
# height_list=list(height_of_students)
# print(height_list)
height_list=list(height_of_students.split(','))
# height_list=list(height_of_students.split())
print(height_list)
#['10' '20' '30']

for i in range(0,len(height_list)):
    height_list[i] = int(height_list[i])
    #[10 20 30]
print(height_list)
no_of_students=0
for each_student in height_list:
    #10 --- 1
                        #20 --- 1+1=2
    #30 --- 2+1 = 3
    no_of_students += 1
print(f"The total no of students are: {no_of_students}")
#3

heights=0
for each_height in height_list:
    #10
    #10+20 = 30
    #30+30 = 60
    heights += each_height
print(f"The sum of heights are: {heights}")
#60

average = heights/no_of_students
#60 / 3 == 20
print(f"THe average height is {average}")
print(f"THe average height is {round(average)}")













#METHOD1
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
# print(f"average height = {average_height}")







# METHOD 2
height = input("Enter the heights:")
#100 120 130 140 150
height_list = height.split()
count = 0
for height in height_list:
    count += 1
print("The number of heights is:" ,count)
for i in range(count):
    height_list[i] = int(height_list[i])
total = 0
for person in height_list:
    total += person
print("The total is:",total)
avg = total / count
print("The average is:",(round(avg)))



# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
# e.g.
#
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
# There are a total of 7 heights in student_heights
#
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
#
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
#
# Example Input 1
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
#
# Example Output 1
# total height = 857
# number of students = 5
# average height = 171
# Example Input 2
# 151 145 179
# Example Output 2
# total height = 475
# number of students = 3
# average height = 158
