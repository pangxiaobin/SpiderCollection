#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import execjs
import requests


def AESDecrypt_json(res):
    with open('./jscode.js', 'r') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('AESDecrypt', res)
    return result


def run():
    headers = {
        'authority': 'interface.bidcenter.com.cn',
        'accept': 'text/plain, */*; q=0.01',
        'accept-language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://search.bidcenter.com.cn',
        'referer': 'https://search.bidcenter.com.cn/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    data = {
        'from': '6137',
        'guid': '11fb79da-a854-434b-8ab0-eba6de41f625',
        'location': '6138',
        'token': '',
        'next_token': '',
        'keywords': '%E6%9C%8D%E5%8A%A1%E5%99%A8',
        'mod': '0',
    }

    response = requests.post('https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx', headers=headers,
                             data=data)

    print(AESDecrypt_json(response.text))


if __name__ == '__main__':
    run()
