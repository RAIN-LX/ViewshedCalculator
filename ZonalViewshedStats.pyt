#unmodified placeholder script
out_raster = arcpy.sa.ZonalStatistics("Statewide_Land_Use_Land_Cover", "OBJECTID", "VB_Transect01.tif", "MEAN", "DATA", "CURRENT_SLICE", 90, "AUTO_DETECT", "ARITHMETIC", 360); out_raster.save(r"C:\Users\ndc18\Documents\ArcGIS\Packages\FLSeaGrantGISWork_ab7f47\commondata\flseagrantgiswork.gdb\ZonalSt_Stat1")
