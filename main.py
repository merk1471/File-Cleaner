import os
from extensions import extension_paths
from processes import *

#Get path to downloads and desktop directories
DOWNLOADPATH = os.path.join(os.path.expanduser("~"), 'Downloads')
DESKTOPPATH = os.path.join(os.path.expanduser("~"), 'Desktop') 


unorganizedFiles = find_files_on_desktop()

for file in unorganizedFiles:
    extension = get_file_options(file, "ext")
    if (extension in extension_paths):
        newDir = extension_paths[extension]
        newDirPath = os.path.join(DESKTOPPATH, newDir)
        newFilePath = os.path.join(DESKTOPPATH, file)      
        if not os.path.exists(newDirPath):
            create_directory_in_desktop(newDir)
        shutil.move(newFilePath, newDirPath)
    

    
    
