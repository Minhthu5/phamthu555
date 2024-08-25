# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:00:32 2024

@author: PhamNguyenThiMinhThu
"""

input_string = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = [s.strip() for s in input_string.split(',')]
for sub_string in sub_strings:
    print (sub_string)
    