from bs4 import BeautifulSoup
import urllib.request
import threading
import re
urls = ['https://mirrors.edge.kernel.org/pub/linux/kernel/v2.6/incr/',
'https://mirrors.edge.kernel.org/pub/linux/kernel/v3.x/incr/',
'https://mirrors.edge.kernel.org/pub/linux/kernel/v4.x/incr/'
]

versions = ['v2.6.39.4', 'v3.0.101', 'v3.1.10', 'v3.2.102', 'v3.3.8', 'v3.4.113', 'v3.5.7', 'v3.6.11', 'v3.7.10', 
'v3.8.13', 'v3.9.11', 'v3.10.108', 'v3.11.10', 'v3.12.74', 'v3.13.11', 'v3.14.79', 'v3.15.10', 'v3.16.56', 'v3.17.8',
'v3.18.112', 'v3.19.8', 'v4.0.9', 'v4.1.52', 'v4.2.8', 'v4.3.6', 'v4.4.135', 'v4.5.7', 'v4.6.7', 'v4.7.10', 'v4.8.17', 
'v4.9.105', 'v4.10.17', 'v4.11.12', 'v4.12.14', 'v4.13.16', 'v4.14.47', 'v4.15.18', 'v4.16.13']
# tempversions = ['v4.3.6', 'v4.4.135', 'v4.5.7', 'v4.6.7', 'v4.7.10', 'v4.8.17', 'v4.9.105', 'v4.10.17', 'v4.11.12', 'v4.12.14', 'v4.13.16', 'v4.14.47', 'v4.15.18', 'v4.16.13']

fss = ['ext3', 'ext4', 'xfs', 'jfs', 'btrfs', 'reiserfs']

def getHtmlSoupFromUrl(url):
    html = ''
    n = 0
    while not html:
        try:
            n += 1
            with urllib.request.urlopen(url) as response:
                html = response.read()
                n = 0
        except:
            if n <= 3:
                pass
            else:
                raise Exception('Connect failed!!!!!!!')

    soup = BeautifulSoup(html)

    return soup


# find all patches' url
def getAllFilesUrls():
    files = []
    for url in urls:
        soup = getHtmlSoupFromUrl(url)
        for link in soup.findAll('a'):
            # print(link.get('href'))
            m = re.match(r'patch-([0-9])\.([0-9]+).*(gz)$', link.get('href'))
            if m :
                files.append(url+link.get('href'))

    return files

# find all fs file's url
def getAllFSFilesUrls():
    files = {}
    for version in versions:
        files[version] = []
        for fs in fss:
            url = 'https://elixir.bootlin.com/linux/' + version + '/source/fs/' + fs
            soup = getHtmlSoupFromUrl(url)
            for link in soup.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['tree-icon', 'icon-blob']):
                files[version].append('https://elixir.bootlin.com/linux/' + link.get('href'))
                print('add link '+ 'https://elixir.bootlin.com/linux/' + link.get('href'))

    return files

# get LOC from file and write the loc info into local_files
def getLOCFromFiles(urls):
    for url in urls:
        soup = getHtmlSoupFromUrl(url)
    # url = 'https://elixir.bootlin.com/linux/v3.19.8/source/fs/ext3/balloc.c'
    # soup = getHtmlSoupFromUrl(url)

        m = re.match(r'https:\/\/elixir.bootlin.com\/linux\/v([0-9]\.[0-9]+)[0-9.]+\/source\/fs\/([0-9a-z]+)\/([0-9a-zA-Z_\-.]+)$', url)
        group = m.groups()
                
        with open('..//kernel//linux-' + group[0] + '//file_size.txt', 'a', encoding='utf8') as f:
            f.write(group[1] + '/' + group[2] + ' has ' + list(soup.find('pre').children)[-1].contents[0] + ' LOC\n')
            print('writing to ' + '..//kernel//linux-' + group[0] + '//file_size.txt')

def multiThreadGetLOCFromFiles(urlDic):
    thread_list = []
    for key, value in urlDic.items():
        t = threading.Thread(target=getLOCFromFiles, args=(value,))
        thread_list.append(t)
    print(thread_list)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()



if __name__ =='__main__':
    multiThreadGetLOCFromFiles(getAllFSFilesUrls())