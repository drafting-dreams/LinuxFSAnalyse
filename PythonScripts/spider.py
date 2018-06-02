from bs4 import BeautifulSoup
import urllib.request
import re
urls = ['https://mirrors.edge.kernel.org/pub/linux/kernel/v2.6/incr/',
'https://mirrors.edge.kernel.org/pub/linux/kernel/v3.x/incr/',
'https://mirrors.edge.kernel.org/pub/linux/kernel/v4.x/incr/'
]

files = []


def getAllFilesUrls():
    for url in urls:
        html = ''
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html)
        for link in soup.findAll('a'):
            # print(link.get('href'))
            m = re.match(r'patch-([0-9])\.([0-9]+).*(gz)$', link.get('href'))
            if m :
                if m.groups()[0]=='4' and m.groups()[1]>'16':
                    continue
                files.append(url+link.get('href'))

    return files

getAllFilesUrls()
#print(files)