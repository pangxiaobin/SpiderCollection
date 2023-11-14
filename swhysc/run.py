#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import base64

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def run():
    cookies = {
        'Hm_lvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c': '1699518481',
        'Hm_lpvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c': '1699518481',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218bb332025ad3d-03046cb892a59c2-16525634-1296000-18bb332025ba7b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiYjMzMjAyNWFkM2QtMDMwNDZjYjg5MmE1OWMyLTE2NTI1NjM0LTEyOTYwMDAtMThiYjMzMjAyNWJhN2IifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218bb332025ad3d-03046cb892a59c2-16525634-1296000-18bb332025ba7b%22%7D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c=1699518481; Hm_lpvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c=1699518481; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218bb332025ad3d-03046cb892a59c2-16525634-1296000-18bb332025ba7b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiYjMzMjAyNWFkM2QtMDMwNDZjYjg5MmE1OWMyLTE2NTI1NjM0LTEyOTYwMDAtMThiYjMzMjAyNWJhN2IifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218bb332025ad3d-03046cb892a59c2-16525634-1296000-18bb332025ba7b%22%7D',
        'Referer': 'https://www.swhysc.com/swhysc/financial/marginTradingList?channel=00010017000300020001&listId=2',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'secuCode': '',
        'market': '',
        'orderFlag': '',
        'pageNum': '2',
        'pageSize': '10',
    }

    response = requests.get(
        'https://www.swhysc.com/swhyscywbl/service/dsinfo/v1/margin/deposit/ratio',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(decrypt(response.text))


def decrypt(t):
    """
    aes 解密
    :param t:
    :return:
    """
    r = 'rewin-swhysc1234'
    key = r.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = base64.b64decode(t)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data.decode('utf-8')


if __name__ == '__main__':
    run()
