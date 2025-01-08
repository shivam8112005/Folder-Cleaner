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
            file_extension=filename.split('.')[-1]
            if file_extension:
                sub_folder=f"{file_extension.upper()} Files"
                sub_folder_path=create_subfolder_if_needed(folder_path, sub_folder)
                new_file_path=os.path.join(sub_folder_path,filename)
                if not os.path.exists(new_file_path):
                     shutil.move(file_path,sub_folder_path)
                     print(f"Moved {filename} -> {sub_folder}")
                else:
                    print(f"New file path already exists {new_file_path}")

               


def create_subfolder_if_needed(folder_path, sub_folder):
    sub_folder_path=os.path.join(folder_path,sub_folder)
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    return sub_folder_path







if __name__=="__main__":
    print('folder cleaner script')
    folder_path='C:/Users/Shivam/vscodeprojects/Python_projects/Folder_cleaner_Demo'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("cleaning complete.")
    else:
        print("Invalid Path of the Folder!")