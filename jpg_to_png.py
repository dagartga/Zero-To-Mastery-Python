'''
    jpgtopng.py converts jpeg files into png files
    
    Calling the python file takes two directories as arguments
    
    The first argument is the directory that currently has jpeg files
    
    The second argument is the directory where the newly created png files will be saved
    
    Example: 
    
        $python jpgtopng.py ./jpeg_folder/ ~/Pictures

        This will convert all the .jpg files from jpeg_folder directory into .png files
        and will save the new .png files in the ~/Pictures directory
'''



from pathlib import Path
import sys
import os
import re
from PIL import Image


regex = re.compile(r"(.+)\.jpg")


current_dir = sys.argv[1]
new_dir = sys.argv[2]

print(current_dir)
print(new_dir)

current_dir_path = Path(current_dir)
new_dir_path = Path(new_dir)

if current_dir_path.exists() and new_dir_path.exists():
    print("The file directory exists")
    for filename in os.listdir(current_dir):
        if ".jpg" in filename:
            re_search = regex.search(filename)
            file_prefix = re_search[1]
            img = Image.open(os.path.join(current_dir + filename))
            print(f'File {filename} has been opened')
            new_filename = str(file_prefix) + '.png'
            img.save(new_dir + new_filename, "png")
            print(f'The file has been saved as {new_filename}')
            

else:
    print("The file directory does not exist")
