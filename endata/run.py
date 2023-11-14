#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import json

import execjs
import requests


def parse_result(result):
    with open('./jscode.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    result = ctx.call('webInstace.shell', result)
    return result


def run():
    cookies = {
        'MEIQIA_TRACK_ID': '2Y71ehAspL2WJYdEOkM4bCwX34s',
        'MEIQIA_VISIT_ID': '2Y71ekVndN93NWAFHtHltaRkaBd',
        'gr_user_id': 'e2fb1ff1-0a5e-4969-b974-0d0e365c508c',
    }

    headers = {
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'MEIQIA_TRACK_ID=2Y71ehAspL2WJYdEOkM4bCwX34s; MEIQIA_VISIT_ID=2Y71ekVndN93NWAFHtHltaRkaBd; gr_user_id=e2fb1ff1-0a5e-4969-b974-0d0e365c508c',
        'Origin': 'https://www.endata.com.cn',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    data = {
        'year': '2023',
        'MethodName': 'BoxOffice_GetYearInfoData',
    }

    response = requests.post('https://www.endata.com.cn/API/GetData.ashx', cookies=cookies, headers=headers, data=data)
    res = parse_result(response.text)
    for i in json.loads(res)['Data']['Table']:
        print(i)


if __name__ == '__main__':
    run()
