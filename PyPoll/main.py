import os
import csv

election_data = os.path.join("election_data.csv")

# Make an empty list to capture the names of candidates
candidates = []

# Make an empty list to capture the number of votes each candidate receives
num_votes = []

# Make an empty to capture the percentage of total votes each candidate garners 
percent_votes = []

# Create a counter for the total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to vote-counter 
        total_votes += 1 

        '''
        If the candidate is not on our list, add his/her name to our list, along with 
        a vote in his/her name.
        If he/she is already on our list, we will simply add a vote in his/her
        name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Display results
print("Election Results")
print(f"Total Votes: {str(total_votes)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print(f"Winner: {winning_candidate}")

# Export to txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = str(f"Total Votes: {str(total_votes)}")
output.write('{}\n{}\n'.format(line1, line2))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = str(f"Winner: {winning_candidate}")
output.write('{}\n'.format(line5))
