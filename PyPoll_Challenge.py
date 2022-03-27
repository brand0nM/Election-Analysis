# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add dependencies
import csv
import os

# variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate Options and votes
candidate_options = []
candidate_votes = {}

# County list and votes dictionary
county_list = []
county_votes = {}

# Initialize winning candidate, vote count and percentages
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# initialize largest county and voter turnout
largest_county = ""
winning_county = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Extract the county name from each row
        county_name = row[1]

        # If the candidate is unique add it to list
        if candidate_name not in candidate_options:

            # Add candidate name to the list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # If statement to check the county is unique
        if county_name not in county_list:
            # Add the county to our list of counties
            county_list.append(county_name)
                
            # Begin tracking the county's vote count
            county_votes[county_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


        # Add a vote to that county's vote count
        county_votes[county_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to terminal and write to text file
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # Retrieve the county vote count.
        county = county_votes.get(county_name)

        # Calculate the percentage of votes for the county.
        county_percentage = round(float(county) / float(total_votes) * 100, 1)

         # create county results variable.
        county_results = (f"{county_name}: {county_percentage}% ({county})\n")

         # Print and Save the county votes to a text file.
        print(county_results)
        txt_file.write(county_results)

         # Write an if statement to determine the winning county and get its vote count.
        if (county > winning_county) and (county_percentage > winning_county_percentage):
            winning_county = county
            largest_county = county_name
            winning_county_percentage = county_percentage

    # Print county with the largest turnout to the terminal and save to text file
    Phat_county = (f"-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n")
    print(Phat_county)
    txt_file.write(Phat_county)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
