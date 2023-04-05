#!/usr/bin/env python
# coding: utf-8

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


# Set in Python
# 
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

