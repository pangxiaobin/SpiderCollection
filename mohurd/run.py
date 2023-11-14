#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import json

import requests
import execjs


def decrypt_result(result):
    with open('jscode.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code).call('get_decrypt_data', result)
    return ctx


def run():
    cookies = {
        'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1699870954,1699924732',
        'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1699924732',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1699870954,1699924732; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1699924732',
        'Pragma': 'no-cache',
        'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLWJd6/53c2B2tyT2ZdEJenRhpUUKvcMtoMqfGfwdLCb8g==',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'timeout': '30000',
        'v': '231012',
    }

    params = {
        'pg': '1',
        'pgsz': '15',
        'total': '450',
    }

    response = requests.get(
        'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    # print(decrypt_result(response.text))
    for i in json.loads(decrypt_result(response.text))['data']['list']:
        print(i)


if __name__ == '__main__':
    run()
