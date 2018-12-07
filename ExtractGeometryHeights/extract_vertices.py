# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2018. 

# Inputs required are:
# 1. Input and Output file names

input_filename = 'test.raw'
output_filename = 'vertices.csv'

vertex = set()

f = open(input_filename,mode='rU')

for L1 in f:
    
    L1stripped = L1.strip()
    vertices = L1stripped.split(' ')
    if len(vertices) == 9:
        P1 = tuple(vertices[0:3])
        P2 = tuple(vertices[3:6])
        P3 = tuple(vertices[6:9])
        if P1 not in vertex:
            vertex.add(P1)
        if P2 not in vertex:
            vertex.add(P2)
        if P3 not in vertex:
            vertex.add(P3)

f.close()


f = open(output_filename,mode='w')

for L1 in vertex:
    f.write(L1[0] + ','+ L1[1] + ',' + L1[2] + '\n')

f.close()
