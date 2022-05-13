# python-challenge - Python Bootcamp Assignment

Complete two challenges to apply Python skills. 

## Background

Welcome to the world of programming with Python. In this assignment, I used the concepts learnt to complete **two** Python challenges, PyBank and PyPoll.

## Setup

Before starting the assignment I made sure to do the following:

* Create a new repository for this project called `python-challenge`.

* Clone the new repository to my computer.

* Inside my local git repository, create a directory for each Python challenge. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder created, add the following:

  * A new file called `main.py`. This is the main script to run each analysis.
  * A `Resources` folder that contains the CSV files used. Making sure the script has the correct path to the CSV file.
  * An `analysis` folder that contains a text file that has the results from my analysis.

* Push these changes to GitHub.

## PyBank Instructions

In this challenge, I was tasked with creating a Python script to analyze the financial records of a company. I was given a set of financial data called **budget_data.csv** (PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, the company has rather lax standards for accounting, so the records are simple.)

First task was to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

Analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```

In addition, the final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll Instructions

In this challenge, I was tasked with helping a small, rural town modernize its vote counting process.

I was given a set of poll data called **election_data.csv** (PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". My task was to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

Analysis should look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

In addition, the final script should both print the analysis to the terminal and export a text file with the results.
