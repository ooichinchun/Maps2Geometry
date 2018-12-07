## Extraction of Geometry Heights and Creation of 3D CAD Model

### Align Photogrammetry Mesh and 2-D Footprint Geometry

The two geometries need to be checked for scale, orientation and relative translation before further combination. This is best done in a CAD program, so they can be visually checked for alignment. 

### Extract Object Heights and Extrude 2-D Footprint to Object Height

The workflow can be understood in terms of the following sections.

#### 01. Extract photogrammetry mesh points in csv format

After importing the mesh from Agisoft PhotoScan into Rhino, we save the mesh as a .raw file with the x,y,z coordinates of the various mesh elements' vertices. 

We then run the [script](https://github.com/ooichinchun/Maps2Geometry/blob/master/ExtractGeometryHeights/extract_vertices.py) on the .raw file to extract individual mesh points' x,y,z coordinates as a .csv file. 

#### 02. Find the height of the 2-D building geometries via Python

We save the 2-D building geometry as an .obj file from Rhino, and filter the vertices saved from Step 01 for the various 2D footprints. From there, our script extracts the 95th percentile of the height of the mesh points within each building footprint, and saves that into another text file that retains the individual vertices, along with the associated height. Objects which are not in the photogrammetry mesh are saved with a default height of 0m. 

This default height can be easily adjusted within the script if so desired.

The script to be used here is [ExtractHeights.py](https://github.com/ooichinchun/Maps2Geometry/blob/master/ExtractGeometryHeights/ExtractHeights.py)

#### 03. Read vertices and heights into Rhino and create 3D geometries

The specified vertices and heights contained in the output file from Step 2 can be processed with this [script](https://github.com/ooichinchun/Maps2Geometry/blob/master/ExtractGeometryHeights/read_heights_extrude_geometries.py) in Rhino to automatically create the points, lines, planar surfaces, and 3-D geometries.  

| ![Sample 3D geometry](https://github.com/ooichinchun/Maps2Geometry/blob/master/ExtractGeometryHeights/ExtrudedGeometry.JPG "Sample 3D geometry") | 
|:--:| 
| **Sample 3D geometry in Rhino** |

In the sample above, the red points represent the vertices in the file, whle the extruded volumes correspond to the heights as identified by photogrammetry. The outer regions only contain planar surfaces as the photogrammetry mesh did not cover that area.

The resulting 3D geometry can then be saved as any CAD geometry file of choice. 


