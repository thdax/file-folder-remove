import os

def delete_folder_files(folder_path):
    try:
        file_count = 0
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                file_count += 1
                os.remove(file_path)
            elif os.path.isdir(file_path):
                file_count += 1
                delete_folder_files(file_path)
                os.rmdir(file_path)
        
        print(f'Total {file_count} file and folder deleted in {folder_path}.')
        
    except Exception as e:
        print(f'Error : {e}')

folder_path = "path//to//your//folder"

delete_folder_files(folder_path)
