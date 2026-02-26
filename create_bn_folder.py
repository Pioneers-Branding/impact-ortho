import os
import shutil
import glob

base_dir = '/Users/bp/Desktop/impact-ortho'
bn_dir = os.path.join(base_dir, 'bn')

# Create bn directory
os.makedirs(bn_dir, exist_ok=True)

# Copy directories
for d in ['components', 'assets', 'data']:
    src = os.path.join(base_dir, d)
    dest = os.path.join(bn_dir, d)
    if os.path.exists(src):
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

# Copy all PHP files
for file_path in glob.glob(os.path.join(base_dir, '*.php')):
    if os.path.isfile(file_path):
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(bn_dir, file_name)
        shutil.copy2(file_path, dest_path)

print(f"Successfully created '{bn_dir}' and copied all relevant files for the Bengali (bn) sub-folder structure.")
