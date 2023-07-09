# I import csv module to use csv reader
import csv

# Giving format to the terminal output
print('Election Results')
print('-------------------------')

# I use with open with a relative path to access election_data.csv
with open(r"PyPoll\\Resources\\election_data.csv", 'r') as file:
    election_analysis= csv.reader(file, delimiter=',')
    next(election_analysis)

    # I create two empty lists in which I will put the id's of the voters, and
    # another one where I will put the candidates
    votes_id=[]
    candidates_list=[]
    
    # I use a for loop, and append to put all the votes, and all the names of the
    # candidates in there.
    for w in election_analysis:
        count_id= w[0]
        votes_id.append(count_id)
        names=w[2]
        candidates_list.append(names)

    # I use list and set, in order to create a new list without the repeated values
    # of candidates_list.
    candidates=list(set(candidates_list))
    total_votes=len(votes_id)
    candidate_0=candidates_list.count('Raymon Anthony Doane')
    percentage_0=round(candidate_0*100/total_votes, 3)
    candidate_1=candidates_list.count('Charles Casper Stockham')
    percentage_1=round(candidate_1*100/total_votes, 3)
    candidate_2=candidates_list.count('Diana DeGette')
    percentage_2=round(candidate_2*100/total_votes, 3)

winner = max(set(candidates_list), key=candidates_list.count)

# print everything at format
print(f'Total votes: {total_votes}')
print('-------------------------')
print(f'{candidates[0]}: %{percentage_0} ({candidate_0})')
print(f'{candidates[1]}: %{percentage_1} ({candidate_1})')
print(f'{candidates[2]}: %{percentage_2} ({candidate_2})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# declare a new_file variable to create a new txt file.
new_file="PyPoll\\Analysis\\election_analysis.txt"

# Then I use with open in writer mode in order to write the previous prints in there.
with open(new_file, 'w') as results:
    results.write('Election Results\n')
    results.write('-------------------------\n')
    results.write(f'Total votes: {total_votes}\n')
    results.write('-------------------------\n')
    results.write(f'{candidates[0]}: %{percentage_0} ({candidate_0})\n')
    results.write(f'{candidates[1]}: %{percentage_1} ({candidate_1})\n')
    results.write(f'{candidates[2]}: %{percentage_2} ({candidate_2})\n')
    results.write('-------------------------\n')
    results.write(f'Winner: {winner}\n')
    results.write('-------------------------')