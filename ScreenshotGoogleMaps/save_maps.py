# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2018. 

# Inputs required are:
# 1. Latitude and Longitude of centre of area of interest
# 2. Paths to chromedriver and output folder
# 3. Distances and angles preset for image acquistion are 
#    (i)   600m distance for top-down
#    (ii)  565m distance for tilt at intervals of 5 degrees going from 5 to 40 degrees
#    (iii) 400m distance for tilt at 45 degrees for full revolution of 360 degrees in steps of 10 degrees
#    Above values can be optimized for downstream purpose of interest

import os
import time
from selenium import webdriver
import numpy as np

# Adjust this list to latitude and longitude of center of area of interest
APS_loc = [1.2913, 103.8236]
# Conversion factor is 11.132m for every 0.0001 degree for lat/long

# Directory path should be updated to appropriate values
chrome_path = "/home/ooicc/Dropbox/temp/chromedriver.exe"
output_path = "/home/ooicc/Dropbox/temp/"

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()

# Image acquisition for top-down image
# Always ensure it is facing true north for easier rotation subsequently

X_data_file = output_path + "test_top.png"
heading = 0
    
image_url = 'https://www.google.com/maps/@' + str(APS_loc[0]) + ',' + str(APS_loc[1]) + ',600m/data=!3m1!1e3'
driver.get(image_url)
time.sleep(30)
driver.save_screenshot(X_data_file)

# Image acquisition for images of varying tilt angle

image_dist = 565.0
for i in range(1,9):
    #time.sleep(5)
    cur_image_tilt = i*5
    if cur_image_tilt < 10:
        X_data_file = output_path + "test_0" + str(cur_image_tilt) + "_tilt.png"
    else:
        X_data_file = output_path + "test_" + str(cur_image_tilt) + "_tilt.png"
    
    lat = APS_loc[0] - image_dist * np.sin(np.pi/180.0*cur_image_tilt)/11.132*0.0001
    longitude = APS_loc[1]
    alt = image_dist*np.cos(np.pi/180.0*cur_image_tilt)
    
    image_url = 'https://www.google.com/maps/@' + str(lat) + ',' + str(longitude) + ',' + str(alt) + 'a,35y,360h,' + str(cur_image_tilt) + 't/data=!3m1!1e3'
    
    driver.get(image_url)
    time.sleep(30)
    driver.save_screenshot(X_data_file)

# Image acquisition for images in a full revolution around area of interest

dist_rev = 400.0
for i in range(36):
    cur_image = i
    if cur_image < 10:
        X_data_file = output_path + "test_0" + str(cur_image) + ".png"
    else:
        X_data_file = output_path + "test_" + str(cur_image) + ".png"
    
    lat = APS_loc[0] + dist_rev/11.132*np.cos(np.pi/180.0*i*10.0)*0.0001
    longitude = APS_loc[1] + dist_rev/11.132*np.sin(np.pi/180.0*i*10.0)*0.0001
    
    if cur_image < 18:
        heading = 180 + i*10
    else:
        heading = i*10 - 180
        
    image_url = 'https://www.google.com/maps/@' + str(lat) + ',' + str(longitude) + ',400a,35y,' + str(heading) + 'h,45t/data=!3m1!1e3'
    # If tilt angle is adjusted from 45 degrees or range is adjusted from 400m, the dist_rev needs to be updated.
	
    driver.get(image_url)
    time.sleep(30)
    driver.save_screenshot(X_data_file)


driver.close()



