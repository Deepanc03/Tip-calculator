print("welcome to tip calculator")
totalbill =float(input("what was the total bill? $ "))
per =int(input("what is the percentage of your tip? - 10,12,15: "))
stotal =int(input("How many people you like to split the bill? "))
tip = totalbill * (per / 100)
total = tip + totalbill
famot = total/stotal
# famot = round(famot , 2 )
famot = "{:.0f}".format(famot)
print(f"Each person should pay ${famot}")
