import urllib.request, os
from utils import walk_dir_unzip
from spider import getAllFilesUrls

urls = getAllFilesUrls()
print(urls)

#download linux-kernel patch 2.6-4.16
for url in urls:
    file_name = url.split('/')[-1]
    directory_name = '..\\kernel\\linux-' + '.'.join(file_name[6:].split('.')[:2]) + '\\'
    local_file = directory_name + file_name

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    if not os.path.exists(local_file):
        local_filename, headers = urllib.request.urlretrieve(url, local_file)

    print(local_file)

walk_dir_unzip('..\\kernel')

