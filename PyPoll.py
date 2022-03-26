# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create empty containers
candidate_options = []
voties = []
percenties = []
candidate_votes = {}

with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Iterate over data set to find subcategories and totals
    for row in file_reader:

        #start total votes counter
        total_votes += 1

        # Append Unique Candidates to List
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #initialize candidate vote counter in our dictionary
            candidate_votes[candidate_name] = 1 

        # Count amount of entries that aren't unique
        else:
            candidate_votes[candidate_name] += 1

    # Loop over data set to print our results
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        voties.append(votes)
        percenties.append(vote_percentage)
    
    winning_count = max(voties)
    winning_percentage = max(percenties)

    for candidate_name in candidate_votes:
        if (votes >= winning_count) and (vote_percentage >= winning_percentage):
             # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
        else:
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    

# Close the file
election_data.close()