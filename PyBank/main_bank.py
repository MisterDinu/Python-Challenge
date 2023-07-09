# I import csv module to use csv reader
import csv

# Giving format to the terminal output
print("Financial Analysis")
print("----------------------------")

# I use with open with a relative path to access budget_data.csv
with open(r'PyBank\\Resources\\budget_data.csv', 'r') as file:
    financial_analysis=csv.reader(file, delimiter=",")
    next(financial_analysis)

    # I create two empty lists in which I will put all the months in the first column,
    # and all the profits/losses in the second column
    months=[]
    budget_list=[]

    # Using for, and append, I put the months and profit losses in the lists.
    for w in financial_analysis:
        count=w[0]
        months.append(count)
        budget=w[1]
        budget_list.append(int(budget))
        # I use min and max to get the minimum and maximum values at "budget_list"
        minimum=min(budget_list)
        maximum=max(budget_list)

    # With len I count the total of months
    months_count=len(months)

    # I get the difference between the last and the first value of budget_list
    # In order to get the average change
    changes=budget_list[-1] - budget_list[0]
    average_change=changes/months_count

    # I use sum to get the total budget
    total_budget=sum(budget_list)

    # I use index, to identify the position of the minimum and maximum value of budget_list
    # Then, with the position, I search for that at the months list, in order to get the
    # month of a higher and a lower profit.
    lower_month_index=budget_list.index(minimum)
    greatest_month_index=budget_list.index(maximum)
    lower_month=months[lower_month_index]
    greatest_month=months[greatest_month_index]

# Print everything at format

print(f'Total months:{months_count}')
print(f'Total: ${total_budget}')
print(f'Average change: ${average_change}')
print(f'Greatest increase in Profits: {greatest_month} (${maximum})')
print(f'Greatest decrease in Profits: {lower_month} (${minimum})')

# declare a new_file variable to create a new txt file.
new_file="PyBank\\Analysis\\budget_analysis.txt"

# Then I use with open in writer mode in order to write the previous prints in there.
with open(new_file, 'w') as results:
    results.write("Financial Analysis\n")
    results.write("----------------------------\n")
    results.write(f'Total months:{months_count}\n')
    results.write(f'Total: ${total_budget}\n')
    results.write(f'Average change: ${average_change}\n')
    results.write(f'Greatest increase in Profits: {greatest_month} (${maximum})\n')
    results.write(f'Greatest decrease in Profits: {lower_month} (${minimum})')
