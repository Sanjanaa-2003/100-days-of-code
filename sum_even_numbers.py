target = int(input()) # Enter a number between 0 and 1000
sum=0
for num in range(2,target+1,2):
     #if num%2==0:      not necessary
       sum += num
 print(sum)

# ALTERNATE
# target = int(input()) # Enter a number between 0 and 1000
# sum=0
# for num in range(1,target+1):
#     if num%2==0:
#         sum+=num
# print(f"{sum}")