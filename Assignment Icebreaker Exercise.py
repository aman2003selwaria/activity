#!/usr/bin/env python
# coding: utf-8

# Problem -I 
# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below:
# 
# Violet 380 to less than 450
# Blue 450 to less than 495
# Green 495 to less than 570
# Yellow 570 to less than 590
# Orange 590 to less than 620
# Red 620 to 750
# 
# Write a program that reads a wavelength from the user and reports its color. Display
# an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum

# In[2]:


wavelength = int(input("Enter the wavelength in nanometers: "))

if wavelength >= 380 and wavelength < 450:
    print("The color of the given wavelength is violet.")
elif wavelength >= 450 and wavelength < 495:
    print("The color of the given wavelength is blue.")
elif wavelength >= 495 and wavelength < 570:
    print("The color of the given wavelength is green.")
elif wavelength >= 570 and wavelength < 590:
    print("The color of the given wavelength is yellow.")
elif wavelength >= 590 and wavelength < 620:
    print("The color of the given wavelength is orange.")
elif wavelength >= 620 and wavelength <= 750:
    print("The color of the given wavelength is red.")
else:
    print("The given wavelength is outside of the visible spectrum.")


# 
# Problem -II
# 
# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below:
# 
# Radio Waves Less than 3 × 10^9
# Microwaves 3 × 10^9 to less than 3 × 10^12
# Infrared Light 3 × 10^12 to less than 4.3 × 10^14
# Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
# Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
# X-Rays 3 × 10^17 to less than 3 × 10^19
# Gamma Rays 3 × 10^19 or more
# 
# Write a program that reads the frequency of some radiation from the user and
# displays name of the radiation as part of an appropriate message.

# In[3]:


frequency = int(input("Enter the frequency of the radiation: "))

if frequency < 3*10**9:
    print("This radiation is a radio wave.")
elif 3*10**9 <= frequency < 3*10**12:
    print("This radiation is a microwave.")
elif 3*10**12 <= frequency < 4.3*10**14:
    print("This radiation is an infrared light.")
elif 4.3*10**14 <= frequency < 7.5*10**14:
    print("This radiation is a visible light.")
elif 7.5*10**14 <= frequency < 3*10**17:
    print("This radiation is an ultraviolet light.")
elif 3*10**17 <= frequency < 3*10**19:
    print("This radiation is an X-ray.")
else:
    print("This radiation is a gamma ray.")

