import os

# replace with your image file path
folder_path = r"."


# Get all image files
files = [f for f in os.listdir(folder_path)
         if f.lower().endswith('.png')] #change for ur file extension

# Sort files for consistent ordering
files.sort()

# Rename files
for index, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)

    extension = os.path.splitext(filename)[1]
    new_filename = f"banana-00-{index:03d}{extension}"  # banana-00-001.png, banana-00-002.png...
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)

print(f"Renamed {len(files)} images successfully!")