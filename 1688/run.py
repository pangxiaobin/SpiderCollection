#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import json
import re
import time
import execjs

import requests


def get_sign(data, timesmap):
    with open('./jscode.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    sign = ctx.call('getSign', data, timesmap)
    return sign


def run():
    cookies = {
        # 'cookie2': '1afde69868faa4b9248d364cbf8c59a9',
        # 't': '0ca4a186e14c7ffb71d8d39b5790f0a3',
        # '_tb_token_': 'ebe3e7ee3ae55',
        # '__cn_logon__': 'false',
        '_m_h5_tk': '92787c3d2a2cb937574f45f6ffaafa11_1699945776200',
        '_m_h5_tk_enc': '2c9836edc49e9055f81084c3a1f75683',
        # 'cna': '2Y6WHenDFQ0BASQIiVZJhdWb',
        # 'xlly_s': '1',
        # 'keywordsHistory': '%E4%BC%91%E9%97%B2%E5%A5%97%E8%A3%85%E5%A5%B3%E8%A3%85',
        # 'ali_ab': '223.71.127.50.1699938603740.6',
        # 'tfstk': 'dbpkYBvXMZa11c_k14BSU-keBFlYNz6C5eedJ9QEgZ7be0TKVIXVjgzFT46JKEYM-Lede6HeoUTfwQKepMJHlT5BwwQR-9xBSm3tBAKWV96rWVHTFFy1LSnxO5zTh36CLVEYLfHMVFdIDGSacX0vGb9xZ6QgAyqVayD3kwKPoRx6ngoV-A_bL_pA4_vEfaBajSPa38yC0Dp4OW1PcibtXA8ph',
        # 'l': 'fBEhXQQlPi93foAvBO5aourza77tNQRbzsPzaNbMiIEGC6bds4JecqxQV45LspxRRJXPiUYB4zPR06vt7euTJPYboi7PuNdoS88BIe8IK7Nk_',
        # 'isg': 'BKKiHsEjM66J1S9yHbtSDAml8y4E86YNU8ULXew5a5Qsv0A51IIzHfZ57_NDrx6l',
    }

    headers = {
        'authority': 'h5api.m.1688.com',
        'accept': '*/*',
        'accept-language': 'zh,en;q=0.9,zh-CN;q=0.8',
        # 'cookie': 'cookie2=1afde69868faa4b9248d364cbf8c59a9; t=0ca4a186e14c7ffb71d8d39b5790f0a3; _tb_token_=ebe3e7ee3ae55; __cn_logon__=false; _m_h5_tk=92787c3d2a2cb937574f45f6ffaafa11_1699945776200; _m_h5_tk_enc=2c9836edc49e9055f81084c3a1f75683; cna=2Y6WHenDFQ0BASQIiVZJhdWb; xlly_s=1; keywordsHistory=%E4%BC%91%E9%97%B2%E5%A5%97%E8%A3%85%E5%A5%B3%E8%A3%85; ali_ab=223.71.127.50.1699938603740.6; tfstk=dbpkYBvXMZa11c_k14BSU-keBFlYNz6C5eedJ9QEgZ7be0TKVIXVjgzFT46JKEYM-Lede6HeoUTfwQKepMJHlT5BwwQR-9xBSm3tBAKWV96rWVHTFFy1LSnxO5zTh36CLVEYLfHMVFdIDGSacX0vGb9xZ6QgAyqVayD3kwKPoRx6ngoV-A_bL_pA4_vEfaBajSPa38yC0Dp4OW1PcibtXA8ph; l=fBEhXQQlPi93foAvBO5aourza77tNQRbzsPzaNbMiIEGC6bds4JecqxQV45LspxRRJXPiUYB4zPR06vt7euTJPYboi7PuNdoS88BIe8IK7Nk_; isg=BKKiHsEjM66J1S9yHbtSDAml8y4E86YNU8ULXew5a5Qsv0A51IIzHfZ57_NDrx6l',
        'referer': 'https://sale.1688.com/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    data = {"fcGroup": "cbu-seller-fc", "fcName": "factory-recommend-service-fn",
            "serviceName": "tpFacRecommendService",
            "params": "{\"pageNo\":\"%d\",\"query\":\"\",\"pageSize\":\"20\",\"from\":\"P"
                      "C\",\"showType\":\"transverse\",\"trafficSource\":\"pc_index_recommend\",\"so"
                      "rt\":\"mix\",\"params\":{\"pageNo\":\"%d\",\"query\":\"\",\"pageSize\":\"20\",\"from"
                      "\":\"PC\",\"showType\":\"transverse\",\"trafficSource\":\"pc_index_recommend"
                      "\",\"sort\":\"mix\"}}" % (3, 3)}

    timesmap = int(time.time() * 1000)

    sign = get_sign(json.dumps(data), timesmap)
    print(sign)

    params = {
        'jsv': '2.6.1',
        'appKey': '12574478',
        't': timesmap,
        'sign': sign,
        'v': '2.0',
        'type': 'jsonp',
        'isSec': '0',
        'timeout': '5000',
        'api': 'mtop.mbox.fc.common.gateway',
        'jsonpIncPrefix': 'mboxfc',
        'dataType': 'jsonp',
        'callback': 'mtopjsonpmboxfc18',
        'data': json.dumps(data)
    }

    response_cookie = requests.get(
        'https://h5api.m.1688.com/h5/mtop.mbox.fc.common.gateway/2.0/',
        params=params,
        cookies=cookies,
        headers=headers,
    ).cookies.get_dict()
    cookies.update(response_cookie)

    response = requests.get(
        'https://h5api.m.1688.com/h5/mtop.mbox.fc.common.gateway/2.0/',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    callback_result = re.search(r'mtopjsonpmboxfc18\((.*)\)', response.text).group(1)

    for i in json.loads(callback_result)['data']['result']['result']['facList']:
        print(json.dumps(i))


if __name__ == '__main__':
    run()
