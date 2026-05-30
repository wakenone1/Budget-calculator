Salary = int(input("Input your salary : "))
currency = input("Select currency : ")

pit1 = input("Majority expenses(Just type the name) : ")
percent1 = int(input("""Put majority percentage(Just put the integer value, no "%" sign needed) : """))
pit2 = input("Other expenses : ")
percent2 = int(input("""Put the expenses percentage(Just put the integer value, no "%" sign needed) : """))
pit3 = input("Savings : ")
percent3 = int(input("""Put savings percentage(Just put the integer value, no "%" sign needed) : """))

budgets = [pit1, pit2, pit3]

percentage = [Salary * percent1 / 100, Salary * percent2 / 100, Salary * percent3 / 100]

print(f"""Monthly salary - {Salary} {currency}

{budgets[0]} - {percentage[0]} {currency}
{budgets[1]} - {percentage[1]} {currency}
{budgets[2]} - {percentage[2]} {currency}""")



