from PIL import Image 
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data 

def _get_if_exist(data, key):
    if key in data:
        return data[key]
    else: 
        pass

def get_lat_lon(exif_data):
    gps_info = exif_data["GPSInfo"]
    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, "GPSLatitudeRef")
        gps_longitude = _get_if_exist(gps_info, "GPSLongitude")
        gps_longitude_ref = _get_if_exist(gps_info, "GPSLongitudeRef")

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degrees(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = _convert_to_degrees(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

        return lat, lon
    

if __name__ == "__main__":
    #
    image = Image.open("photo directory")
    exif_data = get_exif_data(image)
    print(get_lat_lon(exif_data))


#     import glob
# file_names = []
# for name in glob.glob(photo directory):
#     file_names.append(name)

# for item in file_names: 
#     if __name__ == "__main__":
#         image = Image.open(item)
#         exif_data = get_exif_data(image)
#         print(get_lat_lon(exif_data))
#     else:
#         pass 
          
