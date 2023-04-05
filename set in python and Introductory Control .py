#!/usr/bin/env python
# coding: utf-8

# Set in Python
# 
# 

# In[1]:


sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
print(sentence, "\n")

# split sentence into list of words
sentence_list = sentence.split()
print(sentence_list, '\n')

# convert list to set to get unique words
sentence_set = set(sentence_list)
print(sentence_set, '\n')

# print the number of unique words
num_unique = len(sentence_set)
print(num_unique, '\n')


# Introductory Control
# 
# 
# Problem Statement- I
# Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.
# 
# Steps to Follow: 
# Understand how net run rate getting calculated (Cite the reference in submission comment)
# Follow the computational thinking process.
# Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
# Design Controls -  Compound Statements and Suites
# Provide Feedback to the User (Console level Feedback)
# Test (Paper Calculation)
# Validate (Paper Calculation = Code  Result)
# Problem Statement- II
# We have three categories to check. If the sum of divisors is greater than a number, the number is
# abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
# be perfect design control structure for this problem statement
# 
# #Nint=28 # Number to be validated 
# #Div=1    #Divisor
# #while Div<Nint:
# #   if Nint % Div==0:
# #        print(Div) # Suit1
# #Div=Div+1  # Suit 2
# 
# Note: Don't use unnecessary imports.
# 
#  Submission Guidelines: File Upload (Notepad File, Python File, Console Output Pasted)  and Citation of reference in the submission comment section.
# 
# Academic Integrity: Plagiarism is an offense and doesn't try to involve in such malpractices.
# 

# In[2]:


# This program calculates the net run rate for two cricket teams
# and handles the tie-breaker condition if necessary

# Function to calculate net run rate
def calculate_nrr(runs_scored, overs_played, runs_conceded, overs_faced):
    nrr = ((runs_scored / overs_played) - (runs_conceded / overs_faced))
    return nrr

# Inputs required for the program
team1_name = input("Enter team 1 name: ")
team2_name = input("Enter team 2 name: ")
team1_runs_scored = int(input("Enter team 1 runs scored: "))
team2_runs_scored = int(input("Enter team 2 runs scored: "))
team1_overs_played = int(input("Enter team 1 overs played: "))
team2_overs_played = int(input("Enter team 2 overs played: "))
team1_runs_conceded = team2_runs_scored
team2_runs_conceded = team1_runs_scored
team1_overs_faced = team2_overs_played
team2_overs_faced = team1_overs_played

# Calculate net run rate for both teams
team1_nrr = calculate_nrr(team1_runs_scored, team1_overs_played, team1_runs_conceded, team1_overs_faced)
team2_nrr = calculate_nrr(team2_runs_scored, team2_overs_played, team2_runs_conceded, team2_overs_faced)

# Determine the team with higher net run rate
if team1_nrr > team2_nrr:
    print(team1_name, "tops the points table with a net run rate of", team1_nrr)
elif team2_nrr > team1_nrr:
    print(team2_name, "tops the points table with a net run rate of", team2_nrr)
else:
    # Handle the tie-breaker condition
    print("Both teams have the same net run rate. The team with the higher runs scored wins.")
    if team1_runs_scored > team2_runs_scored:
        print(team1_name, "tops the points table")
    else:
        print(team2_name, "tops the points table")

