import os

# Replace with your image file path
folder_path = r"."

# Replace to fit how you would like to rename your files
prefix = "banana-00-"



# Get all image files
files = [f for f in os.listdir(folder_path)
         if f.lower().endswith('.png')] #change for ur img extension

# Sort files for consistent ordering
files.sort()

for index, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)

    extension = os.path.splitext(filename)[1]
    new_filename = f"{prefix}{index:03d}{extension}"  # banana-00-001.png, banana-00-002.png...
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)

print(f"Renamed {len(files)} images successfully!")