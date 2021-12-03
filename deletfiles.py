import os
import shutil
import time
def main():
    day = 30
    seconds = time.time()-(day*24*60*60)
    path = 'C:\\Users\\souvik\\OneDrive\\Desktop\\c99\\test'
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds>=folderAge(root_folder):
                removeFolder (root_folder)

def folderAge(path):
    ctime=os.stat(path).st_ctime
    return ctime
def removeFolder(path):
    os.remove(path)
main()