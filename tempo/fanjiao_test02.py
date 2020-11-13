import json

import requests

from base_fj.fanjiao_config import get_Host
from tempo.fanjiao_url01 import get_verify_code_url, login_url, login_param
from tempo.fanjiao_url02 import get_gift_list, send_gift_url

host = get_Host(True)

token = None


class FanjiaoApi02:

    def __init__(self, phone):
        self.phone = phone
        # self.headertoken = {"token": self.token}
        requests.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        self.s: requests.Session = s
        self.headerToken = {"token": 'Fowaoqw6nJSsJpEBKRALcB7fERSoLyVC-1000048'}

    def login(self):
        # login_param = {"phone": "19999999835", "verify_code": "0000", "device_type": 2}
        # self.get_verify_code()
        # 获取验证码
        data = {'zone': '+99', "phone": self.phone}
        # data_fj['signature'] = signature(data_fj)
        r = self.s.get(host + get_verify_code_url, params=data)
        print(r.json())

        # 登录
        login_param['phone'] = self.phone
        r = self.s.post(host + login_url, json.dumps(login_param))
        jsondata = r.json()
        print(jsondata)
        self.token = jsondata.get('data_fj').get("token")
        self.headerToken = {"token": self.token}
        print(self.token)
        return {"token": self.token}

    def get_gift_list(self):
        ''' 获取礼物列表'''
        get_my_follow_param = {'page': 1, 'size': 30}
        r = self.s.get(host + get_gift_list, headers=self.headerToken, params=get_my_follow_param)
        print(r)
        dataList = r.json()
        print(dataList)

    def send_gift(self):
        send_gift_params = {'gift_id': 1, "count": 1, 'from_uid': 1000049, 'to_uid': 1000040, 'rice': 12}
        url = host + send_gift_url
        print(url)
        r = self.s.post(url, json.dumps(send_gift_params))
        print(r)
        print(r.json())


if __name__ == '__main__':
    fjTest02 = FanjiaoApi02('19999999836')
    # fjTest02.get_verify_code()
    # fjTest02.login()
    # fjTest02.get_gift_list()
    fjTest02.send_gift()
