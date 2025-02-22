from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
# conda install pillow
from osgeo import ogr, osr
import math

def get_gps_metadata(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        
        if not exif_data:
            return None
        
        gps_info = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == "GPSInfo":
                for gps_tag in value:
                    sub_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                    gps_info[sub_tag_name] = value[gps_tag]
                    print(f"Name {sub_tag_name} Value {value[gps_tag]}")
        if gps_info:
            lat = convert_to_degrees(gps_info.get("GPSLatitude"), gps_info.get("GPSLatitudeRef"))
            lon = convert_to_degrees(gps_info.get("GPSLongitude"), gps_info.get("GPSLongitudeRef"))
            return lat, lon
        return None

def convert_to_degrees(value, ref):
    """Convert EXIF GPS coordinates to decimal degrees."""
    if value:
        d, m, s = value
        result = d + (m / 60.0) + (s / 3600.0)
        if ref in ['S', 'W']:
            result = -result
        return result
    return None

def generate_footprint(lat, lon, fov_h=94.4, fov_v=73.6, altitude=10):
    """Generate an approximate footprint polygon given GPS and altitude."""
    # Calculate approximate ground coverage using basic trigonometry
    # For simplicity, assuming nadir shot (looking straight down)
    ground_width = 2 * altitude * math.tan(math.radians(fov_h / 2))
    ground_height = 2 * altitude * math.tan(math.radians(fov_v / 2))

    # Offset in degrees (approx., assuming ~111 km/degree lat and lon at equator)
    deg_width = ground_width / 111000
    deg_height = ground_height / 111000

    # Create polygon corners
    ring = ogr.Geometry(ogr.wkbLinearRing)
    ring.AddPoint(lon - deg_width / 2, lat - deg_height / 2)
    ring.AddPoint(lon + deg_width / 2, lat - deg_height / 2)
    ring.AddPoint(lon + deg_width / 2, lat + deg_height / 2)
    ring.AddPoint(lon - deg_width / 2, lat + deg_height / 2)
    ring.AddPoint(lon - deg_width / 2, lat - deg_height / 2)

    # Create polygon
    polygon = ogr.Geometry(ogr.wkbPolygon)
    polygon.AddGeometry(ring)

    # Set spatial reference (WGS84)
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4269)
    polygon.AssignSpatialReference(srs)

    return polygon


img_path = r"C:\Data\PhD\Projects\FlSeaGrantHurricaneViewsheds\FieldWork\MexicoBeach\Transect0\GOPR0055.JPG"
gps_coords = get_gps_metadata(img_path)

if gps_coords:
    footprint = generate_footprint(*gps_coords, altitude=50)  # Example altitude: 50m
    print("Footprint WKT:", footprint.ExportToWkt())
else:
    print("GPS metadata not found in image.")