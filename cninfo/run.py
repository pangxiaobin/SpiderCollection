#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py

import requests
import execjs


def get_accept_enckey():
    with open('./jscode.js', 'r') as f:
        js_code = f.read()
    return execjs.compile(js_code).call('getResCode')

def run():


    cookies = {
        'routeId': '.uc1',
        'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1699512068',
        'MALLSSID': '3562362F436A55523130657178344F5A664C6C4577414C51682B4B305934307243477076554B41786F4138496541304839734B4B68305676475A6A367476434D',
        'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1699512170',
        'JSESSIONID': '34247136F3D45AC6A578E952FC12B490',
    }

    headers = {
        'Accept': '*/*',
        'Accept-EncKey': get_accept_enckey(),
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'routeId=.uc1; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1699512068; MALLSSID=3562362F436A55523130657178344F5A664C6C4577414C51682B4B305934307243477076554B41786F4138496541304839734B4B68305676475A6A367476434D; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1699512170; JSESSIONID=34247136F3D45AC6A578E952FC12B490',
        'Origin': 'https://webapi.cninfo.com.cn',
        'Referer': 'https://webapi.cninfo.com.cn/',
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
        'tdate': '2023-11-08',
        'market': 'SZE',
    }

    response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007', cookies=cookies, headers=headers,
                             data=data)
    print(response.json())


if __name__ == '__main__':
    run()