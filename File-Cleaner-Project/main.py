import os
from extensions import extension_paths
from processes import *
import shutil

#Get path to downloads and desktop directories
DOWNLOADPATH = os.path.join(os.path.expanduser("~"), 'Downloads')
DESKTOPPATH = os.path.join(os.path.expanduser("~"), 'Desktop') 

#Find scattered files
desktopFiles = find_files_on_desktop()
downloadFiles = find_files_in_downloads()

#Organize desktop files
for file in desktopFiles:
    extension = get_file_options(file, "ext")
    if (extension in extension_paths):
        newDir = extension_paths[extension]
        newDirPath = os.path.join(DESKTOPPATH, newDir)
        newFilePath = os.path.join(DESKTOPPATH, file)      

        if not os.path.exists(newDirPath):
            create_directory_in_desktop(newDir)
        #If the file already exists move it to the suggested_delete folder
        if (os.path.exists(os.path.join(newDirPath, file))):
            deletePath = os.path.join(DESKTOPPATH, 'other/suggested_delete')
            renameDuplicates(newFilePath)
            shutil.move(newFilePath, deletePath)
        else:
            shutil.move(newFilePath, newDirPath)
    
#Organize download files
for file in downloadFiles:
    extension = get_file_options(file, "ext")
    if (extension in extension_paths):
        newDir = extension_paths[extension]
        newDirPath = os.path.join(DESKTOPPATH, newDir)
        newFilePath = os.path.join(DOWNLOADPATH, file)      
        if not os.path.exists(newDirPath):
            create_directory_in_desktop(newDir) 
        if (os.path.exists(os.path.join(newDirPath, file))):
            delete = os.path.join(DESKTOPPATH, 'other/delete')
            renameDuplicates(newFilePath)
            shutil.move(newFilePath, delete)
        else:
            shutil.move(newFilePath, newDirPath)
