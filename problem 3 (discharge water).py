#!/usr/bin/env python
# coding: utf-8

# """
# Task-3: Design and implement recursive solution for the below mentioned scenarios.
# There are n industries, each with a water treatment plant, located along a side of a river.
# We will assume that the industries are arranged from left to right. Each industry generates sewage water that must be cleaned in a plant (not necessarily its own) and discharged into the river through pipes, where additional pipes connect neighboring industries. 
# If a plant is working it will clean the sewage water from its industry, plus any water coming from a pipe connecting a neighboring industry, and discharge it to the river. However, a plant might not be working.
# In that case the water from its industry, plus any water coming from a neighboring industry. 
# must be sent to another industry. Given that water can flow in only one direction inside a pipe, the problem consists of determining the number of different ways it is possible to discharge the cleaned water into the river, for n industries. 
# Finally, we can assume that at least one of the plants will work.

# In[ ]:


def discharge_water(n):
    if n == 1:
        return 1
    else:
        result = 0
        # plant is working
        result += 2 * discharge_water(n-1)
        # plant is not working
        for i in range(2, n+1):
            result += discharge_water(i-2) * discharge_water(n-i+1)
        return result

