import os
import re

def walk_dir_extractFS(root):
    # rootDir = '..\\kernel'
    writing = False
    output = None

    for dirName, subdirList, fileList in os.walk(root):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            # print('\t%s' % fname)
            if re.match(r'.*[0-9]$', fname):
                with open(dirName+'\\'+fname, 'r', encoding='utf8') as input:
                    nol = 1
                    # print('reading ' + dirName+'\\'+fname + ' line ', nol)
                    line = input.readline()
                    
                    while line:
                        nol += 1
                        m = re.match(r'diff --git a/fs/(ext3|ext4|jfs|xfs|btrfs|reiser).*', line)
                        check = re.match(r'diff --git .*', line)
                        if check:
                            writing = False
                            if m:
                                writing = True
                            if output:
                                output.close()
                                output = None

                        if writing:
                            if not output:
                                if not os.path.exists(dirName+'\\'+m.groups()[0]):
                                    os.makedirs(dirName+'\\'+m.groups()[0])
                                output = open(dirName+'\\'+m.groups()[0]+'\\'+m.groups()[0]+'-patches.txt', 'a', encoding='utf8')
                                print('writing to ' + dirName+'\\'+m.groups()[0]+'\\'+m.groups()[0]+'-patches')
                            output.write(line+'\n')
                        
                        # print('reading ' + dirName+'\\'+fname + ' line ' , nol)
                        line = input.readline()
                    if output:
                        output.close()
                        output = None
                    nol = 0
            
# with open('D:\\Documents\\Temp\\patch-3.10.41-42', 'r', encoding='utf8') as f:
#     line = f.readline()
#     f2 = open('D:\\Documents\\Temp\\patch-3.10.41-42hahaha', 'a', encoding='utf8')
#     while(line):
#         f2.write(line+'\n')
#         line = f.readline()
#     f2.close()


walk_dir_extractFS('..\\kernel')