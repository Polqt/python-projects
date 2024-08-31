#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_tip_bill = (float(bill) * (int(tip) / 100))
total_bill = (float(bill)) + float(total_tip_bill)
split_bill = round(total_bill / int(people), 2)
final_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay {final_bill}.")