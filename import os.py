import os

files = os.listdir('c:/Users/ljohn/downloads')
file_info = []

# nested files print recursively
def print_files_recursively(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_info.append({
                'username': os.getlogin(),
                'file_path': file_path,
                'file_name': file,
                'file_type': os.path.splitext(file_path)[1],
                'file_date': os.path.getctime(file_path),
                'file_size': os.path.getsize(file_path),
            })


for entry in os.scandir('c:/Users/ljohn/downloads'):
    if entry.is_file():
        print(entry.path)
    elif entry.is_dir():
        print_files_recursively(entry.path)
    
    


 
 

    