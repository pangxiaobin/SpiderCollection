#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : silderDemo.py
import json
import random
import re
import time

from playwright.sync_api import sync_playwright


def get_job_info(keyword, max_page=100, jobArea="010000"):
    """

    :param keyword: 搜索的信息
    :param max_page:  最大爬取页
    :param jobArea: 地区
    :return:
    """
    with sync_playwright() as playwright:
        # 设置可视化界面
        # browser = playwright.chromium.launch(headless=False)
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page_obj = context.new_page()
        # # 关闭Webdriver属性
        js = """
                Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
                """
        page_obj.add_init_script(js)
        for page in range(max_page):
            timestamp = int(time.time() * 1000)
            page_obj.goto(
                f"https://we.51job.com/api/job/search-pc?api_key=51job&timestamp={timestamp}"
                f"&keyword={keyword}&searchType=2&function=&industry=&jobArea={jobArea}"
                f"&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType"
                f"=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}"
                f"&requestId=f54026ee5b71be1db486d8f841922780&pageSize=20&source="
                f"1&accountId=&pageCode=sou%7Csou%7Csoulb"
            )
            page_obj.wait_for_selector("#nc_1__scale_text")
            # Wait for the captcha slider element to appear
            page_obj.wait_for_selector("#nc_1_n1z")

            # 计算滑块结束位置的坐标
            slider_element = page_obj.query_selector("#nc_1_n1z")
            box = slider_element.bounding_box()
            start_x = box["x"] + box["width"] / 2
            start_y = box["y"] + box["height"] / 2
            end_x = start_x + 300  # 你要移动的像素距离

            # 移动滑块
            page_obj.mouse.move(start_x, start_y)
            page_obj.mouse.down()
            page_obj.mouse.move(end_x, start_y, steps=random.randint(30, 40))
            page_obj.mouse.up()
            time.sleep(random.randint(3, 10))
            html_res = page_obj.content()
            pattern = r'pre-wrap;">(.*?)</pre></body></html>'
            result = re.search(pattern, html_res)
            if result:
                page_info = result.group(1)
                try:
                    job_item = json.loads(page_info)['resultbody']['job']['items']
                except Exception as e:
                    print(f'抓取页面数据异常:{page}页 keyword:{keyword} Exception:{e}')
                print(job_item)
            else:
                print(f'抓取页面数据异常:{page}页 keyword:{keyword}')

        # 关闭浏览器
        browser.close()


if __name__ == '__main__':
    get_job_info('python', max_page=1)
