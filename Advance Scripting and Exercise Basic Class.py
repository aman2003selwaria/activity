#!/usr/bin/env python
# coding: utf-8

# 
# Case: We have an admission counsellor who wants to deliver a bulk message.
# 
# To the corresponding students with similar context, the admission counsellor asked a team of developers in EN2004 to help them creating a mechanism to deliver the same with an application that has a form like structure wherein
# The counsellor can update the asked fields and messages will be processed.
# 
# 
# names = # get and process input for a list of names
# Admission_ID = # get and process input for a list of the number of admission ID
#  CAP_Rank = # get and process input rank of the student in CAP # Information to be sent to be used for each student
# # HINT: use .format() with this string in your for loop
# 
# message = "Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship. \n\n" # write a for loop that iterates through each set of names, Admission_ID, and CAP ranks to print each student's message.

# In[ ]:


# get and process input for a list of names
names = input("Enter a comma-separated list of student names: ").split(",")
# get and process input for a list of the number of admission ID
Admission_ID = input("Enter a comma-separated list of admission ID numbers: ").split(",")
# get and process input rank of the student in CAP
CAP_Rank = input("Enter a comma-separated list of CAP ranks: ").split(",")

# iterate through each set of names, Admission_ID, and CAP ranks to print each student's message
for i in range(len(names)):
    # use .format() to insert the values into the message template
    message = "Hi {},\n\nCongratulations...! {} You got selected for the next round of the recruitment process. Submit your academic credentials including primary and secondary certificates. Your admission ID is {} and you will be eligible for the next round of interview with a CAP rank of {}. If you submit all the documents on time, the university might offer you a scholarship. \n\n".format(names[i], Admission_ID[i], CAP_Rank[i])
    # print the message
    print(message)


# Write a Python class,
# 
# MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.
# 
# Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type
# 
# If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class

# In[ ]:


class MedPlus:
    def __init__(self, name: str, batch_number: int, price: float) -> None:
        
        if not isinstance(name, str):
            raise TypeError("The name should be a string.")
        if not isinstance(batch_number, int):
            raise TypeError("The batch number should be an integer.")
        if not isinstance(price, float):
            raise TypeError("The price should be a float.")

        self._name = name
        self._batch_number = batch_number
        self._price = price

    def set_name(self, name: str) -> None:
       
        if not isinstance(name, str):
            raise TypeError("The name should be a string.")
        self._name = name

    def set_batch_number(self, batch_number: int) -> None:

        if not isinstance(batch_number, int):
            raise TypeError("The batch number should be an integer.")
        self._batch_number = batch_number

    def set_price(self, price: float) -> None:
     
        if not isinstance(price, float):
            raise TypeError("The price should be a float.")
        self._price = price

    def get_name(self) -> str:

        return self._name

    def get_batch_number(self) -> int:
     
        return self._batch_number

    def get_price(self) -> float:
  
        return self._price

