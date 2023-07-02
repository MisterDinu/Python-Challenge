import pandas as pd
import csv
from pathlib import Path

# Here starts the FIRST challenge

# Creating the path to the file, and a df to read the file
file= Path("C:\\Users\\Usuario\\Desktop\\Butucamopo\\MisterHacker\\Python challenge\\PyBank\\Resources\\budget_data.csv")
df_1=pd.read_csv(file)

# print(df_1.header())

print()
# Print in the example's format
print("Financial Analysis")
print("-------------------------")

# To determine the total of months, I use len function to count the total of unique values in that column
months=len(df_1["Date"].unique())
print(f'Total months: {months}')

# For the total amount of the proffit/losses, I use the sum function to add every value and print the result
Total_profit=sum(df_1["Profit/Losses"])
print(f'Total: ${Total_profit}')

# To get the changes over the entire period, I get the first and last value of Profit/Losses
# and get the difference between them using the iloc function.
first_value=df_1["Profit/Losses"].iloc[0]
last_value=df_1["Profit/Losses"].iloc[-1]

# To get the average I can divide the result between the change over period and the total number
# of values in the column
change_over_period=last_value-first_value
average_change=change_over_period/len(df_1["Profit/Losses"])

# Print print print
print(f'Change Overall:${change_over_period}')
print(f'Average change:${average_change}')

# To determine the greatest increase and decrease I use the function max and min and make a
# reference in "greatest increase/decrease" to use it at the print.
greateast_increase=df_1["Profit/Losses"].max()
greateast_decrease=df_1["Profit/Losses"].min()

# To get the date of the increase and decrease, I use the function loc and the idxmin/idxmax
# to get index of the minimum and maximum value, and then get the value at the 'Date' column 
date_decrease = df_1.loc[df_1["Profit/Losses"].idxmin(), 'Date']
date_increase = df_1.loc[df_1["Profit/Losses"].idxmax(), 'Date']

# Then print with the example's format
print(f'Greatest increase in Profits: {date_increase} (${greateast_increase})')
print(f'Greatest decrease in Profits: {date_decrease} (${greateast_decrease})')

# To export results in a new txt file, I create it with a reference to a new txt file, so it's created.
new_file="C:\\Users\\Usuario\\Desktop\\Butucamopo\\MisterHacker\\Python challenge\\budget_results.txt"

# Then, to write in it, i use with open, with a "w", as a result2, and then use the function write to
# put all the information requested in the file.
with open(new_file, "w") as results:
    results.write("Financial Analysis"+'\n')
    results.write("-------------------------"+'\n')
    results.write('\n')
    results.write(f'Total months: {months}'+'\n')
    results.write(f'Total: ${Total_profit}'+'\n')
    results.write(f'Change Overall:${change_over_period}'+'\n')
    results.write(f'Average change:${average_change}'+'\n')
    results.write(f'Greatest increase in Profits: {date_increase} (${greateast_increase})'+'\n')
    results.write(f'Greatest decrease in Profits: {date_decrease} (${greateast_decrease})'+'\n')


# Here starts the SECOND challenge

# Set the path
file2= Path("C:\\Users\\Usuario\\Desktop\\Butucamopo\\MisterHacker\\Python challenge\\PyPoll\\Resources\\election_data.csv")
df_2=pd.read_csv(file2)

# print(df_2.header())

print()

# Set format:
print('Election Results')
print("-------------------------")

# Set total votes into a variable
total_votes=len(df_2["Ballot ID"])

# I first print the lenght of the votes 
print(f'Total Votes: {total_votes}')
print("-------------------------")

    # And to get rid of the empty cells y use dropna (because i need a clean version to do the task of creating 
    # a complete list of candidates who received votes)
    # df_2_clean= df_2.dropna()

    # I then print the lenght of the votes in the new df, but it doesnt changes, so I comment the dropna code since 
    # there are not empty cells 
    # print(len(df_2_clean['Ballot ID']))

# To get the candidates list, I use the unique function, at the 'Candidate' column
candidates=df_2['Candidate'].unique()

# To get the total of votes, I use .value_counts at the 'candidate' column, searching for the ones matching the 
# first candidate. I do that for each candidate.
charles_count = df_2[df_2['Candidate'] == 'Charles Casper Stockham']['Candidate'].value_counts().values[0]

# And to get the percentage of votes, I multiply the count of the candidate for 100 and divide the result between
# the total of votes, then use the round function to show only 3 decimals. I do that for each caniddate.
charles_percentage=round(charles_count*100/total_votes, 3)

diana_count = df_2[df_2['Candidate'] == 'Diana DeGette']['Candidate'].value_counts().values[0]
diana_percentage=round(diana_count*100/total_votes, 3)

raymon_count = df_2[df_2['Candidate'] == 'Raymon Anthony Doane']['Candidate'].value_counts().values[0]
raymon_percentage=round(raymon_count*100/total_votes, 3)

# print results
print(f'{candidates[0]}: {charles_percentage}% ({charles_count} votes)')
print(f'{candidates[1]}: {diana_percentage}% ({diana_count} votes)')
print(f'{candidates[2]}: {raymon_percentage}% ({raymon_count} votes)')
print("-------------------------")
winner=df_2['Candidate'].value_counts().idxmax()
print(f'Winner: {winner}')

# To export results in a new txt file, I create it with a reference to a new txt file, so it's created.
new_file2="C:\\Users\\Usuario\\Desktop\\Butucamopo\\MisterHacker\\Python challenge\\election_results.txt"

# Then, to write in it, i use with open, with a "w", as a result2, and then use the function write to
# put all the information requested in the file.
with open(new_file2, "w") as results2:
    results2.write('Election Results'+'\n')
    results2.write('\n')
    results2.write("-------------------------"+'\n')
    results2.write(f'Total Votes: {total_votes}'+'\n')
    results2.write('\n')
    results2.write("-------------------------"+'\n')
    results2.write(f'{candidates[0]}: {charles_percentage}% ({charles_count} votes)'+'\n')
    results2.write(f'{candidates[1]}: {diana_percentage}% ({diana_count} votes)'+'\n')
    results2.write(f'{candidates[2]}: {raymon_percentage}% ({raymon_count} votes)'+'\n')
    results2.write('\n')
    results2.write("-------------------------"+'\n')
    results2.write(f'Winner: {winner}')