Salary = int(input("Input your salary(Intership money) : "))#PaidInternship
pit1 = input("Majority expenses(Just type the name) : ")
pit2 = input("Other expenses : ")
pit3 = input("Savings : ")

budgets = [pit1, pit2, pit3]

percentage = [Salary * .70, Salary * .20, Salary * .10]

print(f"""Monthly salary - {Salary} taka

{budgets[0]} - {percentage[0]} taka
{budgets[1]} - {percentage[1]} taka
{budgets[2]} - {percentage[2]} taka""")



