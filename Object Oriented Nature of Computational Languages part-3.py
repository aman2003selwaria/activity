#!/usr/bin/env python
# coding: utf-8

# OODP-02 Create Return on Investment class for UX and Usability Firm (Case Based Approach)
# 
# Mock Client: Human Factors Internationals (HFI)
# 
# Client Specifications are shared in this Link: http://hfiacademy.com/roi_increased_conversion_rate.phpLinks to an external site.
# 
# 1. You are working as an oops designer and programmer  in one of the reputed firm in the World.
# 
# 2. You are been asked to create a ROI Increased conversion rate calculator using OOPS principles by your Manager. Having said that you are experienced individual who knows the principles of oops and python.
# 
# 3. Design the requirements and implement the OOP for the ROI Increased conversion rate calculator
# 
# OODP-03 Representation of Concept of Inheritance
# 
# Open Problem: Take an cue from Healthcare, Agriculture, Education , FinTech Domains
# 
# Choose an area and apply the concept of Inheritance.
# 
# Test and Debug Your Code is Weighed 15% Overall
# 
# GitHub Classroom Link: https://classroom.github.com/a/nexaHT6cLinks to an external site.

# In[1]:


class ROI:
    def __init__(self, cost, visitors_before, visitors_after, order_value, conv_before, conv_after):
        self.cost = cost
        self.visitors_before = visitors_before
        self.visitors_after = visitors_after
        self.order_value = order_value
        self.conv_before = conv_before
        self.conv_after = conv_after
        
    def calculate_roi(self):
        revenue_before = self.visitors_before * self.conv_before * self.order_value
        revenue_after = self.visitors_after * self.conv_after * self.order_value
        profit = revenue_after - revenue_before - self.cost
        roi = (profit / self.cost) * 100
        return roi
        
    def display_results(self):
        print("Cost of HFI services: $", self.cost)
        print("Average monthly website visitors before HFI services: ", self.visitors_before)
        print("Average monthly website visitors after HFI services: ", self.visitors_after)
        print("Average order value of the website: $", self.order_value)
        print("conv rate before HFI services: ", self.conv_before)
        print("conv rate after HFI services: ", self.conv_after)
        print("ROI: ", self.calculate_roi(), "%")

# Get input from the user
cost = float(input("Enter the cost of HFI services: "))
visitors_before = int(input("Enter the average monthly website visitors before HFI services: "))
visitors_after = int(input("Enter the average monthly website visitors after HFI services: "))
order_value = float(input("Enter the average order value of the website: "))
conv_before = float(input("Enter the conv rate before HFI services: "))
conv_after = float(input("Enter the conv rate after HFI services: "))

# Create an instance of the ROI class with user inputs
hfi_roi = ROI(cost, visitors_before, visitors_after, order_value, conv_before, conv_after)

# Display the results
hfi_roi.display_results()

