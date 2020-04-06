#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:57:51 2020

@author: ginger
@email:  gingerxjiang@gmail.com

Python中创建包: 在当前目录建立一个文件夹,
文件夹中包含一个__init__.py文件和若干个模块文件.
其中__init__.py可以是一个空文件, 建议将包中所有需要导出的变量放到__all__中,
这样可以确保包的接口清晰明了, 易于使用.

"""


# __all__ = ['add_method',  'functions', 'hello_gen', 'gen_random']
__all__ = ["add_method", "functions", "hello_gen", "gen_random"]

