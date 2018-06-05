import gzip
import shutil
import os
import re

#unzip all files in a dir
def walk_dir_unzip(root):
    # rootDir = '..\\kernel'
    for dirName, subdirList, fileList in os.walk(root):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            unzip(dirName+'\\', fname)

#unzip a file
def unzip(dir, file):
    with gzip.open(dir+file, 'rb') as f_in:
        with open(dir+file[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# delete a dir
def walk_dir_remove(root):
    # rootDir = '..\\kernel'
    for dirName, subdirList, fileList in os.walk(root):
        if not re.match(r'..\\kernel\\([a-z-.0-9]+)$', dirName) and dirName != '..\\kernel':
            shutil.rmtree(dirName)
            print('Deleted directory: %s' % dirName)
        
if __name__ == '__main__':
    walk_dir_remove('..\\kernel')
    # walk_dir_unzip('..\\kernel\\linux-4.0')
    # walk_dir_unzip('..\\kernel\\linux-4.1')
    # walk_dir_unzip('..\\kernel\\linux-4.2')
    # walk_dir_unzip('..\\kernel\\linux-4.3')
    # walk_dir_unzip('..\\kernel\\linux-4.4')
    # walk_dir_unzip('..\\kernel\\linux-4.5')
    # walk_dir_unzip('..\\kernel\\linux-4.6')
    # walk_dir_unzip('..\\kernel\\linux-4.7')
    # walk_dir_unzip('..\\kernel\\linux-4.8')
    # walk_dir_unzip('..\\kernel\\linux-4.9')
    # walk_dir_unzip('..\\kernel\\linux-4.10')
    # walk_dir_unzip('..\\kernel\\linux-4.11')
    # walk_dir_unzip('..\\kernel\\linux-4.12')
    # walk_dir_unzip('..\\kernel\\linux-4.13')
    # walk_dir_unzip('..\\kernel\\linux-4.14')
    # walk_dir_unzip('..\\kernel\\linux-4.15')
    # walk_dir_unzip('..\\kernel\\linux-4.16')