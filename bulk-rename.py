# script to rename multiple files

import os

def main():

    filepath = r'C:\Users\me\Music'

    # 'walk' down the directory structure
    for path, dirs, files in os.walk(filepath):
        for file in files:
            new_file = 'Coldplay -' + file[2:]
        
            os.rename(path + '\\' + file, path + '\\' + new_file)

if __name__ == '__main__':
    main()
