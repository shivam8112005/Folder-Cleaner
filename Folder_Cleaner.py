import os
# shutil is library that allows us to move a files inside our computer's file system
import shutil


def clean_folder(folder_path):
    list_files=os.listdir(folder_path)
    print(f"in folder {folder_path} this are the files {list_files}")
    for filename in list_files:
        file_path=os.path.join(folder_path, filename)
        if(os.path.isfile(file_path)):
            print(file_path)





if __name__=="__main__":
    print('folder cleaner script')
    folder_path='C:/Users/Shivam/vscodeprojects/Python_projects/Folder_cleaner_Demo'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("cleaning complete.")
    else:
        print("Invalid Path of the Folder!")