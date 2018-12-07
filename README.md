# Maps2Geometry
Scripts for converting OpenStreetMap / Google Maps data to 3D Geometry Information

This repo contains all the code required to convert open source data from Open Street Maps into CAD geometries for further downstream processing such as Computational Fluid Dynamics (CFD) simulations.

Only codes and documentation are provided due to the size of the geometry files but sample data files can be requested from us if desired.

### Workflow
There are 3 parts to this workflow:

1. Data Download from [OpenStreetMap](https://www.openstreetmap.org)  
   (a) Download image from OpenStreetMap for area of interest.   
   (b) Identify the color settings for the objects within the area of interest.  
   (c) Extract vertices of objects of interest.  
   (d) Extract the convex hull geometry to simplify object geometry.  

2. Data Download from [Google Maps](https://maps.google.com)  
   (a) Acquire set of images from Google Maps comprising a flat top-down view, a series of images with gradually decreasing tilt angles, and another series of images providing a 360<sup>o</sup> perspective of area of interest.  
   (b) Run photogrammetry algorithms to re-generate a mesh from the point clouds generated from the images.  
   (c) Mesh should be re-scaled and re-leveled to remove any existing tilts.  

3. Extracting Geometry Heights for 3D Geometry Generation  
   (a) Realign the two sets of meshes by applying the appropriate transformation to the meshes.  
   (b) Save the mesh file as a set of mesh elements and extract the individual point locations.  
   (c) Loop through all the 2D geometries and find their corresponding heights as per the point cloud.  
   (d) Re-create the geometries and create the 3D extrusion for export as 3D CAD geometry.  

Additional details for Parts 1-3 are in the corresponding subdirectories:
1. <b>SimplifyOpenStreetMap</b>
2. <b>ScreenshotGoogleMaps</b>
3. <b>ExtractGeometryHeights</b>

Three commercial programs are used in this workflow.  
 - [Adobe Illustrator](https://www.adobe.com/sea/products/illustrator.html) is used to convert files between .pdf, .svg and .dwg formats, and to obtain the color codes for the geometry objects of interest.  
 - [Agisoft PhotoScan](https://www.agisoft.com) is used to convert the google map images into a 3D mesh file.  
 - [Rhinoceros](https://www.rhino3d.com) is used for aligning the meshes, and is used for the 3D geometry regeneration.  
 
Open-source photogrammetry software exists, and open-source CAD programs that can handle the conversion between CAD file formats can be used, but some re-formatting of data is anticipated.

Note: This is not an official IHPC product, but please credit this work if this is helpful to you.

This work is a joint effort by Raymond Quek and [Ooi Chin Chun](ooicc@ihpc.a-star.edu.sg) from the Institute of High Performance Computing, A* Singapore.
