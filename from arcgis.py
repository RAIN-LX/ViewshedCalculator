import arcpy
from arcpy import env
env.overwriteOutput = True

#https://support.esri.com/en-us/knowledge-base/how-to-transfer-content-from-one-arcgis-online-organiza-000022252
#https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/
from arcgis.gis import GIS
from arcgis.gis import User


print("ArcGIS Online Org account")    
gis = GIS('home')
print("Logged in as " + str(gis.properties.user.username))
username = str(gis.properties.user.username)


# https://developers.arcgis.com/python/latest/guide/accessing-item-resources/


query_string = f"owner: {gis.users.me.username}"
user_items = gis.content.search(query=query_string, max_items=-1)
print(len(user_items), 'items returned belonging to current user')
user_items[:5]

for item in user_items:
    if "Mexico Beach" in item.title:
        print(item.title)
        try:
            item.delete()
            print(f"Item '{item.title}' deleted successfully.")
        except Exception as e:
            print(f"Failed to delete item with ID {item.title}: {e}")