# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

input_path = os.path.join("PyBank/Resources/budget_data.csv")
output_path = os.path.join("PyBank/analysis/budget_analysis.txt")

# Define Variables
total_months = 0
total_net = 0

previous_month = 0
current_month = 0 
total_change = 0

greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Open and read the csv
with open(input_path) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    csv_header = next(reader)

    # Process each row of data
    for row in reader:
        # Print Total Months
        total_months += 1
        date = row[0]
        current_month = int(row[1])
        total_net += current_month       

        # Track the net change
        if total_months == 1:
            previous_month = int(row[1])
        else:
            current_month = int(row[1])
            change = current_month - previous_month
            total_change += change 
           
            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date


            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

        # Reset
        previous_month = current_month

# Print the output
output = f"""
Financial Analysis
--------------------------------------------------------
Total Months: {total_months} 
Total Net: ${total_net}
Average Change: ${total_change / (total_months - 1)}
Greatest Increase in Profits: {greatest_increase_date} $ {greatest_increase} 
Greatest Decrease in Profits: {greatest_decrease_date} $ {greatest_decrease} """
        
print(output)  

# Write the results to a text file
with open(output_path, "w") as txt_file:
    txt_file.write(output)

