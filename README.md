# Viewshed Calculator
Python script for generating viewsheds across coastal transects

The goal is to be able to draw a line in ArcGIS Pro, and feed the line shape to the script so
that it generates a viewshed for continous points along the line. 

# ArcGIS Resource Pages:
1. Generate points along line https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/generate-points-along-lines.htm
2. 

# Current Process:

1. DEM data for Pensacola Beach region acquired as .tif file from https://apps.nationalmap.gov/lidar-explorer/#/ (USGS)
2. Viewshed project initialized in ArcGIS Pro
3. Add .tif file, create point shapefile, add an initial testing point. 
4. Familiarize with spatial analyst viewshed tool
5. Project .tif to coordinate system with Z coord system
6. What should the observer height be given that we will be using low-oblique aerial imagery? (This is not an input option in the regular viewshed geoprocessing tool)
8. Python script for a single point can be scraped from the actual viewshed geoprocessing tool
9. The script is identical for a polyline feature, as well
10. If we can input a line to the tool by default, what's the point of using a script?
11. From what I can tell, the value of using a python script would be in specifying fields like maximum viewing distance, observer height, etc, which aren't accessible through the normal tool inputs (or for making a standalone script)
12. These options *are* accessible by tool input through the geodesic viewshed tool, but the geodesic viewshed tool can't run in the GIS online VM due to processing issues.
13. ///change of information
14. Regular viewshed tool is not actually applicable
15. Geodesic viewshed is a must
//////////////////////////////////////////////////////////////////////////////////////////////////

# Functioning Script Process

1. Script totally reevaluated
2. Dr. Morgan's code gathers attribute table information from selected features, into a list  ->
3. Python string and list manipulation generates an SQL query inclusive to each object ID gathered in the aforementioned list  ->
4. Select analysis tool creates a new feature layer using the dynamic sql query  ->
5. Generate Points creates example observer points from the new line selection layer  ->
6. Geodesic viewshed created for every generated observer point.




