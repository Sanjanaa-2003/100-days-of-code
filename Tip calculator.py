print("Welcome to the tip Calculator!")
bill=float(input("What was the total bill?"))
tip=int(input("WHat percentage tip would you like to give? 10,12 or 15?"))
tip_percentage=tip*bill/100
people=int(input("How many people to split the bill?"))
bill_perperson=(bill+tip_percentage)/people
final_bill=round(bill_perperson,2) #Rounds off upto 1 decimal if second decmal is 0
final_bill="{:.2f}".format(bill_perperson) #Rounds exactly upto 2 decimals
print(f"Each person should pay {final_bill}")
