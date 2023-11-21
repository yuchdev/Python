import os
import shutil

# Loop through directories from 00_* to 12_*
for i in range(13):
    src_dir = "{:02d}_".format(i)
    dest_dir = "{:02d}_".format(i + 1)

    # Check if the source directory exists
    if os.path.exists(src_dir):
        # Perform the rename operation
        shutil.move(src_dir, dest_dir)
        print(f"Moved {src_dir} to {dest_dir}")

# After renaming, you might want to stage and commit the changes in Git
os.system("git add .")
os.system("git commit -m 'Rename directories'")
