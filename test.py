# C:\Users\kb137\OneDrive\Documents\PythonPrograms\MyArwReader\test.py
import os
from MyArwReader import ARWReader

# Find all .arw files
arw_dir = "MyArwReader"
file_paths = [os.path.join(arw_dir, f) for f in os.listdir(arw_dir) if f.lower().endswith('.arw')]

# Test metadata extraction
for file_path in file_paths:
    reader = ARWReader(file_path)
    meta = reader.get_metadata()
    print(f"File: {reader.file_path}")
    print(f"ISO: {meta['EXIF:ISO']}")
    print(f"Camera: {meta['EXIF:Model']}")
    print(f"DateTimeOriginal: {meta['EXIF:DateTimeOriginal']}")
    print()


# test.py
# from MyArwReader import ARWReader

# Use the correct absolute path to an existing .ARW file
file_path = "MyArwReader/sample.ARW"  # Relative to C:\Users\kb137\OneDrive\Documents\PythonPrograms\MyArwReader
reader = ARWReader(file_path)
metadata = reader.get_metadata()
print(metadata)  # Print full metadata dictionary



from MyArwReader import ARWReader

reader = ARWReader("photo.ARW")  # A real .ARW file I had
print(f"ISO: {reader.get_tag('EXIF:ISO')}")
print(f"Date: {reader.get_tag('EXIF:DateTimeOriginal')}")