#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午6:49
# @Author  : zhaoyu
# @Site    : 
# @File    : ip_pool.py
# @Software: PyCharm

import requests
import json
import logging as logger

MSG_OK = 'OK'


def get_request(url, params=None):
    """
    get 请求
    :param url: 请求地址
    :param params: get参数
    :return: 字典
    """

    logger.info('get 请求：{}'.format(url))
    resp = requests.get(url, params=params)
    if resp is not None and len(resp.text) > 300:
        logger.info('get 请求返回：{}'.format(resp.text[:300]))
    else:
        logger.info('get 请求返回：{}'.format(resp.text))
    result = json.loads(resp.content)

    return result


def post_request(url, request):
    """
    post 请求
    :param url: 请求地址
    :param request: 请求对象 dict
    :return:
    """

    logger.info('post 请求：{} {}'.format(url, request))
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url, data=json.dumps(request, ensure_ascii=False).encode('utf-8'), headers=headers)
    if resp is not None and len(resp.text) > 300:
        logger.info('post 请求返回：{}'.format(resp.text[:300]))
    else:
        logger.info('post 请求返回：{}'.format(resp.text))
    result = json.loads(resp.content)

    return result


def get_kdl_ip():
    """
    获取快代理的ip列表
    :return:
    """
    # 快代理获取ip的api
    proxy_url = 'http://dps.kdlapi.com/api/getdps/?orderid=947372684422252&num=1&pt=1&format=json&sep=1'

    result = ''
    msg = MSG_OK
    try:
        resp_data = get_request(proxy_url)
        if resp_data.get('code', -1) != 0:
            msg = resp_data.get('msg', '快代理没有返回错误信息！')
            return result, msg
        data = resp_data.get('data', None)
        if data is None:
            msg = '快代理返回数据data为None'
            return result, msg
        result = data.get('proxy_list', [])[0]
    except Exception as e:
        msg = str(repr(e))
    return result, msg


if __name__ == '__main__':
    x = get_kdl_ip()
    print(x)


