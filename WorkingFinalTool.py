import arcpy
import os
# Errors in 139 and 260

##################################################################
#########Change This to the Zip Folder that you extracted#########
##################################################################
outputDirectory = r"C:\data\d1\NRS522\April"
arcpy.env.workspace = outputDirectory
##################################################################
#########DO NOT SET TO ANY OF THE DATA FOLDERS.###################
##################################################################
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox Homes"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [HomeFinder]


class HomeFinder(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Home Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):

        """Define parameter definitions"""
        print("Beginning Home Finder")
        print("Adding Parameters...")
        params = []
        #########################
        print("...Adding Schools")
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = os.path.join(outputDirectory, "schools","schools.shp")
        #input_shp1.value = r"C:\data\d1\NRS522\April\schools\schools.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp1)
        print("...Schools Added")
        #########################
        print("...Adding Roads")
        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = os.path.join(outputDirectory, r"Roads","roads.shp")
        #input_shp2.value = r"C:\data\d1\NRS522\April\Roads\roads.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp2)
        print("...Roads Added")
        #########################
        print("...Adding Shoreline")
        input_shp3 = arcpy.Parameter(name="input_shp3",
                                     displayName="Input shp 3",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp3.value = os.path.join(outputDirectory, r"shoreline","Shoreline.shp")
        #input_shp3.value = r"C:\data\d1\NRS522\April\shoreline\Shoreline.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp3)
        print("...Shoreline Added")
        #########################
        print("...Adding Historic Districts")
        input_shp4 = arcpy.Parameter(name="input_shp4",
                                     displayName="Input shp 4",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp4.value = os.path.join(outputDirectory, r"historic","historic.shp")
        #input_shp4.value = r"C:\data\d1\NRS522\April\historic\historic.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp4)
        print("...Historic Districts Added")
        #########################
        print("...Adding Fishing and Boating Access")
        input_shp5 = arcpy.Parameter(name="input_shp5",
                                     displayName="Input shp 5",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp5.value = os.path.join(outputDirectory, r"fishing","Fishing_and_Boating_Access.shp")
        #input_shp5.value = r"C:\data\d1\NRS522\April\fishing\Fishing_and_Boating_Access.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp5)
        print("...Fishing and Boating Access Added")
        #########################
        print("...Adding Bikeways and Trails")
        input_shp6 = arcpy.Parameter(name="input_shp6",
                                     displayName="Input shp 6",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp6.value = os.path.join(outputDirectory, r"BikewaysState","Bikeways_and_Trails.shp")
        #input_shp6.value = r"C:\data\d1\NRS522\April\BikewaysState\Bikeways_and_Trails.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp6)
        print("...Bikeways and Trails Added")
        #########################
        print("...Adding Hiking Trails")
        input_shp7 = arcpy.Parameter(name="input_shp7",
                                     displayName="Input shp 7",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp7.value = os.path.join(outputDirectory, r"HikingState","HikingState.shp")
        #input_shp7.value = r"C:\data\d1\NRS522\April\HikingState\HikingState.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp7)
        print("...Hiking Trails Added")
        #########################
        print("...Adding Town Boundaries")
        input_shp8 = arcpy.Parameter(name="input_shp8",
                                     displayName="Input shp 8",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp8.value = os.path.join(outputDirectory, r"Towns","towns.shp")
        #input_shp8.value = r"C:\data\d1\NRS522\April\Towns\towns.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp8)
        print("...Town Boundaries Added")
        #########################
        print("...Adding Homes For Sale")
        input_shp9 = arcpy.Parameter(name="input_shp9",
                                     displayName="Input shp 9",
                                     datatype="DETable",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        ################################
        ################################
        input_shp9.value = os.path.join(outputDirectory, r"RhodyHomes","RhodyHomes.xlsx","RhodyHomes$")
        ################################
        ################################
        #input_shp9.value = r"C:\data\d1\NRS522\April\RhodyHomes\RhodyHomes.xlsx\RhodyHomes$"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp9)
        print("...Homes For Sale Added")
        print("All Datasets Added")
        #########################
        print("Now we will add parameters and where clasues")
        print("Adding Parameters and Where Clause...")
        print("...Adding County Clause")
        SelectCounty = arcpy.Parameter(name="SelectCounty",
                                     displayName="Select County or None",
                                     parameterType="Optional",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        SelectCounty.value = "COUNTY IS NOT NULL"
        params.append(SelectCounty)
        print("...County Clause Added")
        #########################
        print("...Adding Hiking and Biking Distance")
        Distance_to_Hiking_Biking =arcpy.Parameter(name="Distance_to_Hiking_Biking",
                                     displayName="Select Distance to Hiking and Biking Trails",
                                     parameterType="Optional",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        Distance_to_Hiking_Biking.value = "5 Miles"
        params.append(Distance_to_Hiking_Biking)
        print("...Hiking and Biking Distance Added")
        #########################
        print("...Adding Fishing and Boating Distance")
        Distance_to_Fishing_Boating =arcpy.Parameter(name="Distance_to_Fishing_Boating",
                                     displayName="Select Distance to Fishing and Boating Access",
                                     parameterType="Optional",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        Distance_to_Fishing_Boating.value = "5 Miles"
        params.append(Distance_to_Fishing_Boating)
        print("...Fishing and Boating Distance Added")
        #########################
        print("...Adding Distance to the shoreline")
        Distance_to_Shore = arcpy.Parameter(name="Distance_to_Shore",
                                    displayName="Select Distance to Shoreline",
                                    parameterType="Optional",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        Distance_to_Shore.value = "8 Miles"
        params.append(Distance_to_Shore)
        print("...Shoreline Distance Added")
        #########################
        print("...Adding School Radius")
        School_Radius =  arcpy.Parameter(name="School_Radius",
                                    displayName="Select Distance to School",
                                    parameterType="Optional",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        School_Radius.value = "10 Miles"
        params.append(School_Radius)
        print("...School Radius Added")
        #########################
        print("...Adding School Type")
        Choose_a_school_type = arcpy.Parameter(name="Choose_a_school_Type",
                                    displayName="Select School Type",
                                    parameterType="Optional",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        Choose_a_school_type.value = "TYPE = 'Public'"
        params.append(Choose_a_school_type)
        print("...School Type Parameter Added")
        #########################
        print("...Adding PRice Range and Property Type")
        Price_Range_and_Proprety_Tyle = arcpy.Parameter(name="Price_Range_and_Property_Tyle",
                                    displayName="Select Property Type",
                                    parameterType="Optional",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        Price_Range_and_Proprety_Tyle.value = "'PRICE' >  '100000'"
        params.append(Price_Range_and_Proprety_Tyle)
        print("... All Parameters Added")
        print("Checking Licenses")

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    print("Licenses Cleared")
    print("Executing Home Finder Based on Parameters...")
    def execute(self, parameters, messages):
        arcpy.env.overwriteOutput = True
        """The source code of the tool."""
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        input_shp3 = parameters[2].valueAsText
        input_shp4 = parameters[3].valueAsText
        input_shp5 = parameters[4].valueAsText
        input_shp6 = parameters[5].valueAsText
        input_shp7 = parameters[6].valueAsText
        input_shp8 = parameters[7].valueAsText
        input_shp9 = parameters[8].valueAsText
        SelectCounty = parameters[9].valueAsText
        Distance_to_Hiking_Biking = parameters[10].valueAsText
        Distance_to_Fishing_Boating = parameters[11].valueAsText
        Distance_to_Shore = parameters[12].valueAsText
        School_Radius = parameters[13].valueAsText
        Choose_a_school_type = parameters[14].valueAsText
        Price_Range_and_Proprety_Tyle = parameters[15].valueAsText

        print("Coverting Excel file to Shapefile...")
        print("...Starting XY Table to Point")
        RhodyHomes = os.path.join(outputDirectory, r"RhodyHomes","RhodyHomes.shp")
        arcpy.management.XYTableToPoint(in_table=input_shp9,
                                        out_feature_class=RhodyHomes,
                                        x_field="LONGITUDE",
                                        y_field="LATITUDE", z_field="",
                                        coordinate_system="GEOGCS['GCS_WGS_1984',"
                                                          "DATUM['D_WGS_1984',"
                                                          "SPHEROID['WGS_1984',6378137.0,298.257223563]],"
                                                          "PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];"
                                                          "-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;"
                                                          "0.001;0.001;IsHighPrecision")
        print("...Shapefile created!")
        #prject homes
        print("Projecting homes to RISP Feet...")
        print("...Starting Project")
        RhodyHomes_Project = os.path.join(outputDirectory, r"RhodyHomes","RhodyHomes_Project.shp")
        arcpy.management.Project(in_dataset=RhodyHomes, out_dataset=RhodyHomes_Project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("...Project Completed")

        # select homes based on price
        print("Selecting Homes Based on Price and Property Type...")
        PricedHomes =  os.path.join(outputDirectory, r"RhodyHomes","PricedHomes.shp")
        arcpy.analysis.Select(in_features=RhodyHomes_Project, out_feature_class=PricedHomes,
                              where_clause=Price_Range_and_Proprety_Tyle)

        print("...Homes Selected")

        #project the towns
        print("Projecting the Town boundaries to RISP Feet")
        print("Starting Project...")
        towns_project = os.path.join(outputDirectory, r"Towns", "towns_project.shp")
        arcpy.management.Project(in_dataset=input_shp8, out_dataset=towns_project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("...Project Finished")

        # Select the county
        print("Selecting the County")
        print("Beginning Select...")
        towns_select =  os.path.join(outputDirectory, r"Towns","towns_select.shp")
        arcpy.analysis.Select(in_features=towns_project, out_feature_class=towns_select,
                              where_clause=SelectCounty)
        print("...County Selected")

        #project the roads
        print("Projecting the Roads to RISP Feet")
        print("Beginning Project...")
        roads_project =  os.path.join(outputDirectory, r"Roads","roads_project.shp")
        arcpy.management.Project(in_dataset=input_shp2, out_dataset=roads_project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("...Project completed")

        #project the schools
        print("Projecting Schools to RISP Feet")
        print("Beginning Project...")
        schools_project =  os.path.join(outputDirectory, r"schools","schools_project.shp")
        arcpy.management.Project(in_dataset=input_shp1, out_dataset=schools_project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("...Project completed")

        # Select the schools
        print("Selecting the School Type")
        print("Beginning Select...")
        schoolType =  os.path.join(outputDirectory, r"schools","schoolType.shp")
        arcpy.analysis.Select(in_features=schools_project, out_feature_class=schoolType,
                              where_clause=Choose_a_school_type)
        print("...School Type Selected")

        #Buffer School Type
        print("Buffering School Radius")
        print("Beginning Buffer...")
        SchoolType_Buffer =  os.path.join(outputDirectory, r"schools","schoolType_Buffer.shp")
        arcpy.analysis.Buffer(in_features=schoolType, out_feature_class=SchoolType_Buffer,
                              buffer_distance_or_field=School_Radius, line_side="FULL", line_end_type="ROUND",
                              dissolve_option="NONE", dissolve_field=[], method="PLANAR")
        print("...School Buffer Complete")

        #Clip roads to buffer
        print("Clipping Roads to School Radius Buffer")
        print("Beginning Clip...")
        neighborhoods1 =  os.path.join(outputDirectory, r"Roads","neighborhoods1.shp")
        arcpy.analysis.Clip(in_features=roads_project, clip_features=SchoolType_Buffer,
                            out_feature_class=neighborhoods1, cluster_tolerance="")
        print("...Clip Completed")

        #Project shoreline
        print("Projecting Shoreline to RISP Feet")
        print("Beginning Project...")
        Shoreline_Project =  os.path.join(outputDirectory, r"shoreline","shoreline_project.shp")
        arcpy.management.Project(in_dataset=input_shp3, out_dataset=Shoreline_Project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("...Shoreline Projection Complete")

        #Buffer Shoreline
        print("Buffering Shoreline")
        print("Beginning Buffer...")
        Shoreline_Buffer1 =  os.path.join(outputDirectory, r"shoreline","shoreline_Buffer1.shp")
        arcpy.analysis.Buffer(in_features=Shoreline_Project, out_feature_class=Shoreline_Buffer1,
                              buffer_distance_or_field=Distance_to_Shore, line_side="FULL", line_end_type="ROUND",
                              dissolve_option="NONE", dissolve_field=[], method="PLANAR")
        print("...Shoreline Buffer Complete")

        # Clip shoreline and schools
        print("Clipping schools within shoreline buffer")
        print("Beginning Clip...")
        ShorelineSchools =  os.path.join(outputDirectory, r"shoreline","ShorelineSchools.shp")
        arcpy.analysis.Clip(in_features=neighborhoods1, clip_features=Shoreline_Buffer1,
                            out_feature_class=ShorelineSchools, cluster_tolerance="")
        print("... Clip Completed")

        #Project Historic Districts
        print("Projecting Historic Districts to RISP Feet")
        print("Beginning Project...")
        HistoricDistricts_Project = os.path.join(outputDirectory, r"historic","historic_project.shp")
        arcpy.management.Project(in_dataset=input_shp4, out_dataset=HistoricDistricts_Project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("... Historic District Projection Completed")

        #Clip shorelineschools to historic districts
        print("Clipping Schools near shoreline to historic districts")
        print("Beginning Clip...")
        ShorelineSchoolsInHistoricDistricts = os.path.join(outputDirectory, r"historic","ShorelineSchoolsInHistoricDistricts.shp")
        arcpy.analysis.Clip(in_features=ShorelineSchools, clip_features=HistoricDistricts_Project,
                            out_feature_class=ShorelineSchoolsInHistoricDistricts, cluster_tolerance="")
        print("...Clip Completed")

        #Project fishing/boating
        print("Projecting Fishing and Boating Access to RISP Feet")
        print("Beginning Projection...")
        Fishing_and_Boating_Access_P =  os.path.join(outputDirectory, r"fishing","Fishing_and_Boating_Access_P.shp")
        arcpy.management.Project(in_dataset=input_shp5,
                                 out_dataset=Fishing_and_Boating_Access_P,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("... Fishing and Boating Projection Completed")

        #Buffer fishing and boating access projection
        print("Buffering Fihing and Boating access")
        print("Beginning Buffer...")
        Fishing_and_Boating_Access_B =  os.path.join(outputDirectory, r"fishing","Fishing_and_Boating_Access_B.shp")
        arcpy.analysis.Buffer(in_features=Fishing_and_Boating_Access_P, out_feature_class=Fishing_and_Boating_Access_B,
                              buffer_distance_or_field=Distance_to_Fishing_Boating, line_side="FULL",
                              line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")
        print("... Buffer Completed")

        #Clips schools and fishing
        print("Clipping Schools and Fishing")
        print("Beginning Clip...")
        neighborhoods2 =  os.path.join(outputDirectory, r"Roads","neighborhoods2.shp")
        arcpy.analysis.Clip(in_features=ShorelineSchoolsInHistoricDistricts, clip_features=Fishing_and_Boating_Access_B,
                            out_feature_class=neighborhoods2, cluster_tolerance="")
        print("...Clip Completed")

        #project bikeways and trails
        print("Projecting Bikeways and Trails to RISP Feet")
        print("Beginning Projection...")
        Bikeways_and_Trails_Project =  os.path.join(outputDirectory, r"BikewaysState","Bikeways_and_Trails_Project.shp")
        arcpy.management.Project(in_dataset=input_shp6, out_dataset=Bikeways_and_Trails_Project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("... Projection Completed")

        #project hiking
        print("Projecting Hiking to RISP Feet")
        print("Beginning Projection...")
        HikingState_Project =  os.path.join(outputDirectory, r"HikingState","HikingState_Project.shp")
        arcpy.management.Project(in_dataset=input_shp7, out_dataset=HikingState_Project,
                                 out_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 transform_method=["WGS_1984_(ITRF00)_To_NAD_1983"],
                                 in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
        print("... Projection Completed")

        #merge hiking and biking
        print("Merge Hiking and Biking Trails")
        print("Beginning Merge...")
        AllTrails = os.path.join(outputDirectory, r"HikingState","AllTrails.shp")
        arcpy.Merge_management(inputs=[Bikeways_and_Trails_Project, HikingState_Project], output=AllTrails)
        print("...Merge Completed")

        # buffer alltrails
        print("Buffer All Trails")
        print("Beginning Buffer...")
        alltrails_Buffer =  os.path.join(outputDirectory, r"HikingState","AllTrails_Buffer.shp")
        arcpy.analysis.Buffer(in_features=AllTrails, out_feature_class=alltrails_Buffer,
                              buffer_distance_or_field=Distance_to_Hiking_Biking, line_side="FULL",
                              line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")
        print("... Buffer Complete")

        #clip neighborhoods to trails buffer
        print("Clip possible neighborhoods to trails...")
        print("Beginning Clip...")
        neighborhoods3 =  os.path.join(outputDirectory, r"Roads","neighborhoods3.shp")
        arcpy.analysis.Clip(in_features=neighborhoods2, clip_features=alltrails_Buffer,
                            out_feature_class=neighborhoods3, cluster_tolerance="")
        print("...Clip Completed")

        #transform to polygon
        print("Transform these areas to polygons")
        print("Beginning Transform...")
        Npolys =  os.path.join(outputDirectory, r"Roads","Npolys.shp")
        arcpy.management.FeatureToPolygon(in_features=[neighborhoods3], out_feature_class=Npolys, cluster_tolerance="",
                                          attributes="ATTRIBUTES", label_features="")
        print("...Transform Completed")

        # Buffer to find suitable neighborhoods
        print("Buffer areas to find suitable neighborhoods")
        print("Beginning Buffer...")
        SuitableNeighborhoods =  os.path.join(outputDirectory, r"Roads","SuitableNeighborhoods.shp")
        arcpy.analysis.Buffer(in_features=Npolys, out_feature_class=SuitableNeighborhoods,
                              buffer_distance_or_field="0.25 Miles", line_side="FULL", line_end_type="ROUND",
                              dissolve_option="NONE", dissolve_field=[], method="PLANAR")
        print("... Buffer Completed")

        # clip selected towns
        print("Clip Selected Towns from earlier to suitable neighborhoods")
        print("Beginning Clip...")
        BestAreas =  os.path.join(outputDirectory, r"BestAreas.shp")
        arcpy.analysis.Clip(in_features=towns_select, clip_features=SuitableNeighborhoods,
                            out_feature_class=BestAreas, cluster_tolerance="")
        print("...Clip Completed")
        print("Now we have the Best Areas for a new home")

        # clips best areas to best homes
        print("Choosing Best Homes in Best Area")
        print("Beginning Clip...")
        BestHomes =  os.path.join(outputDirectory, r"BestHomes.shp")
        arcpy.analysis.Clip(in_features=PricedHomes, clip_features=BestAreas, out_feature_class=BestHomes,
                            cluster_tolerance="")
        print("... Clip Completed")
        print("BestHomes.shp is now available to view")
        print("Thank you!")
        return

# This code block allows you to run your code in a test-mode within PyCharm, i.e. you do not have to open the tool in
# ArcMap. This works best for a "single tool" within the Toolbox.
def main():

    tool = HomeFinder()
    tool.execute(tool.getParameterInfo(), None)

if __name__ == '__main__':
    main()