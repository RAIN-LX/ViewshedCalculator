# Viewshed Calculator
Python script for generating viewsheds across coastal transects

The goal is to be able to draw a line in ArcGIS Pro, and feed the line shape to the script so
that it generates a viewshed for continous points along the line. 

Potentially, the user will have the option to combine the linear viewshed series into a single
shapefile, or to leave it as a series of individual viewsheds so that several points can be 
chosen for single-point ground truthing.

# Current Process:

1. DEM data for Pensacola Beach region acquired as .tif file from https://apps.nationalmap.gov/lidar-explorer/#/ (USGS)
2. Viewshed project initialized in ArcGIS Pro
3. Add .tif file, create point shapefile, add an initial testing point. 
4. Familiarize with spatial analyst viewshed tool
5. Project .tif to coordinate system with Z coord system
6. What should the observer height be given that we will be using low-oblique aerial imagery? assume 6 meters for testing.
7. 




