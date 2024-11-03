import os

file_path = "LibraryProject/README.md"

if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
    print("README.md file is non-empty.")
else:
    print("README.md file is empty or does not exist.")
