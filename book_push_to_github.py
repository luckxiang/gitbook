#!/usr/bin/env python3.5
# coding=utf-8

import os

os.system('cp -rf /Users/xiang/GitBook/Library/Import/ ./ ')
os.system('find . -name  ".git"  -mindepth 2|xargs rm -rf ')
os.system('git add . ')
os.system('git commit -m "add" ')
os.system('git push origin master')
