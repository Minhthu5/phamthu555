# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:57:08 2024

@author: PhamNguyenThiMinhThu
"""
import math
a=float(input("nhap a: "))
b=float(input("nhap b: "))
A=((math.sqrt(a)-math.sqrt(b)) / (math.pow(a, 0.25)-math.pow(b, 0.25))) - ((math.sqrt(a)+math.pow(a*b, 0.25)) / (math.pow(a, 0.25)+math.pow(b, 0.25)))
print("ket qua la:", round(A))
