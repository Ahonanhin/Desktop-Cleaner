import os
import shutil
import time

# Dictionary of file extensions and the folder to move them to
extensions = {
    "images": ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.svg'],
    "videos": ['.mp4', '.mkv', '.webm', '.flv', '.avi', '.mov', '.wmv'],
    "documents": ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    "compressed": ['.zip', '.rar', '.tar', '.gz', '.7z'],
    "music": ['.mp3', '.wav', '.ogg', '.m4a', '.flac', '.aac'],
    "executable": ['.exe', '.msi']
}

def move_file(file, folder):
    """
    Moves the file to the destination folder
    """
    shutil.move(file, folder)

def create_folder(folder):
    """
    Creates the destination folder if it doesn't exist
    """
    if not os.path.exists(folder):
        os.mkdir(folder)

def get_file_extension(file):
    """
    Returns the file extension
    """
    return os.path.splitext(file)[1]

def get_folder_name(file):
    """
    Returns the folder name based on the file extension
    """
    for key, value in extensions.items():
        for extension in value:
            if extension == get_file_extension(file):
                return key
    return "other"

def rearrange_files(path):
    """
    Rearranges the files in the given path
    """
    for file in os.listdir(path):
        folder_name = get_folder_name(file)
        folder_path = os.path.join(path, folder_name)
        create_folder(folder_path)
        file_path = os.path.join(path, file)
        move_file(file_path, folder_path)

#Ask for the path
path = input("Enter the path to rearrange: ")

#Check if the path exists
if not os.path.exists(path):
    print("The path doesn't exist!")
    exit()

#Check if the path is a directory
if not os.path.isdir(path):
    print("The path is not a directory!")
    exit()

#Rearrange the files
rearrange_files(path)
print("Files have been rearranged!")
