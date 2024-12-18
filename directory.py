import os

files = os.listdir('c:/Users/ljohn/downloads')
file_info = []


for file in files:
    file_path = os.path.join('c:/Users/ljohn/downloads', file)
    file_info.append({
        'username': os.getlogin(),
        'file_path': file_path,
        'file_name': file,
        'file_type': os.path.splitext(file_path)[1],
        'file_date': os.path.getctime(file_path),
        'file_size': os.path.getsize(file_path),
        
        
    })

for i, file in enumerate(file_info):
    print(f'file_info {i+1}: {file}')
