"""
author :rain
Date : 2020/07/27
Description :首页
"""
from api_fj.BaseApi import BaseApi

import requests

import constant


# TODO
class HomeApi(BaseApi):

    @staticmethod
    def get_banner():
        "广告banner"
        # 小程序
        params1 = {"platform": 1, "position": 1}
        # app 首页
        params2 = {"platform": 2, "position": 1}
        # app直播中心
        params3 = {"platform": 2, "position": 2}
        # app直播列表
        params4 = {"platform": 2, "position": 3}
        r1 = requests.get(constant.banner_url, params=params1)
        r2 = requests.get(constant.banner_url, params=params2)
        r3 = requests.get(constant.banner_url, params=params3)
        r4 = requests.get(constant.banner_url, params=params4)
        return [r1, r2, r3, r4]


if __name__ == '__main__':
    datas = HomeApi.get_banner()
    for data in datas:
        print(data)
        print(data.json())
        print("\n")
