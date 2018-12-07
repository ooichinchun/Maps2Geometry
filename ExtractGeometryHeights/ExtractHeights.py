# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2018. 

# Inputs required are:
# 1. Input filename containing photogrammetry mesh points
# 2. Input filename containing 2D geometry footprints as an obj file
# 3. Output filename to write vertices and heights
# 4. For faster processing, we request the mesh x and y minimum and maximum ranges to filter out 2D geometries that are not within the range.
#    It is anticipated that the photogrammetry mesh will typically be smaller than the 2D geometry dimension
# 5. The default setting is that the 95th percentile height value for the mesh points within each 2D geometry will be used. This can be optimized further if desired.


import numpy as np
import matplotlib.path as mpltPath

vertices_filename = 'vertices.csv'
obj_filename = 'reduced_convex_hull_w_paths.obj'
output_filename = 'reduced_convex_hull_w_path_vertex_w_height.csv'

# This delineates the limits of the photogrammetry mesh values to facilitate filtering of the mesh points
mesh_xlim = [-500.0,300.0]
mesh_ylim = [-360.0,360.0]

# This sets the relevant percentile to use for extracting the heights.
percentile_to_use = 95

# This just extracts the mesh points from the photogrammetry mesh into a single list with x,y,z coordinates
vertices_file = open(vertices_filename,mode='rU')
vertex_seqList = []

for L1 in vertices_file:
    L1stripped = L1.strip()
    vertices = L1stripped.split(',')
    P1 = tuple([float(vertices[0]),float(vertices[1]),float(vertices[2])])
    
    vertex_seqList.append(P1)
    
vertices_file.close()

# This part uses the 2D geometry vertices as a mask to identify the mesh points within them
# The 95th percentile height of the filtered meshpoints for each mask are then identified and saved.
obj_file = open(obj_filename,mode='rU')
f = open(output_filename,'w')

new_object = False
vertex = []

for L1 in obj_file:
    L1stripped = L1.strip()
    y_split = L1stripped.split(' ')
    
    if new_object:
        if y_split[0] == 'v':
            f.write(L1stripped + '\n')
            vertex.append([float(y_split[1]),float(y_split[2])])
        else:
            counter += 1
            if counter == 1:
                new_object = False
                
                vertex_array = np.array(vertex)
                x_min,y_min = np.min(vertex_array,axis=0)
                x_max,y_max = np.max(vertex_array,axis=0)
                heights = []
                if (x_max < mesh_xlim[1]) and (x_min > mesh_xlim[0]):
                    if (y_max < mesh_ylim[1]) and (y_min > mesh_ylim[0]):
                    
                        path = mpltPath.Path(vertex)
                
                        for p in vertex_seqList:
                            P1 = p[0:2]
                    
                            if path.contains_point(P1):
                                heights.append(p[2])
                        
                if len(heights) > 0:
                    output_height = np.percentile(np.array(heights),percentile_to_use)
                    
                    f.write('Height ' + str(output_height) + '\n')
                        
                else:
                    # Default height to use can be adjusted here if so desired
                    f.write('Height 0\n')
                    
    if 'object' in L1stripped:
        new_object = True
        f.write(L1stripped + '\n')
        vertex = []
        counter = 0
        
obj_file.close()
f.close()
