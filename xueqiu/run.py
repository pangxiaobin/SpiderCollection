#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import execjs
import requests
import re

HEADERS = {
    'Host': 'xueqiu.com',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'elastic-apm-traceparent': '00-bf05d032897dc6d77dc6280f77a01733-2961fd43ce137e04-00',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Purpose': 'prefetch;prerender',
    'sec-ch-ua-platform': '"macOS"',
    'Purpose': 'prefetch',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://xueqiu.com/today',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
}


def get_cookie() -> dict:
    """
    获取acw__sc__v2 cookie
    :return: cookie
    """

    response = requests.get('https://xueqiu.com/today', headers=HEADERS)
    pattern = r"arg1='(.*?)';"
    match = re.search(pattern, response.text)

    if match:
        arg1 = match.group(1)
    else:
        raise ValueError('没有匹配到arg1的值')
    with open('./jscode.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    acw__sc_v2_cookie = execjs.compile(js_code).call('getAcwScV2Cooke', arg1)
    cookies = {}
    cookies['acw_sc__v2'] = acw__sc_v2_cookie
    response = requests.get('https://xueqiu.com/today', headers=HEADERS, cookies=cookies)
    cookies.update(response.cookies.get_dict())

    return cookies


def run():
    cookies = get_cookie()
    params = {
        'since_id': '-1',
        'max_id': '-1',
        'size': '15',
    }

    response = requests.get('https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=-1&size=15', params=params,
                            cookies=cookies, headers=HEADERS)
    print(response.json())


if __name__ == '__main__':
    run()
