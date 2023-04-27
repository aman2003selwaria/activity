#!/usr/bin/env python
# coding: utf-8

# OODP-01 Create your own I_SET class;
# 
# Design and Implement your own integer set class with class name New_Set
# 
# The above class must have following methods-
# 
# inserting element in a set 
# check a membership of the element e - if it is present in a set then return is_member else return not_a_member 
# Remove the element e from a given set if e is in self removes it from self otherwise raise a ValueError if member not in self (NewSet)
# Get all the members of the list 
# Get members of self in descending order 
# Note: Add appropriate docstring as and when required

# In[ ]:


class New_Set:
    """
    A class representing an integer set.
    """
    
    def __init__(self):
        """
        Initialize an empty set.
        """
        self.members = []
        
    def insert(self, e):
        """
        Insert an element e into the set if it is not already present.
        """
        if e not in self.members:
            self.members.append(e)
            
    def is_member(self, e):
        """
        Check if the element e is a member of the set.
        If e is a member of the set, return True.
        Otherwise, return False.
        """
        return e in self.members
    
    def remove(self, e):
        """
        Remove the element e from the set if it is present.
        If e is not a member of the set, raise a ValueError.
        """
        if e in self.members:
            self.members.remove(e)
        else:
            raise ValueError("Element not in set.")
            
    def get_members(self):
        """
        Return a list of all the members of the set.
        """
        return self.members
    
    def get_members_descending(self):
        """
        Return a list of all the members of the set in descending order.
        """
        return sorted(self.members, reverse=True)
s = New_Set()

s.insert(1)
s.insert(2)
s.insert(3)

print(s.is_member(2))  # True
print(s.is_member(4))  # False

s.remove(2)

print(s.get_members())  # [1, 3]
print(s.get_members_descending())  # [3, 1]

