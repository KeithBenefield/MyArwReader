# MyArwReader
A lightweight Python package to read metadata from Sony .ARW files.

## Overview
`MyArwReader` provides a simple interface to extract metadata from .ARW files using the `pyexiftool` library. It supports accessing all metadata tags (EXIF, XMP, IPTC, etc.) or specific tags like ISO, camera model, or timestamp.

## Installation
```bash
pip install path/to/MyArwReader-0.1.0-py3-none-any.whl

## Requirements
Python: 3.6 or higher
pyexiftool: Installed automatically as a dependency
exiftool: Must be installed separately and available in your system PATH. Download from the official ExifTool website and follow the installation instructions.


Usage
Basic Example
Extract specific metadata tags from an .ARW file:

from MyArwReader import ARWReader

file_path = "path/to/your/file.ARW"
reader = ARWReader(file_path)
print(f"File: {reader.file_path}")
print(f"ISO: {reader.get_tag('EXIF:ISO')}")
print(f"Camera: {reader.get_tag('EXIF:Model')}")
print(f"DateTimeOriginal: {reader.get_tag('EXIF:DateTimeOriginal')}")

Full Metadata Example

from MyArwReader import ARWReader

reader = ARWReader("path/to/your/file.ARW")
metadata = reader.get_metadata()
print(metadata)

Batch Processing Example
Process multiple .ARW files in a directory:

import os
from MyArwReader import ARWReader

arw_dir = "path/to/your/arw/files"
file_paths = [os.path.join(arw_dir, f) for f in os.listdir(arw_dir) if f.lower().endswith('.arw')]

for file_path in file_paths:
    reader = ARWReader(file_path)
    print(f"File: {reader.file_path}")
    print(f"ISO: {reader.get_tag('EXIF:ISO')}")
    print(f"Camera: {reader.get_tag('EXIF:Model')}")
    print(f"DateTimeOriginal: {reader.get_tag('EXIF:DateTimeOriginal')}")
    print()

Methods
get_metadata(): Returns a dictionary of all metadata tags.
get_tag(tag): Returns the value of a specific tag (e.g., 'EXIF:ISO') or None if not found. For a list of Sony-specific EXIF tags, see the Sony Tag ID documentation. https://exiftool.org/TagNames/Sony.html

Notes
Ensure your .ARW file paths are valid; a FileNotFoundError will be raised if the file doesn’t exist.
Install exiftool separately and ensure it’s in your system PATH for pyexiftool to work. See the ExifTool download page for the latest version. https://exiftool.org/

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
ARWEnthusiast

MIT License

Copyright (c) 2025 ARWEnthusiast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Step 2: Updated `README.md` with `get_tags`
Here’s a polished version adding `get_tags`, assuming the above as a base (adjust if yours differs):

## Get Multiple Tags (New in v0.1.2)
from MyArwReader import ARWReader

reader = ARWReader("photo.arw")
tags = reader.get_tags(["EXIF:ISO", "EXIF:DateTimeOriginal"])
print(f"ISO: {tags['EXIF:ISO']}")
print(f"Date: {tags['EXIF:DateTimeOriginal']}")
