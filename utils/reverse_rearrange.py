#Use this file if u need to reverse ur splitting of images to train, test and validation
#This file needs to be in the folder with ur other folders of images
#structure:
    #test/
    #train/
    #valid/
    #this file (reverse rearrange.py)

import os
import shutil

root_dir = os.getcwd()

# Split folders to restore from
split_folders = ["train", "valid", "test"]

for split in split_folders:
    split_path = os.path.join(root_dir, split)

    if not os.path.exists(split_path):
        continue

    for filename in os.listdir(split_path):
        src = os.path.join(split_path, filename)

        if not os.path.isfile(src):
            continue

        # Separate folder name and original filename
        try:
            folder_name, original_name = filename.split("_", 1)     #banana01_001.png => folder_name = banana01, 
                                                                                        #original_name = 001
        except ValueError:
            print(f"Skipping {filename} (cannot determine original folder)")
            continue

        # Create original folder if needed
        #Change the -2 if needed. If the folder_name is banana01, then [-2:] will give you 01. thats what you want
        original_folder = os.path.join(root_dir, folder_name[-2:])
        os.makedirs(original_folder, exist_ok=True)

        #use filename here to keep original name of the file
        dst = os.path.join(original_folder, filename)

        shutil.move(src, dst)

        print(f"Moved {filename} -> {folder_name}/{original_name}")

print("Restoration complete.")