#!/usr/bin/env python
#coding:utf-8
#__time__: 2018/6/7 17:52
#__author__ = 'ren_mcc'

import sys
import codecs

def modify_config(config_file):
    idx = 0
    with codecs.open(config_file, 'rb+', 'utf8') as f:
        contents = f.readlines()
        f.seek(0, 0)
        for line in contents:
            #找出IsTestAPK在列表中的索引，取下一行索引
            if line.find('IsTestAPK') > 0:
                idx = contents.index(line)+1
                break
        #修改文件
        for line in contents:
            line_new = line.replace(contents[idx], "\t\treturn 1;\r\n")
            f.write(line_new)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("argument count error", "error")
    config_file = sys.argv[1]
    ceshi = sys.argv[2]
    if ceshi == 'true':
        modify_config(config_file)