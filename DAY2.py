#learnnig data types , numbers and many more....
#tip calculator
print("Welcome to the tip calculator. \n")
totalbill = float(input("What was the total bill : "))
split = float(input("How many people to split the bill : "))
tip_percent = float(input("What percentage tip would you like to give for our service ? 10 , 12 , 15 : "))
per_person = (totalbill/split)
print("Each person should pay : " , per_person + per_person*tip_percent/100)
