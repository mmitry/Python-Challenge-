# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
input_path = os.path.join("PyPoll/Resources/election_data.csv")
output_path = os.path.join("PyPoll/analysis/election_analysis.txt")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
candidate_count = 0
candidate_percentage = 0

# Open the CSV file and process it
with open(input_path) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1
    

        # Get the candidate's name from the row
        candidate_name = row[2]
    
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1



    # Write the total vote count to the text file

    output = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    """

    # Loop through the candidates to determine vote percentages and identify the winner

    # Calculate Vote Percentage
    for candidate, votes in candidate_votes.items():
        candidate_percentage = (votes / total_votes) * 100
        
        # Calculate the Winner
        if votes > candidate_count:
            candidate_count = votes
            winning_candidate = candidate
            candidate_percentage = candidate_percentage

        output += f"\t{candidate}: {candidate_percentage:.2f}% ({votes})\n"
        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary
    winner = f"""
    -----------------------------
    Winner: {winning_candidate}"""

    output += winner
    # Print the summary
   
print(output)


# Write the results to a text file
with open(output_path, "w") as txt_file:
    txt_file.write(output)