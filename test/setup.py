#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午7:23
# @Author  : zhaoyu
# @Site    : 
# @File    : setup.py
# @Software: PyCharm

# Automatically created by: scrapydweb x scrapyd-client

from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = test_spider.settings']},
)