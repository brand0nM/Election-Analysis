# Election Analysis
## Project Overview
We've been hired to audit the local election; this requires reading a csv file to determine the total number of cast votes for each candidate, then exporting these results to a txt file. 

### Purpose
Using python this project reads an unpathed csv file, stores it's data in a list of dictionaries, counts and prints the results using for loops and if statements, then prints the results in the terminal and writes them to a text file. 

## Results

<img width="806" alt="Terminal" src="https://user-images.githubusercontent.com/79609464/160296360-0f02842e-6b1c-49e1-be73-0b4fb18bf8b9.png">
<img width="308" alt="Text File" src="https://user-images.githubusercontent.com/79609464/160296361-6a18d68b-41d0-40da-89fa-77850d3300c9.png">

## Summary

Python is a powerful and reuseable tool. With slight modifications the algorithms behind this project can be recycled for years to come. 
1) Confirm the New_Election_Results.csv's second column has the election's counties and the third column has the candidates name.
2) Change the unpathed read to argue ("New_Folder", "New_Election_Results.csv"); this is located on line 9 of our code
<br /> 
Now we can reuse this algorithm to count any election!
