#!/usr/bin/env python3.5
# coding=utf-8

import os
import sys

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
    sys = 'cd %s;gitbook build;mv _book  %s;cp -rf %s /Users/xiang/Workspace/github/luckxiang.github.io/gbook/%s;rm -rf %s'%(path,path,path,path,path)
    os.system(sys)
