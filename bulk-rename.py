# script to rename multiple files

import os

def main():

    filepath = r'C:\Users\me\Music'

    # 'walk' down the directory structure
    for path, dirs, files in os.walk(filepath):
        for file in files:
            
            # replace all underscores with spaces
            if '_' in file:
                new_file = file.replace('_', ' ')
            else:
                new_file = file
            
            new_file = 'Stand Atlantic' + new_file[2:]
        
            os.rename(path + '\\' + file, path + '\\' + new_file)


if __name__ == '__main__':
    main()