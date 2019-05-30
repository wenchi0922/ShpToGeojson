import shapefile
import os
from json import dumps

dir = os.fsencode("my_dir")

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    if filename.endswith(".shp"):
        path = os.path.join("my_dir", filename)
#         print(path)
        sf = shapefile.Reader(path)
#         print(sf)
        fields = sf.fields[1:]
        field_names = [field[0] for field in fields]
#         print(field_names)
        buffer = []
        for sr in sf.shapeRecords():
            atr = dict(zip(field_names, sr.record))
            geom = sr.shape.__geo_interface__
            buffer.append(dict(type="Feature", 
                      geometry = geom, properties = atr))
            new_file_name = filename + ".geojson"
            geojson = open(new_file_name, "w")
            
        geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
        geojson.close()
