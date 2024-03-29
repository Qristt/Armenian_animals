import os
# import numpy as np
import json


json_file = input("Please input the path to the json file.\n")
new_name = input("Please input the new file name.\n")
# Read json file
# Opening JSON file
f = open(json_file)

# returns JSON object as a dictionary
data = json.load(f)

f.close()

objs = data['annotations']

for i in range(len(objs)):
    removed_value = objs[i].pop('segmentation')
    
h, t = os.path.split(json_file)
updated_file = os.path.join(h, new_name)

g = open(updated_file, "w")
with g as outfile:
    json.dump(data, outfile, indent=2)
