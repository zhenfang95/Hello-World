#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/26 16:50

import os
def get_cwd():
    '''跟目录路径'''
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path