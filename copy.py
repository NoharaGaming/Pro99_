import os
import shutil
print("os imported")
path = os.getcwd()
print(path)
# os.mkdir('C:\\Users\\souvik\\OneDrive\\Desktop\\c99\\test')
# source='C:\\Users\\souvik\\OneDrive\\Desktop\\c99\\text1.txt'
# destination = 'C:\\Users\\souvik\\OneDrive\\Desktop\\c99\\test\\file.txt'
source= input("Enter a path from where you want to copy file")
destination = input("Enter a path where you want to paste your file")
print (source)
dest = shutil.copy(source,destination)