#!/usr/bin/env python
# coding: utf-8

# Problem 1:
# 
# Suppose you are buying something online on amazon.com 
# 
# On the website, you get
# a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.
# 
# Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.

# In[2]:


def calculate_discount(asset_amount, is_prime_member):
    if is_prime_member:
        discount = 0.15
    else:
        discount = 0
        
    black_friday_discount = 0.08
    
    total_discount = discount + black_friday_discount
    
    final_price = asset_amount * (1 - total_discount)
    
    return final_price


# Chit Chat Application - Function:
# 
# (a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.
# 
# Write a function that takes as input the,
# 
# message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.
# 
# 
# If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.
#     
# 
# (b) How one can check if the restriction is on a number of words rather than letters?
# Write a function that allows a message with only 30 words.

# In[4]:


def check_message_length(message):
    if len(message) <= 200:
        return message
    else:
        return message[:200]
    
    
    
    def check_message_word_count(message):
    words = message.split()
    if len(words) <= 30:
        return message
    else:
        return "Message contains more than 30 words."

