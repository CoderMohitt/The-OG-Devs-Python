# import OS module
import os
# Get the list of all files and directories
path = r"C:\Users\deepa\OneDrive\Desktop\Batch 1 Python"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)
