#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import requests
import execjs


def get_request_body(data):
    with open('./jscode.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    res = execjs.compile(js_code).call('getRequestData', data)
    return bytes(res['data'])


def run():
    cookies = {
        'JSESSIONID': '7E286A008B6A52DF0C0239409123FFA2',
        'Hm_lvt_6146f11e5afab71309b3accbfc4a932e': '1699435609',
        'Hm_lpvt_6146f11e5afab71309b3accbfc4a932e': '1699504996',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Content-Type': 'application/octet-stream',
        'Origin': 'http://www.spolicy.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.spolicy.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    data = {
        "policyType": "6",
        "province": "",
        "city": "",
        "downtown": "",
        "garden": "",
        "centralId": "",
        "sort": 0,
        "homePageFlag": 1,
        "pageNum": 1,
        "pageSize": 7
    }
    data = get_request_body(data)
    url = 'http://www.spolicy.com/info_api/policyType/showPolicyType'
    response = requests.post(url, cookies=cookies,
                             headers=headers, data=data, verify=False)
    print(response.json())


if __name__ == '__main__':
    run()
