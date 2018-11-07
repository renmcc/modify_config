#!/usr/bin/env python
#coding:utf-8
#__time__: 2018/6/7 17:10
#__author__ = 'ren_mcc'

import os
import io
import sys
import codecs

def modify_config(config_file):
    idx = 0
    with codecs.open(config_file, 'rb+', 'utf-8') as f:
        contents = f.readlines()
        f.seek(0,0)
        for line in contents:
            if line.find('LuaBundleMode') > 0:
                idx = contents.index(line)
                break
    with codecs.open(config_file, 'wb', 'utf-8') as f:
        old_string = contents[idx]
        new_string = "        public const bool LuaBundleMode = true;                    //Lua代码AssetBundle模式\n"
        for line in contents:

            line_new = line.replace(old_string, new_string)
            f.write(line_new)
            print(line_new)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("argument count error", "error")
    config_file = sys.argv[1]
    LuaBundleMode = sys.argv[2]

    if LuaBundleMode == 'true':
        # 因为windows的print方法默认是gbk编码，所以需要修改
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
        modify_config(config_file)
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')