# AVERY DELPIT
# 02/10/2024
# P1HW2
# Trip Expenses Caluculator

print('This Program calculates and displays travel expenses')

Budget = int(input('Whats your budget?: '))
Travel_Destination = input('Where are you going?: ')
Gas = int(input('How much do you think you will spend on gas?: '))
Accomodation = int(input('Approximately, how much will you need for accomodation/hotel?: '))
Food = int(input('Last, how much do you need for food?: '))

print('-------Travel Expenses for the trip-------')
# I added a variable for the total expenses to keep track of the total expenses
total_expenses = 0
# I added a variable for the remaining budget to keep track of the remaining budget
remaining_budget = 0
# I added a variable for the total expenses to keep track of the total expenses
total_expenses = Gas + Accomodation + Food
# I added a variable for the remaining budget to keep track of the remaining budget
remaining_budget = Budget - total_expenses
# I added a print statement to display the total expenses and the remaining budget
print(f'Budget: ${Budget}')
print(f'Gas: ${Gas}')
print(f'Accomodation: ${Accomodation}')
print(f'Food: ${Food}')
print(f'Total expenses: ${total_expenses}')
print(f'Remaining budget: ${remaining_budget}')
# I added a print statement to display the travel destination and the total expenses
print(f'Travel destination: {Travel_Destination}')
# This is the end of the program the user can now see their total expenses and remaining budget. Also the 'f' string was used to format the output.