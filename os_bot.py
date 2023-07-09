import os
import shutil

PATH = '/Users/BLYER/Desktop'

def main(path: str):
    os.chdir(path)
    os.mkdir(path, 'new')
    shutil.make_archive('new_archive', 'zip', 'new')


if __name__ == '__main__':
    PATH = '/Users/BLYER/Desktop'
    print(main(PATH))

