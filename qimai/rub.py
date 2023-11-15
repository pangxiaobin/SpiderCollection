#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : rub.py
import execjs
import requests


def get_analysis(params, url_path):
    """
    获取 analysis
    :param params: {"brand": "all",
                    "device": "iphone",
                    "country": "cn",
                    "genre": "6014",
                    "date": "2023-11-15",
                    "page": "2",
                }
    :param url_path:
    :return:
    """
    with open("./jscode.js") as f:
        js_code = f.read()
    cxt = execjs.compile(js_code)
    analysis = cxt.call(
        "getAnalysis", params, url_path.replace("https://api.qimai.cn", "")
    )
    return analysis


def run():
    headers = {
        "authority": "api.qimai.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
        # 'cookie': 'qm_check=A1sdRUIQChtxen8pI0dAPxYVUltXHBlmQVQOBwlISVdJGwcSGGpHXV4RNQ8JHBwIFXNXRlBTURhNNRIKAhwIWh4SGAlIBAhVViRYPDxTHBsSY05ZUkw2DgYMHQtaUUVbRlxCHRpJRAQAHRoRFw0QABUAGAhJVktYWgQ%3D; gr_user_id=ea54bc28-26df-4b0e-b185-8536a26846c7; PHPSESSID=62nhh3s2u0ttvir7t6ngr21nqj; synct=1700028214.165; syncd=-584; tgw_l7_route=29ef178f2e0a875a4327cbfe5fbcff7e; ada35577182650f1_gr_session_id=6ff9d12d-909a-4023-a6f9-c888e8a23aab; ada35577182650f1_gr_session_id_sent_vst=6ff9d12d-909a-4023-a6f9-c888e8a23aab',
        "origin": "https://www.qimai.cn",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    params = {
        "brand": "all",
        "device": "iphone",
        "country": "cn",
        "genre": "6014",
        "date": "2023-11-15",
        "page": "2",
    }
    url = "https://api.qimai.cn/rank/indexPlus/brand_id/1"
    analysis = get_analysis(params, url)
    print(analysis)
    params["analysis"] = analysis
    response = requests.get(
        url,
        params=params,
        headers=headers,
    )
    for i in response.json()["list"]:
        print(i)


if __name__ == "__main__":
    run()
