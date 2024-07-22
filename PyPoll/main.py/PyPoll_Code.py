import os
import csv

#Set Path for CSV File
election_csv = os.path.join("..", "Resources", "election_data.csv")
#Set Path for Exporting Text File
analysis_path = os.path.join("..", "Analysis")
f = open(f"{analysis_path}/PyPoll_Code.txt" , "w")

#Set Variables
total_votes = 0
candidate_votes = {}

#Open CSV File
with open(election_csv, encoding= 'UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Find Total Number of Votes Cast
    for row in csv_reader:
         for row in csv_reader:
            total_votes += 1
            candidate = row[2]
            
         #Total Candidate Votes
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
# Print Total Votes results
print(f'Election Results')
print(f'-------------------------')
print(f"Total Votes: {total_votes}")
print(f'-------------------------')
print(f'Election Results', file= f)
print(f'-------------------------', file= f)
print(f"Total Votes: {total_votes}", file= f)
print(f'-------------------------', file= f)

#Calculate and Print Candidate Results
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    print(f"{candidate}: {percentage:.3f}% ({votes})", file= f)
print(f'-------------------------')
print(f'-------------------------', file= f)

# Determine the winner based on the most votes and Print
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print(f'-------------------------')
print(f"Winner: {winner}", file= f)
print(f'-------------------------', file= f)
