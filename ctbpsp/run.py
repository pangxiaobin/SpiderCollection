#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import execjs
import requests


def des_decrypt(data):
    """
    des 解密
    :param data:
    :return:
    """
    with open('./jscode.js', 'r') as f:
        js_code = f.read()
    return execjs.compile(js_code).call('DESDecrypt', data)


def run():
    cookies = {
        'yP4dbuxzYtffO': '60vANnjI9GW1BKec1T_i6PwouMUlfs1iC1C6lDW87UL8l6vBFdWbXLyjbCMWDiRIvPYbk9d9SmWpYrJqYgxZceLG',
        'route': 'ef535e3a0d0b78922cdc0df3d6b94403',
        'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1699803946,1700116132',
        'BSFIT_EXPIRATION': '1700171918384',
        'BSFIT_DEVICEID': 'V8MBnE2oid-nZD8FIVLL9FMGDRtVoh0rJrVzWxeTS9v6wvq1a9buvSaqLbiRa4LvS1tCNKvOt9mTt-HO1lo-orQgudFYItjZ9yE7UEFWxvwEOWZnHQNfywd8Cnl7z9mai5_xPlaqwgAbQ1YwPXiuO9BwFbEDDyFC',
        'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1700124549',
        '__ts': '1700124550001',
        'BSFIT_rgt3l': 'JShwJ3lex3vRz3MVxQ,J3lex3JwJSsRzB,J3lNJOvwJSlVxr,J3lRJLQwJSswxQ,J3r1JLvwJSvwzB',
        'yP4dbuxzYtffP': '0pTsL9q1bs2DESiDYeYL8ZpI4_BVTkyogV1qV8L57cUwUW5cHlJHT7xwNITusmByskKvyEz3FqvmRp5SivetYTvhTg67eVDx_kMytisBV3Pv2Xju88FntDJ7JR_b7TX9y0kmMQr381JiIP_1.EGb2Ycxy9QD19fHNBmUJW1niFyQu8hNFPh1wAVSXgZSkBlHEupWXs06cvFVogLF.SfkIQ1aRSz2N266Ntw4duogVzOECW1mwYFCjpD4Y.c2NkHmwJ8OEWl.ZY8LDyZh555P3MWx8ODnz7rSWFgpvCQ7xxekclyYlsevvW12DvxeTReJqn1obealpCXsXGSEAj4lXSam8fkIF4Kp6QquPJ5FbV5UZLLZ_xLaBMNyXWHIeRYbPZMAnGAUi3327V_vhrywut1ZhuB_A9qoH2WT25uMcltL',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'yP4dbuxzYtffO=60vANnjI9GW1BKec1T_i6PwouMUlfs1iC1C6lDW87UL8l6vBFdWbXLyjbCMWDiRIvPYbk9d9SmWpYrJqYgxZceLG; route=ef535e3a0d0b78922cdc0df3d6b94403; Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1699803946,1700116132; BSFIT_EXPIRATION=1700171918384; BSFIT_DEVICEID=V8MBnE2oid-nZD8FIVLL9FMGDRtVoh0rJrVzWxeTS9v6wvq1a9buvSaqLbiRa4LvS1tCNKvOt9mTt-HO1lo-orQgudFYItjZ9yE7UEFWxvwEOWZnHQNfywd8Cnl7z9mai5_xPlaqwgAbQ1YwPXiuO9BwFbEDDyFC; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1700124549; __ts=1700124550001; BSFIT_rgt3l=JShwJ3lex3vRz3MVxQ,J3lex3JwJSsRzB,J3lNJOvwJSlVxr,J3lRJLQwJSswxQ,J3r1JLvwJSvwzB; yP4dbuxzYtffP=0pTsL9q1bs2DESiDYeYL8ZpI4_BVTkyogV1qV8L57cUwUW5cHlJHT7xwNITusmByskKvyEz3FqvmRp5SivetYTvhTg67eVDx_kMytisBV3Pv2Xju88FntDJ7JR_b7TX9y0kmMQr381JiIP_1.EGb2Ycxy9QD19fHNBmUJW1niFyQu8hNFPh1wAVSXgZSkBlHEupWXs06cvFVogLF.SfkIQ1aRSz2N266Ntw4duogVzOECW1mwYFCjpD4Y.c2NkHmwJ8OEWl.ZY8LDyZh555P3MWx8ODnz7rSWFgpvCQ7xxekclyYlsevvW12DvxeTReJqn1obealpCXsXGSEAj4lXSam8fkIF4Kp6QquPJ5FbV5UZLLZ_xLaBMNyXWHIeRYbPZMAnGAUi3327V_vhrywut1ZhuB_A9qoH2WT25uMcltL',
        'Pragma': 'no-cache',
        'Referer': 'https://ctbpsp.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'oArpptFq': '0Ms3ssGlqEkTYi9cGPihytpy1Mi7auLLE8Y3gM0tlvc7hzVoXB9cOEJ3V8c34CVl6_dVni35lXYDG_bM9IICaxj6twvHOzJdH',
    }

    response = requests.get(
        'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    print(response.status_code)
    print(response.text)
    print(des_decrypt(response.json()))


if __name__ == '__main__':
    run()
