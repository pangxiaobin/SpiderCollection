#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import json

import requests
import execjs


def get_params(soin_id):
    with open('./jscode.js', encoding='utf-8') as f:
        js_code = f.read()
    params = {"ids": f"[{soin_id}]", "level": "standard", "encodeType": "aac", "csrf_token": ""}

    res = execjs.compile(js_code).call('getParams', str(params))
    return res


def run():
    cookies = {
        'NMTID': '00OrY_yzDgFisncUEcGkU-gB_2M5sAAAAGLwk1WWg',
        '_iuqxldmzr_': '32',
        '_ntes_nnid': 'ef76c33ce52a9829a3775f48e7730574,1699771931688',
        '_ntes_nuid': 'ef76c33ce52a9829a3775f48e7730574',
        'WM_TID': 'BmuG1HjEsY1ABEBQURd634aKXmPsy6wk',
        'WEVNSM': '1.0.0',
        'WNMCID': 'mcigxs.1699771933548.01.0',
        'WM_NI': 'I6arPOYfnmXW3X%2BbPQpuA%2BZLlgqCT3W2NSp7SLQ1SduIbHptB7KAw4iRDc0sDfnfWTXViDseamlGvGMwQtzLw8B3tOrm%2FTDsO1NtVRl7ZLCHwHzGM8eDYAT20tZkNUsORDI%3D',
        'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeadd55da1ecb791f570f68a8fa2d54a979e9a83d139e98e9785e169fc9db693cd2af0fea7c3b92a8beaaf93d3459bbaa28edb5df188e583d35bb4ab8fccd948b0b9bfa4d73995ee82b4f33d91949fd2d270b797aea9f38082e985a2f640ab8e8c84b37988baa287d6609c8aa7a5f26fa3b3a4a8f54d8fa99f95f948b5e88ed4f745b2b3e1b5c7798def8295d55ab0e996adc244b598b6a8d034a79c97a2d73af4ac968ccd5fb1919ea5cc37e2a3',
        'ntes_utid': 'tid._.Sg2lvlB3inhAQlRFVULE1t7qQFCFvjtg._.0',
        'sDeviceId': 'YD-YaGpsiLdkf1BUxFFRUfVg8v6RVTRqmp4',
        'playerid': '64815770',
        'JSESSIONID-WYYY': '5puXnPBpVswSDs7d%2FaR%5C0sKsbwDs9dVdndf5%2B8Igd9AGskXlHGqw%2FfHKZAErE68rQOFyGpKpXirjDR2uRB4GhaHfWc0bflq%2FcvnuIA1pfM4XY%5CYHyE3aH5aU3vMzUrMSatDU7X4cnQ%2FzRhvVKHwB1AF45Tr3wBF4s6dN8KDHpFypFTlO%3A1699777330334',
    }

    headers = {
        'authority': 'music.163.com',
        'accept': '*/*',
        'accept-language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'NMTID=00OrY_yzDgFisncUEcGkU-gB_2M5sAAAAGLwk1WWg; _iuqxldmzr_=32; _ntes_nnid=ef76c33ce52a9829a3775f48e7730574,1699771931688; _ntes_nuid=ef76c33ce52a9829a3775f48e7730574; WM_TID=BmuG1HjEsY1ABEBQURd634aKXmPsy6wk; WEVNSM=1.0.0; WNMCID=mcigxs.1699771933548.01.0; WM_NI=I6arPOYfnmXW3X%2BbPQpuA%2BZLlgqCT3W2NSp7SLQ1SduIbHptB7KAw4iRDc0sDfnfWTXViDseamlGvGMwQtzLw8B3tOrm%2FTDsO1NtVRl7ZLCHwHzGM8eDYAT20tZkNUsORDI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeadd55da1ecb791f570f68a8fa2d54a979e9a83d139e98e9785e169fc9db693cd2af0fea7c3b92a8beaaf93d3459bbaa28edb5df188e583d35bb4ab8fccd948b0b9bfa4d73995ee82b4f33d91949fd2d270b797aea9f38082e985a2f640ab8e8c84b37988baa287d6609c8aa7a5f26fa3b3a4a8f54d8fa99f95f948b5e88ed4f745b2b3e1b5c7798def8295d55ab0e996adc244b598b6a8d034a79c97a2d73af4ac968ccd5fb1919ea5cc37e2a3; ntes_utid=tid._.Sg2lvlB3inhAQlRFVULE1t7qQFCFvjtg._.0; sDeviceId=YD-YaGpsiLdkf1BUxFFRUfVg8v6RVTRqmp4; playerid=64815770; JSESSIONID-WYYY=5puXnPBpVswSDs7d%2FaR%5C0sKsbwDs9dVdndf5%2B8Igd9AGskXlHGqw%2FfHKZAErE68rQOFyGpKpXirjDR2uRB4GhaHfWc0bflq%2FcvnuIA1pfM4XY%5CYHyE3aH5aU3vMzUrMSatDU7X4cnQ%2FzRhvVKHwB1AF45Tr3wBF4s6dN8KDHpFypFTlO%3A1699777330334',
        'origin': 'https://music.163.com',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
        'csrf_token': '',
    }

    params_dict = get_params('2093980140')

    data = {
        'params': params_dict['encText'],
        'encSecKey': params_dict['encSecKey'],
    }

    response = requests.post(
        'https://music.163.com/weapi/song/enhance/player/url/v1',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.json())


if __name__ == '__main__':
    run()
