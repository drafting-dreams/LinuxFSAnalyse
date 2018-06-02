import gzip
import shutil
import os

def walk_dir(root):
    # rootDir = '..\\kernel'
    for dirName, subdirList, fileList in os.walk(root):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            unzip(dirName+'\\', fname)

def unzip(dir, file):
    with gzip.open(dir+file, 'rb') as f_in:
        with open(dir+file[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)