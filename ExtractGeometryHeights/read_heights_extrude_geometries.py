# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2018. 

# Inputs required are:
# 1. Filename of input file containing vertices and heights
# 2. Choice of function to round the heights extracted


import rhinoscriptsyntax as rs

vertices_file = open('reduced_convex_hull_w_path_vertex_w_height.csv',mode='rU')

new_object = False
vertex = []
for L1 in vertices_file:
    L1stripped = L1.strip()
    y_split = L1stripped.split(' ')
    
    if new_object:
        if y_split[0] == 'v':
            vertex.append([float(y_split[1]),float(y_split[2]),0])
        else:
            counter += 1
            if counter == 1:
                new_object = False
                
                vertex.append(vertex[0])
                pts_ids = rs.AddPoints(vertex)
                rs.ObjectColor(pts_ids, [255,0,0])
                
                curve_ids = rs.AddPolyline(vertex)
                surf_ids = rs.AddPlanarSrf(curve_ids)
                
				# This height value can be further edited to reduce complexity
				# A simple way to edit this would be to floor the value to reduce the step sizes possible.
                height = float(y_split[1])
                
                if height > 0:
                    extrusion_pt = [vertex[0][0],vertex[0][1],height]
                    extrusion_curve = rs.AddLine(vertex[0],extrusion_pt)
                    vol_ids = rs.ExtrudeSurface(surf_ids,extrusion_curve)

    if 'object' in L1stripped:
        new_object = True
        vertex = []
        counter = 0
    

vertices_file.close()

