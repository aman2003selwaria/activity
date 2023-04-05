#!/usr/bin/env python
# coding: utf-8

# Set in Python
# 
# 

# Problem - I 
# 
# sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"
# print(verse, "\n")
# 
# # split sentence into list of words
# sentence_list =  # You will have to fill out the function 
# print(sentence_list, '\n')
# 
# # convert list to set to get unique words
# sentence_set = 
# print(sentence_set, '\n')
# 
# # print the number of unique words
# num_unique = 
# print(num_unique, '\n')
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
# Exercises Rubrics
# Exercises Rubrics
# Criteria	Ratings	Pts
# Think
# view longer description
# 10 to >7 pts
# Good
# Students where able to understand the given exercise and the objective
# 7 to >3 pts
# Fair
# Student partially understood the given exercise and the objective
# 3 to >0 pts
# Poor
# Student could not understand the exercise and the objective
# / 10 pts
# Create
# view longer description
# 10 to >7 pts
# Good
# Student was able to identify the inputs, outputs and the constraints for the given exercise
# 7 to >3 pts
# Fair
# Student was partially able to identify the inputs, output and the constraints for the given exercise
# 3 to >0 pts
# Poor
# Student could not identify the inputs output and the constraints for the given exercise
# / 10 pts
# Code
# view longer description
# 10 to >7 pts
# Good
# Student was able to fully code the exercise with correct datatypes and indentations
# 7 to >3 pts
# Fair
# Student was able to partially code the exercise with minor errors in the datatypes and indentations
# 3 to >0 pts
# Poor
# Student was not able to code the exercise with correct datatypes and indentations
# / 10 pts
# Validation
# view longer description
# 10 to >7 pts
# Good
# The output validation of the exercise is fully correct
# 7 to >3 pts
# Fair
# The output validation of the exercise is partially correct with minor errors
# 3 to >0 pts
# Poor
# The output validation of the exercise is incorrect with major errors
# / 10 pts
# Total Points: 0
# Choose a submission type
# 
# 
# 
# 
# 
# 
# or
#  
# Drag a file here, or click to select a file to upload
# 
# Drag a file here, or
# Choose a file to upload
# No file chosen

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


# In[ ]:


Introductory Abstraction


# Complete the Exercises - Representing Abstraction Through Code 
# In programming, we deal with two kinds of elements: functions and data. 
# 
# Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 
# 
# By the concept of abstraction create functions representing abstracting principles through function 
# 
# Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
# Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
# Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
# Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
# Factor:  Calculate temperature that a person feels because of the wind (Python3)

# In[ ]:


def arithmetic(num1, num2, operator):
    """
    This function takes two numbers and an operator and returns the result of applying the operator to the numbers.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"


# In[9]:


def conversion(num, unit):
    """
    This function takes a number and a unit (either 'miles' or 'kilometers') and converts the number to the other unit.
    """
    if unit == "miles":
        return num * 1.60934
    elif unit == "kilometers":
        return num / 1.60934
    else:
        return "Invalid unit"


# In[ ]:


def earthquake_impact(magnitude):
    """
    This function takes the magnitude of an earthquake and returns a description of the impact.
    """
    if magnitude < 2.0:
        return "Generally not felt by people"
    elif magnitude < 3.0:
        return "Often felt, but rarely causes damage"
    elif magnitude < 4.0:
        return "Light shaking, noticeable indoors, but no damage"
    elif magnitude < 5.0:
        return "Moderate shaking, no damage to well-built structures"
    elif magnitude < 6.0:
        return "Strong shaking, damage to poorly constructed buildings"
    elif magnitude < 7.0:
        return "Major earthquake, widespread damage"
    elif magnitude < 8.0:
        return "Great earthquake, serious damage"
    else:
        return "Can totally destroy communities near the epicenter"


# In[ ]:


def factor(temp, wind_speed):
    """
    This function takes the temperature in Celsius and the wind speed in kilometers per hour and returns the wind chill factor.
    """
    if wind_speed < 5.0:
        return temp
    else:
        wind_chill = 13.12 + 0.6215 * temp - 11.37 * wind_speed ** 0.16 + 0.3965 * temp * wind_speed ** 0.16
        return wind_chill

