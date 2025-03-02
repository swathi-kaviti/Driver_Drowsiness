import os
import pandas as pd
import shutil

# Load the CSV file
df = pd.read_csv('labels.csv')
print(df.columns)

# Set your paths
image_folder = 'images'
drowsy_folder = 'drowsy'
awake_folder = 'awake'

# Create folders if they don’t exist
os.makedirs(drowsy_folder, exist_ok=True)
os.makedirs(awake_folder, exist_ok=True)

# Loop through the rows and move the images
for index, row in df.iterrows():
    image_name = row['filename']
    
    # Determine the label based on drowsy/awake columns
    if row[' drowsy'] == 1 and row[' awake'] == 0:
        label = 'drowsy'
        dest_folder = drowsy_folder
    elif row[' drowsy'] == 0 and row[' awake'] == 1:
        label = 'awake'
        dest_folder = awake_folder
    else:
        print(f"Skipping {image_name}: Invalid or conflicting label")
        continue

    source_path = os.path.join(image_folder, image_name)
    dest_path = os.path.join(dest_folder, image_name)

    # Move the image to the respective folder
    if os.path.exists(source_path):
        shutil.move(source_path, dest_path)
        print(f"Moved {image_name} to {label} folder")
    else:
        print(f"Image {image_name} not found in the source folder")

print("Image classification complete!")
