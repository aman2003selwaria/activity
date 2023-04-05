#!/usr/bin/env python
# coding: utf-8

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

# In[3]:


class New_Set:
   
    def __init__(self):
        self._members = []

    def insert(self, e: int) -> None:
       
        if e not in self._members:
            self._members.append(e)

    def is_member(self, e: int) -> bool:
      
        return e in self._members

    def remove(self, e: int) -> None:
        
        if e in self._members:
            self._members.remove(e)
        else:
            raise ValueError(f"{e} is not a member of the set")

    def get_members(self) -> list[int]:
      
        return self._members

    def get_members_descending(self) -> list[int]:
       
        return sorted(self._members, reverse=True)


# In[4]:


s = New_Set()
s.insert(3)
s.insert(1)
s.insert(4)
print(s.get_members())  # Output: [3, 1, 4]
print(s.is_member(3))   # Output: True
print(s.is_member(2))   # Output: False
s.remove(3)
print(s.get_members())  # Output: [1, 4]
print(s.get_members_descending())  # Output: [4, 1]


# 
# 
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

# In[ ]:


class ROI_Calculator:
    """
    A class representing a ROI Increased conversion rate calculator.
    """
    
    def __init__(self, current_conv_rate: float, new_conv_rate: float, monthly_visitors: int, cost_of_redesign: float):
        """
        Initialize the attributes of the calculator.
        """
        self.current_conv_rate = current_conv_rate
        self.new_conv_rate = new_conv_rate
        self.monthly_visitors = monthly_visitors
        self.cost_of_redesign = cost_of_redesign
        
    def calculate_roi(self) -> float:
        """
        Calculate the ROI of the redesign project.
        """
        current_revenue = self.monthly_visitors * self.current_conv_rate
        new_revenue = self.monthly_visitors * self.new_conv_rate
        net_revenue_increase = new_revenue - current_revenue
        roi = net_revenue_increase / self.cost_of_redesign * 100
        return roi
    
    def display_roi(self) -> None:
        """
        Display the calculated ROI.
        """
        roi = self.calculate_roi()
        print(f"The ROI for the redesign project is {roi:.2f}%.")


# In[ ]:


# Create an instance of the calculator with sample inputs
calc = ROI_Calculator(current_conv_rate=0.02, new_conv_rate=0.04, monthly_visitors=10000, cost_of_redesign=50000)

# Display the calculated ROI
calc.display_roi()  # Output: The ROI for the redesign project is 40.00%.


# 
# 
# OODP-03 Representation of Concept of Inheritance
# 
# Open Problem: Take an cue from Healthcare, Agriculture, Education , FinTech Domains
# 
# Choose an area and apply the concept of Inheritance.

# In[ ]:


class MedicalTest:
    def __init__(self, patient_id, test_date):
        self.patient_id = patient_id
        self.test_date = test_date
        self.test_result = None

    def perform_test(self):
        pass

    def get_test_result(self):
        return self.test_result


# In[ ]:


class BloodTest(MedicalTest):
    def __init__(self, patient_id, test_date, glucose_level, cholesterol_level):
        super().__init__(patient_id, test_date)
        self.glucose_level = glucose_level
        self.cholesterol_level = cholesterol_level

    def perform_test(self):
        # perform the blood test and set the test result
        self.test_result = "Normal"


class ImagingTest(MedicalTest):
    def __init__(self, patient_id, test_date, type_of_imaging, imaging_results):
        super().__init__(patient_id, test_date)
        self.type_of_imaging = type_of_imaging
        self.imaging_results = imaging_results

    def perform_test(self):
        # perform the imaging test and set the test result
        self.test_result = "Positive"


class GeneticTest(MedicalTest):
    def __init__(self, patient_id, test_date, genetic_mutations):
        super().__init__(patient_id, test_date)
        self.genetic_mutations = genetic_mutations

    def perform_test(self):
        # perform the genetic test and set the test result
        self.test_result = "Negative"

