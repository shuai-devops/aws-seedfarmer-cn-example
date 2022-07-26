#!/usr/bin/python
# -*- coding: utf-8 -*-
# version: beta

import os
import re
import logging
import site
# import aws_codeseeder as cs
# import seedfarmer as sf


def replace_file_str(location, t_str,r_str):
    """打开文件并替换字符串

    Args:
        location (str): 文件路径
        t_str (str): 匹配正则
        r_str (str): 替代字符
    """    
    fin = open(location, "rt")
    data = fin.read()
    # data = data.replace(t_str, r_str)
    if re.search(t_str, data):
        data = re.sub(t_str, r_str, data)
        logging.warning("file located in:%s has been replaced with:%s" % (location,r_str))
        # print("file located in:%s has been replaced with:%s" % (location,r_str))
    fin.close()
    fin = open(location, "wt")
    fin.write(data)
    fin.close()

# get all filename paths from the directory


    


def get_file_paths(base_path, ext, target_reg,replace_str):
    
    """扫描整个文件夹

    Args:
        ext (list): 需要扫描的文件后缀名
        target_reg (str): 目标正则
        replace_str (str): 替换字符
    """
    for root, dirs, files in os.walk(base_path):
        for filename in files:
            if  filename.endswith(tuple(ext)) and filename !="replace_file_str.py": # 扫描该文件所在路径下的所有文件（包括子目录），但不包括自己
                fpath = (os.path.abspath(os.path.join(root, filename)))
                replace_file_str(fpath,target_reg,replace_str)



ext = [".py", ".yaml", ".yml", ".json"] # 扫描指定后缀名
target_reg = "arn:aws(?!-cn)" # 正则测试推荐工具：https://regex101.com/
replace_str = "arn:aws-cn"

cs_base_path = "aws_codeseeder" 
sf_base_path = "seedfarmer" 
# base_py_site_path = site.USER_SITE

base_py_site_path = site.getsitepackages()[0] # 不同环境sitepackage的位置不一样，未来需要把[]遍历一般。
cs_path = os.path.join(base_py_site_path, cs_base_path)
sf_path = os.path.join(base_py_site_path, sf_base_path)


get_file_paths(cs_path, ext,target_reg,replace_str)
get_file_paths(sf_path, ext,target_reg,replace_str)

