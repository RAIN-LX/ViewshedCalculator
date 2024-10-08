#setting up the viewshed tool allows you to copy what would have been a regular geoprocessing run 
#into an in-ArcGIS python command (for use in a window or notebook)

#this is what the command looks like setup for my test environment
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_UTM_Zone_16N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-87.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]],VERTCS["NAD_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'):
    out_raster = arcpy.sa.Viewshed("FL_GulfCoast_T_ProjectRaster", "ObserverPoints", 1, "FLAT_EARTH", 0.13, None); out_raster.save(r"S:\Viewshed\ViewshedAnalysisOUR\ViewshedAnalysisOUR.gdb\Viewshe_FL_G3"))

#here's the same geoprocessing tool setup, but with a polyline shape selected instead of a point
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_UTM_Zone_16N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-87.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]],VERTCS["NAD_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'):
    out_raster = arcpy.sa.Viewshed("FL_GulfCoast_T_ProjectRaster", "LineTest", 1, "FLAT_EARTH", 0.13, None); out_raster.save(r"S:\Viewshed\ViewshedAnalysisOUR\ViewshedAnalysisOUR.gdb\Viewshe_FL_Line"))
    
#as you can see, they're exactly the same in format

