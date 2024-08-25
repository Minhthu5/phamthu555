# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:01:10 2024

@author: PhamNguyenThiMinhThu
"""
input_string = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
parts = [part.strip() for part in input_string.split(',')]
sub_strings = [
    parts[0],
    parts[1],
    parts[2].split('P. ')[1],
    parts[3].split('Q. ')[1],
    parts[4].split('Tp. ')[1] ]
for sub_string in sub_strings:
    print (sub_string)
