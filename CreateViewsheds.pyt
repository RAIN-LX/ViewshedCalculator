# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "CreateViewshed"
        self.alias = "createviewshed"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Viewshed"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = [
            arcpy.Parameter(
                displayName="Observer Points",
                name="observer_input",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Input"),

            arcpy.Parameter(
                displayName="Elevation Input",
                name="elevation_input",
                datatype="GPRasterLayer",
                parameterType="Required",
                direction="Input"),

            arcpy.Parameter(
                displayName="Observer Elevation",
                name="observer_height",
                datatype="GPLinearUnit",
                parameterType="Required",
                direction="Input"),

            arcpy.Parameter(
                displayName="Sight Distance",
                name="observer_viewdist",
                datatype="GPLinearUnit",
                parameterType="Required",
                direction="Input"),

            arcpy.Parameter(
                displayName="Spatial Reference",
                name="projectionref",
                datatype="GPSpatialReference",
                parameterType="Required",
                direction="Input"),

            arcpy.Parameter(
                displayName="Output Name",
                name="outRaster",
                datatype="DEDiskConnection",
                parameterType="Required",
                direction="Output"),

            arcpy.Parameter(
                displayName="Input Workspace",
                name="in_workspace",
                datatype="DEWorkspace",
                parameterType="Derived",
                direction="Output")
            ]        
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        parameters[2].value = "15 feet"
        parameters[3].value = "2 miles"
        

        try:
            # https://pro.arcgis.com/en/pro-app/3.3/arcpy/classes/spatialreference.htm
            if arcpy.Describe(parameters[0]).spatialReference:
                parameters[4].value = arcpy.Describe(parameters[0]).spatialReference
        except Exception:
            pass


        parameters[6].defaultEnvironmentName = "workspace"

        return

    def updateMessages(self, parameters):
        arcpy.AddMessage("{0} is {1}:".format("param 0: ", parameters[0].valueAsText))
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #geodesic viewshed
        #Get projection from MHWL data and put in variable e.g. outCoordSys

        #NAD903 = 'PROJCS["NAD_1983_2011_StatePlane_Florida_North_FIPS_0903_Ft_US",GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1968500.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-84.5],PARAMETER["Standard_Parallel_1",29.58333333333333],PARAMETER["Standard_Parallel_2",30.75],PARAMETER["Latitude_Of_Origin",29.0],UNIT["Foot_US",0.3048006096012192]],VERTCS["NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'
        # We can also just get the projection from one of our input files that we are already sure is in the right projection
        feature_class = parameters[0].valueAsText 
        desc = arcpy.Describe(feature_class)
        sr = desc.spatialReference
        print(sr.name)  # Prints the name of the projection
        print(sr.factoryCode)  # Prints the factory code of the projection

        # #other variables
        # workspace = parameters[6].valueAsText

        arcpy.AddMessage("{0} is {1}:".format("param 0: ", parameters[0].valueAsText))
        arcpy.AddMessage("{0} is {1}:".format("param 1: ", parameters[1].valueAsText))
        arcpy.AddMessage("{0} is {1}:".format("param 2: ", parameters[2].valueAsText))
        arcpy.AddMessage("{0} is {1}:".format("param 3: ", parameters[3].valueAsText))
        arcpy.AddMessage("{0} is {1}:".format("param 4: ", parameters[4].valueAsText))
        arcpy.AddMessage("{0} is {1}:".format("param 5: ", parameters[5].valueAsText))

        

        # Since the project is in feet let's keep the parameters in feet as well e.g. 6 feet on observer elevation
        with arcpy.da.SearchCursor(parameters[0].valueAsText,['SHAPE@','FID']) as cursor:
            for row in cursor:
                arcpy.AddMessage("Running viewshed number {}".format(row[1]))
                # with arcpy.EnvManager(outputCoordinateSystem=sr, parallelProcessingFactor="100%", scratchWorkspace=workspace):
                #     out_raster = arcpy.sa.Viewshed2(
                #         in_raster=parameters[1].valueAsText,
                #         in_observer_features=row[0],
                #         out_agl_raster=None,
                #         analysis_type="FREQUENCY",
                #         vertical_error="0 Meters",
                #         out_observer_region_relationship_table=None,
                #         refractivity_coefficient=0.13,
                #         surface_offset="0 Meters",
                #         observer_elevation=parameters[2].valueAsText,
                #         observer_offset="1 Meters",
                #         inner_radius=None,
                #         inner_radius_is_3d="GROUND",
                #         outer_radius=parameters[3].valueAsText,
                #         outer_radius_is_3d="GROUND",
                #         horizontal_start_angle=0,
                #         horizontal_end_angle=360,
                #         vertical_upper_angle=90,
                #         vertical_lower_angle=-90,
                #         analysis_method="ALL_SIGHTLINES",
                #         analysis_target_device="CPU_ONLY"
                #     )
                #     out_raster.save(parameters[5].valueAsText + str(row[1]) +".tif")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
