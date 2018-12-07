# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2018. 

# Inputs required are:
# (a) Name of input text file and output text file

import re
from scipy.spatial import ConvexHull
import numpy as np

# Edit names of input and output files to match
input_file = open('all_list.txt',mode='rU')
f = open('all_list_convex_hull_path.txt','w')

bld_num_pts_seqList = []

for L1 in input_file:
    L1stripped = L1.strip()

	# This checks for the first sort of object specification style : Polygons
    if 'polygon' in L1stripped:
        y = re.findall('points=".*"',L1stripped)
        y_split = y[0].split('"')

        yyy = y_split[1].split(' ')
        num_vertex = len(yyy)
        bld_num_pts_seqList.append(num_vertex)
               
		# This creates a list of all vertices specified in the svg file
        cur_list = []
               
        for yyyy in range(num_vertex-1):
            new_pt = yyy[yyyy]
            x,y = new_pt.split(',')

            cur_list.append([float(x),float(y)])
        
        points = np.array(cur_list)
        hull = ConvexHull(points)
    
		# This re-writes the list of convex hull vertices for regeneration of geometry
        str_to_save = L1stripped[0:(L1stripped.index('points="')+8)]
        
        for j in range(len(hull.vertices)):
            str_to_save = str_to_save + str(points[hull.vertices[j],0]) + ',' + str(points[hull.vertices[j],1]) + " " 
        str_to_save = str_to_save + '"/>\n'
        
        f.write(str_to_save)
    
	# This deals with the second class of possible svg objects. Rect does not need further configuration as a convex hull operation will return the same shape
    elif 'rect' in L1stripped:
        f.write(L1stripped+'\n')

	# This deals with the third class of objects, 'path'. 
    elif 'path' in L1stripped:
        
        y = re.findall('d=".*"',L1stripped)
        y_split = y[0].split('"')

        yyy = re.split('[A-Za-z]',y_split[1])
		
        vertex_index_in_str = []
        for match in re.finditer('[A-Za-z]',y_split[1]):
            vertex_index_in_str.append(match.start())
        
        num_vertex = len(yyy)
        bld_num_pts_seqList.append(num_vertex)
                
		# This creates the vertex list according to possible SVG specifications for the move pattern
        cur_list = []
               
        for yyyy in range(num_vertex-1):
            if y_split[1][vertex_index_in_str[yyyy]] != 'z':
                
                
                new_pt = yyy[yyyy+1]
                
                
                if y_split[1][vertex_index_in_str[yyyy]] == 'M':
                    x,y = new_pt.split(',')
                    cur_point = [float(x),float(y)]
                elif y_split[1][vertex_index_in_str[yyyy]] == 'L':
                    x,y = new_pt.split(',')
                    cur_point = [float(x),float(y)]
                elif y_split[1][vertex_index_in_str[yyyy]] == 'l':
                    if ',' in new_pt:
                        dx,dy = new_pt.split(',')
                        x = cur_point[0] + float(dx)
                        y = cur_point[1] + float(dy)
                    elif new_pt[0] == '-':
                        dxdy = new_pt.split('-')
                        x = cur_point[0] - float(dxdy[1])
                        y = cur_point[1] - float(dxdy[2])
                    else:
                        dxdy = new_pt.split('-')
                        x = cur_point[0] + float(dxdy[0])
                        y = cur_point[1] - float(dxdy[1])
                        
                    cur_point = [x,y]
                    
                elif y_split[1][vertex_index_in_str[yyyy]] == 'h':
                    x = cur_point[0] + float(new_pt)
                    cur_point[0] = x
                elif y_split[1][vertex_index_in_str[yyyy]] == 'v':
                    y = cur_point[1] + float(new_pt)
                    cur_point[1] = y

                    
                cur_list.append(cur_point)
        
        points = np.array(cur_list)
        hull = ConvexHull(points)
        
		# This resaves the convex hull form of the geometry
        str_to_save = '<polygon fill-rule="evenodd" clip-rule="evenodd" fill="#D9D0C9" points="'
        
        for j in range(len(hull.vertices)):
            str_to_save = str_to_save + str(points[hull.vertices[j],0]) + ',' + str(points[hull.vertices[j],1]) + " " 
        str_to_save = str_to_save + '"/>\n'
        
        f.write(str_to_save)
    
        
input_file.close()
f.close()

