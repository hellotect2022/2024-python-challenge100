print("Welcome to the thip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
peoples = int(input("How many people to split the bill? "))

# Convert inputs to float
total = bill + (bill*tip_percent/100)
individual = total/peoples

print("######## BILL ##########")
print(f"## TOTAL : {round(total,2)}$")
print(f"## PEOPLES : {peoples}")
print(f"## INDIVIDUALS : {round(individual,2)}$")
print("######## ---- ##########")