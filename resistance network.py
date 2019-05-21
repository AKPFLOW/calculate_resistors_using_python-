# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:59:04 2019

@author: Akpofure
"""


#input statement
R1 = float(input("Enter the value of the first resistor: "))
R2 = float(input ("Enter the value of the second resistor: "))
R3 = float(input ("Enter the value of the third resistor: "))

#computation for the parallel network

Rp = (R2*R3)/(R2+R3)

#computation for the total resistance

Rt = R1 + Rp

print(Rt)
