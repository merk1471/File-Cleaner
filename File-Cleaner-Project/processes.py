import os
from pathlib import Path

#Get path to downloads and desktop directories
DOWNLOADPATH = os.path.join(os.path.expanduser("~"), 'Downloads')
DESKTOPPATH = os.path.join(os.path.expanduser("~"), 'Desktop') 

#function to split file name
def get_file_options(file_path, option):
    base_name, extension = os.path.splitext(file_path)
    if (option == "ext"):
        return extension
    elif (option == "base"):
        return base_name
    
#Function to create directories
def create_directory_in_desktop(directory_path):
    # Create the directory if it doesn't exist
    newDirPath = os.path.join(DESKTOPPATH, directory_path)
    if not os.path.exists(newDirPath):
        os.makedirs(newDirPath)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")

#Find scattered desktop files (not in a folder)
def find_files_on_desktop():
    # Get the path to the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Initialize a list to store file names
    files_on_desktop = []
    
    # Iterate through all items on the desktop
    for item in os.listdir(desktop_path):
        # Construct the full path for the item
        item_path = os.path.join(desktop_path, item)
        # Check if the item is a file
        if os.path.isfile(item_path):
            files_on_desktop.append(item)
    
    return files_on_desktop

#Find scattered download files (not in a folder)
def find_files_in_downloads():
    # Get the path to the user's desktop directory
    
    # Initialize a list to store file names
    download_files = []
    
    # Iterate through all items on the desktop
    for item in os.listdir(DOWNLOADPATH):
        # Construct the full path for the item
        item_path = os.path.join(DOWNLOADPATH, item)
        # Check if the item is a file
        if os.path.isfile(item_path):
            download_files.append(item)
    
    return download_files

def renameDuplicates(path):
    deletePath = os.path.join(DESKTOPPATH, 'other/suggested_delete')
    os.path.join(path, deletePath)
 
    stem = path.stem
    suffix = path.suffix
    counter = 1

    newPath = path

    while newPath.exists():
        new_name = f"{stem} ({counter}){suffix}"
        os.rename(path, new_name)
        newPath = os.path.join(deletePath, new_name)
        counter += 1


    return str(newPath)


