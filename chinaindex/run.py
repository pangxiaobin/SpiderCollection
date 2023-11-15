#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import execjs
import requests


def aes_parse(data, lastFetchTime):
    with open("./jscode.js", encoding="utf-8") as f:
        js_code = f.read()
    cxt = execjs.compile(js_code)
    result = cxt.call("AESParse", data, lastFetchTime)
    return result


def run():
    cookies = {
        "mobile_iindex_uuid": "b0f83dd7-1e64-51d4-8dad-be25ffaccf3d",
        "Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f": "1700036352",
        "Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f": "1700036352",
    }

    headers = {
        "authority": "www.chinaindex.net",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
        # 'cookie': 'mobile_iindex_uuid=b0f83dd7-1e64-51d4-8dad-be25ffaccf3d; Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f=1700036352; Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f=1700036352',
        "funcid": "undefined",
        "incognitomode": "0",
        "referer": "https://www.chinaindex.net/ranklist/680",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "uuid": "b0f83dd7-1e64-51d4-8dad-be25ffaccf3d",
    }

    params = {
        "channel": "varietylist",
        "sign": "6fb5ce5dd1fb90ed46df7b71cef028e3",  # 这里的sign是根据channel进行加密生成的 固定
    }

    response = requests.get(
        "https://www.chinaindex.net/iIndexMobileServer/mobile/entertainment/objectFansRank",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.json())
    result = aes_parse(response.json()["data"], response.json()["lastFetchTime"])
    print(result)


if __name__ == "__main__":
    run()
