#!/usr/bin/env python
# coding: utf-8

# # problem2
# 
# """ 
# Problem: Knock Knock are you there?
# Input Format:
# 1. Take N int input from the User 
# 2. Get N , seperated values from a user 
# 3. Enter a number 'M' you are looking for
# Output Format:
# 1. Print index on console once Found or Print 'You Have Missed It' to the console
# """

# In[ ]:



N = int(input("Enter the number of elements in the list: "))

nums = list(map(int, input("Enter the elements of the list separated by space: ").split()))

M = int(input("Enter the number you are looking for: "))

found = False

for i in range(N):
    if nums[i] == M:
        print("Index of the number:", i)
        found = True
        break
if not found:
    print("You Have Missed It")


# """ 
# # Problem 3
# Archit and Girish are playing Ludo. In one turn, both of them roll their dice at once.
# They consider a turn to be good if the sum of the numbers on their dice is less than 6
# Given that in a particular turn Archit and Girish got 
# A and B on their respective dice, find whether the turn was good.
# Input Format
# The first line of input will contain a single integer  T, denoting the number of test cases.
# Each test case contains space-separated integers 
# A and B — the numbers Archit and Girish got on their respective dice.
# Output Format
# For each test case, output on a new line, Perfect, if the turn was good and Bad Luck otherwise.
# Input.          
# 4
# 1 3
# 3 4
# 6 2
# 2 6
# Output 
# Bad Luck
# Perfect
# Perfect
# Perfect
# """

# In[ ]:


# Read the number of test cases
T = int(input())

# Loop over the test cases
for i in range(T):
    # Read the input values
    A, B = map(int, input().split())

    # Calculate the sum of A and B
    total = A + B

    # Check if the turn is good or bad luck
    if total < 6:
        print("Perfect")
    else:
        print("Bad Luck")


# In[ ]:


# Read the number of test cases
t = int(input())

# Loop through each test case
for i in range(t):
    # Read the values of A and B
    a, b = map(int, input().split())
    
    # Check if the sum is less than 6
    if a + b < 6:
        print("Perfect")
    else:
        print("Bad Luck")


# # problem4 
#  """
# Print the following pattern for given number of rows.
# Input format :
# Integer N (Total number of rows)
# Output Format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output:
# 5432*
# 543*1
# 54*21
# 5*321
# *4321
#    
# """

# In[ ]:


n = int(input())

for i in range(n):
    for j in range(n):
        if j == n-i-1:
            print("*", end="")
        else:
            print(n-j, end="")
    print()

