import os

directory_path = 'YOUR_PATH'

contents = os.listdir(directory_path)

for item in contents:
    print(item)