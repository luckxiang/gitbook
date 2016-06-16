#!/usr/bin/env python3.5
# coding=utf-8

import os 
import sys
from bs4 import BeautifulSoup

gbookpath = '/Users/xiang/Workspace/github/luckxiang.github.io/gbook'

def replace_tags(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                filename = os.path.join(root, file)
                fp = open(filename)
                soup = BeautifulSoup(fp, 'lxml')
                fp.close()
                tags = soup.find_all(href='https://www.gitbook.com')
                for tag in tags:
                    tag['class'] = 'homepage-back'
                    tag['target'] = '_self'
                    tag['href'] = 'http://www.bigxiangbaobao.com/book/'
                    tag.string = '\n                        Back to Book'
                fp = open(filename, 'w')
                fp.write(str(soup))
                fp.close()

os.system('cp -rf /Users/xiang/GitBook/Library/Import/ ./')
os.system('find . -name  ".git"  -mindepth 2|xargs rm -rf')
os.system('git add .')
os.system('git commit -m "add"')
os.system('git push origin master')

if len(sys.argv) < 2:
    paths = os.popen('ls -F |grep "/"').readlines()
else:
    paths = sys.argv
    paths.pop(0)

for path in paths:
    path = path.strip('\n')
    print(path)
 #   sys = 'cd %s;gitbook build;mv _book  %s;cp -rf %s /Users/xiang/Workspace/github/luckxiang.github.io/gbook/%s;rm -rf %s'%(path,path,path,path,path)
  #  os.system(sys)

#replace_tags(os.path.abspath(gbookpath))




