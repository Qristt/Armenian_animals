import json, os


def all_json_files(dir_path):
    all_items = os.listdir(dir_path)
    json_file_paths = [os.path.join(dir_path, item) for item in all_items if ".json" in item]
    return json_file_paths


def update_label(json_file_path):

    # Read json file
    f = open(json_file_path)  # Opening JSON file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()

    new_label = data["imagePath"].split(".")[0]
    elements = new_label.split("_")[:-1]
    new_label = "-".join(elements)

    items = data["shapes"]


    for item in items:
        # initial_label = item["label"]
        item["label"] = new_label


    g = open(json_file_path, "w")
    with g as outfile:
        json.dump(data, outfile, indent=2)



dir_path = input("Please input the directory path to the annotation json files.\n")
json_file_paths = all_json_files(dir_path)

for json_file_path in json_file_paths:
    print(">", end = " ")

    update_label(json_file_path)


print("\nDone! All files updated.")



























