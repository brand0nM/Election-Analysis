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
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""


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
            candidate_votes[candidate_name] = 0 

        # Count amount of entries that aren't unique
        else:
            candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    print(f"{candidate_name}: {vote_percentage}% ({votes:,})\n")
    winning_count = 0
    winning_percentage = 0
    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

# Close the file
election_data.close()