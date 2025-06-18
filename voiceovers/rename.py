import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through all files in the directory
for filename in os.listdir(script_dir):
    # Check if the file has a .mp3 extension
    if filename.endswith('.mp3'):
        # Create the new filename with .ogg extension
        new_filename = filename.replace('.mp3', '.ogg')
        # Get the full paths
        old_file = os.path.join(script_dir, filename)
        new_file = os.path.join(script_dir, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} to {new_filename}')