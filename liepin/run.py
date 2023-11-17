#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
import json

import execjs
import requests


def get_trace_id():
    with open('./jscode.js', encoding='utf-8') as f:
        js_code = f.read()
    trace_id = execjs.compile(js_code).call('getTraceId')
    return trace_id


def run():
    cookies = {
        'XSRF-TOKEN': 'KCNNBUzkTc6KmIA44EYTTQ',
        '__gc_id': '38a4a788c0544fa5b05d427847394174',
        '__uuid': '1700205285262.09',
        'Hm_lvt_a2647413544f5a04f00da7eee0d5e200': '1700205286',
        '_ga': 'GA1.1.176558359.1700206027',
        'acw_tc': '276077db17002071291317333ed8bc4886fd9d8f27973e6ea11af9620884ec',
        '__tlog': '1700205285267.84%7C00000000%7C00000000%7Cgg_pc_02%7Cgg_pc_02',
        '_gcl_aw': 'GCL.1700207544.Cj0KCQiAmNeqBhD4ARIsADsYfTfOhENBwZJ-921Seo_nx68-9QjwRcUyemUfzBTooqHy-5hTcgslVssaAvcAEALw_wcB',
        '_gcl_au': '1.1.1700661451.1700207544',
        '_uetsid': '3f13d470851e11ee8811294005316d33',
        '_uetvid': '3f1404b0851e11eeacef470cbf27a9e9',
        '_ga_Q11MZCVPQN': 'GS1.1.1700207543.1.0.1700207545.0.0.0',
        'Hm_lpvt_a2647413544f5a04f00da7eee0d5e200': '1700207557',
        '_ga_54YTJKWN86': 'GS1.1.1700206026.1.1.1700207753.0.0.0',
        '__tlg_event_seq': '92',
        '__session_seq': '18',
        '__uv_seq': '18',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8;',
        'Origin': 'https://www.liepin.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.liepin.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Client-Type': 'web',
        'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=1&pageSize=40&key=python&suggestTag=&workYearCode=0&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&skId=hojhqg3eiakc72qcb55s9m3oc36nmdub&sfrom=search_job_pc&fkId=hojhqg3eiakc72qcb55s9m3oc36nmdub&ckId=rv3b64m5ctjhibco3gmg6cijecd010da&scene=page&suggestId="}',
        'X-Fscp-Fe-Version': '',
        'X-Fscp-Std-Info': '{"client_id": "40108"}',
        'X-Fscp-Trace-Id': 'e96340b5-fdd0-4880-ae96-2aa619398933',
        'X-Fscp-Version': '1.1',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'KCNNBUzkTc6KmIA44EYTTQ',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    json_data = {
        'data': {
            'mainSearchPcConditionForm': {
                'city': '010',
                'dq': '010',
                'pubTime': '',
                'currentPage': 0,
                'pageSize': 40,
                'key': 'python开发',
                'suggestTag': '',
                'workYearCode': '0',
                'compId': '',
                'compName': '',
                'compTag': '',
                'industry': '',
                'salary': '',
                'jobKind': '',
                'compScale': '',
                'compKind': '',
                'compStage': '',
                'eduLevel': '',
                'otherCity': '',
            },
            'passThroughForm': {
                'scene': 'page',
                'skId': 'sz68pt8lfv679i6ai3ra5fcstrmvf4e9',
                'fkId': 'sz68pt8lfv679i6ai3ra5fcstrmvf4e9',
                'sfrom': 'search_job_pc',
                'ckId': '2is4e6ynku6dfhqm77f0913qagb07599',
            },
        },
    }
    trace_id = get_trace_id()
    # 更新X-Fscp-Trace-Id
    headers['X-Fscp-Trace-Id'] = trace_id
    response = requests.post(
        'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(json.dumps(response.json()))
    if response.json()['flag'] != 1:
        raise ValueError('IP被封控，需界面进行验证')


if __name__ == '__main__':
    run()
