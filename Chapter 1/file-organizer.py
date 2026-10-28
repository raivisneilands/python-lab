import os
import shutil

file_extensions = ['png', 'txt', 'mp3', 'mp4', 'mov', 'html', 'css', 'js', 'jpg', 'pdf', 'docx', 'pptx']

print('Enter a path which to organize: ', end='')
path=input()

if (not os.path.exists(path)):
    print('\nPath is not found. Please enter a valid path and try again.')

os.chdir(path)
print('Changed into - ', os.getcwd())

def move_file(file, destination):
    if (not os.path.exists(destination)):
        os.mkdir(destination)
    shutil.move(file, os.path.join(destination, file))

for file in os.listdir():
    if (os.path.isfile(file)):
        file_extension = file[file.rfind('.') + 1:]
        match file_extension:
            case 'png' | 'jpg':
                move_file(file, path + '/images')

            case 'txt' | 'pdf' | 'docx':
                move_file(file, path + '/documents')  

            case 'mp3' | 'mp4' | 'mov':
                move_file(file, path + '/media')

            case 'html' | 'css' | 'js':
                move_file(file, path + '/web-dev')

            case _:
                move_file(file, path + '/miscellaneous')
    else:
        print(f'{file} is a directory. Skipping it.')

            