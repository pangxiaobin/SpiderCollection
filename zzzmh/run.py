#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import json
import os
from urllib.parse import urlparse

import execjs
import requests


def parse_result(res):
    """
    解密结果
    :param res:
    :return:
    """
    with open("jscode.js", encoding="utf-8") as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    result = ctx.call("_0x563330", res)
    return result


def download_img(param_key):
    """
    下载图片
    :param param_key:
    :return:
    """
    headers = {
        'authority': 'api.zzzmh.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://bz.zzzmh.cn/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    url = f'https://api.zzzmh.cn/bz/v3/getUrl/{param_key}'
    parsed = urlparse(url)
    file_name = os.path.basename(parsed.path)
    response = requests.get(url, headers=headers)
    with open(f"{file_name}.jpg", "wb") as file:
        file.write(response.content)


def run():
    headers = {
        "authority": "api.zzzmh.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://bz.zzzmh.cn",
        "referer": "https://bz.zzzmh.cn/",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    json_data = {
        "size": 24,
        "current": 1,
        "sort": 0,
        "category": 0,
        "resolution": 0,
        "color": 0,
        "categoryId": 0,
        "ratio": 0,
    }

    response = requests.post(
        "https://api.zzzmh.cn/bz/v3/getData", headers=headers, json=json_data
    )
    for i in json.loads(parse_result(response.json()["result"]))['list']:
        param_key = f"{i['i']}{i['t']}9"
        print(f'download img:{param_key}')
        download_img(param_key)


if __name__ == "__main__":
    run()
