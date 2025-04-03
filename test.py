# test.py
from MyArwReader import ARWReader

reader = ARWReader("photo.arw")
tags = reader.get_tags(["EXIF:ISO", "EXIF:DateTimeOriginal"])
print(f"ISO: {tags['EXIF:ISO']}")
print(f"Date: {tags['EXIF:DateTimeOriginal']}")