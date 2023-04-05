#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Nature of Computational Languages
# 
# 
# 

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
    This class represents a set of integers. It provides methods to insert elements,
    check membership of an element, remove an element, and get all the members of the set.
    """
    def __init__(self):
        """
        Constructor for the New_Set class. Initializes an empty set.
        """
        self.members = []
        
    def insert(self, e):
        """
        Inserts an element e into the set if it is not already present.
        """
        if e not in self.members:
            self.members.append(e)
            
    def is_member(self, e):
        """
        Checks if the element e is present in the set.
        If present, returns True, else returns False.
        """
        if e in self.members:
            return True
        else:
            return False
        
    def remove(self, e):
        """
        Removes the element e from the set if it is present.
        If not present, raises a ValueError.
        """
        if e in self.members:
            self.members.remove(e)
        else:
            raise ValueError("Element not present in the set")
        
    def get_members(self):
        """
        Returns a list of all the members of the set.
        """
        return self.members
    
    def get_members_descending(self):
        """
        Returns a list of all the members of the set in descending order.
        """
        return sorted(self.members, reverse=True)
# You can create an instance of this class and test its methods:

s = New_Set()

s.insert(5)
s.insert(10)
s.insert(7)


print(s.is_member(7))  # True
print(s.is_member(20))  


print(s.get_members())  # [5, 10, 7]


print(s.get_members_descending())  # [10, 7, 5]

s.remove(5)
print(s.get_members())  # [10, 7]


# In[ ]:




