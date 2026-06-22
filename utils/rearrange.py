#This file needs to be in the folder with ur other folders of images
#structure:
    #01/
    #02/
    #03/
    #04/
    #05/
    #this file (rearrange.py)

#important thing is the filename, since we will be using it too to rename our images
import os
import shutil

root_dir = os.getcwd()
prefix = "banana"
file_extension = ".png"

# Create output folders
for split in ["train", "valid", "test"]:
    os.makedirs(os.path.join(root_dir, split), exist_ok=True)

# Process each subfolder
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)

    # Skip non-folders and output folders
    if (not os.path.isdir(folder_path)
            or folder_name in ["train", "valid", "test"]):
        continue

    # Get images (do NOT trust filename structure)
    images = sorted([
        f for f in os.listdir(folder_path)
        if file_extension in f.lower()
    ])

    total = len(images)

    if total == 0:
        continue

    train_count = round(total * 0.8)
    valid_count = round(total * 0.1)

    # Indices to assign to valid and test
    valid_indices = {
        round(i * (total - 1) / (valid_count - 1))
        for i in range(valid_count)
    } if valid_count > 1 else set()

    remaining = [i for i in range(total) if i not in valid_indices]

    test_count = total - train_count - valid_count

    test_indices = {
        remaining[round(i * (len(remaining) - 1) / (test_count - 1))]
        for i in range(test_count)
    } if test_count > 1 else set()

    moved_train = moved_valid = moved_test = 0

    # counters for clean renaming per split
    train_i = valid_i = test_i = 1

    for idx, img in enumerate(images):
        src = os.path.join(folder_path, img)

        if idx in valid_indices:
            new_name = f"{prefix}{folder_name}_{valid_i:03d}{file_extension}"
            dst = os.path.join(root_dir, "valid", new_name)
            valid_i += 1
            moved_valid += 1

        elif idx in test_indices:
            new_name = f"{prefix}{folder_name}_{test_i:03d}{file_extension}"
            dst = os.path.join(root_dir, "test", new_name)
            test_i += 1
            moved_test += 1

        else:
            new_name = f"{prefix}{folder_name}_{train_i:03d}{file_extension}"
            dst = os.path.join(root_dir, "train", new_name)
            train_i += 1
            moved_train += 1

        shutil.move(src, dst)

    print(f"{folder_name}:")
    print(f"  Train: {moved_train}")
    print(f"  Valid: {moved_valid}")
    print(f"  Test : {moved_test}")