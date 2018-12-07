# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2018. 

# Inputs required are:
# (a) Hexadecimal codes for color of geometries of interest
# (b) Name of input svg file and output text file


#Using python3.4
import re

# Input and output file names to be used
input_file = 'map.svg'
output_file = 'all_list.txt'

# Color code of geometries to select for
f1 = '#D9D0C9'
f2 = '#AF9C8D'

# This extracts and combines the various lines that describe the geometry objects of interest
svg_file = open(input_file,mode='rU')

polygon_list = []
counter = 0
inside_polygon = False
for L1 in svg_file:
    L1stripped = L1.strip()

    #if 'polygon' in L1stripped:
    if (f1 in L1stripped) or (f2 in L1stripped):
        inside_polygon = True
        cur_line = ''

    if inside_polygon is True:
        cur_line = cur_line + ' ' + L1stripped
        if '"/>' in L1stripped:
            inside_polygon = False
            polygon_list.append(cur_line)

svg_file.close()

# Write lines for re-combining into svg files
f = open(output_file,'w')

for L1 in polygon_list:
    f.write('\t'+L1+'\n')

f.close()
