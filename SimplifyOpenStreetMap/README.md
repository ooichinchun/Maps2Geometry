## Automatic Simplification of Buildings from [Open Street Map](https://www.openstreetmap.org)

#### Exporting Data from Open Street Map

It is possible to extract data for a specified minimum and maximum latitude and longitude.  
It is worth remembering that the conversion factor is approximately 11.1m for 0.0001 degree when specifying the range required.

| ![Sample OSM Interface](https://github.com/ooichinchun/Maps2Geometry/blob/master/SimplifyOpenStreetMap/OSM_Example.tif "Exporting OSM Data") | 
|:--:| 
| **Sample OSM interface for exporting OSM data** |

Specifying the LATITUDE and LONGITUDE in the highlighted yellow boxes on the left, and the appropriate scale and file format on the right allows for easy parsing of OSM data.
We chose to save the data in the pdf format for easy conversion in Illustrator to svg format. 

### Automatic Acquisition of Images via Python

The script to be run is saved [here](https://github.com/ooichinchun/Maps2Geometry/blob/master/ScreenshotGoogleMaps/save_maps.py) and can be understood in terms of the following sections.

#### 01. Install Selenium and Chromedriver

Image acquistion is accomplished via the use of the Selenium package in conjunction with the [chromedriver](http://chromedriver.chromium.org/downloads) for the chrome browser. Hence, packages must be installed, and the directory where the chromedriver is installed should be noted.  
The chromedriver needs to be renamed with a .exe extension and permissions adjusted (chmod +x).

#### 02. Open browser window and save screenshot for area of interest

Images are saved in a pre-specified directory.

#### 03. Acquire images for a top-down view

| ![Top-Down Image](https://github.com/ooichinchun/Maps2Geometry/blob/master/ScreenshotGoogleMaps/test_top.png "Top-Down Image") | 
|:--:| 
| **Sample top-down image that was automatically acquired** |

#### 04. Acquire images for a sequence of different tilt angles

As written currently, images are acquired in steps of 5<sup>o</sup> between 0 and 45 degrees.

| ![Image at Tilt of 20 degrees](https://github.com/ooichinchun/Maps2Geometry/blob/master/ScreenshotGoogleMaps/test_20_tilt.png "20 Degree Image") | 
|:--:| 
| **Sample image with a tilt** |

#### 05. Acquire images for a sequence of different headings (360<sup>o</sup> view)

As written currently, images are acquired in steps of 10<sup>o</sup> between 0 and 360 degrees at a tilt of 45<sup>o</sup>. 

| ![Rotating view of area of interest](https://github.com/ooichinchun/Maps2Geometry/blob/master/ScreenshotGoogleMaps/rotate.gif "360 Degree Image") | 
|:--:| 
| **Sample image with 360 degree rotation** |
