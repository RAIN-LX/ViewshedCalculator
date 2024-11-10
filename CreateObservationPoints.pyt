# -*- coding: utf-8 -*-
# Purpose: This script will take as input a selected line feature and a percentage spacing value. 
#          These input points along the line will be generated, resulting in observation points. 
# Good video overview: https://youtu.be/nPUkTyDaIhg?si=TpcJ1EfNzX4VG4L7
# Also, the direct docs https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Create Observation Points"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = [
            arcpy.Parameter(
                displayName="Input Features",
                name="in_features",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Input")            
        ]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        in_feature_layer = parameters[0].valueAsText
        arcpy.AddMessage(in_feature_layer)

        #May not need to programmatically get selected features because 
        #appears to be an option on the tool to use selected featrues         
        selected_features = arcpy.Describe(in_feature_layer).FIDSet
        query_list = f"({','.join([val for val in selected_features.split(';')])})"
        arcpy.AddMessage(query_list) 
        # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/generate-points-along-lines.htm

        workspace = r"G:\My Drive\Projects\FlSeaGrantHurricaneViewsheds\Data\PensacolaBeach"
        pointOutput = workspace + "\ObserverPoints"
        pointSpacing = 10        
        arcpy.management.GeneratePointsAlongLines(
            Input_Features= in_feature_layer,
            Output_Feature_Class= pointOutput,
            Point_Placement="PERCENTAGE",
            Percentage=pointSpacing,
            Include_End_Points="NO_END_POINTS",
        )     
        arcpy.AddMessage("Finished creating observation points")    
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
