import json

import requests

from base_fj.fanjiao_config import signature, get_Host

# rain
# token = "3AUnGOnF97fKFdYlW9Uzm9dXf2ooRBEC-362890"
# from fanjiao_config import host
from tempo.fanjiao_url01 import get_verify_code_url, login_url, get_my_follow_url, notice_url, notice_list_url, \
    update_album_url, new_album_url, user_info_url, is_read_url, rice_list_url, rice_list_param, \
    get_my_follow_param, notice_param3, notice_param1, notice_param2, notice_list_param, login_param, \
    update_album_param, new_album_param, notice_param4

host = get_Host(False)


class FanjiaoApi01:

    def __init__(self, phone):
        self.phone = phone
        # self.token = DButils.get_token("+86" + self.phone)
        self.token = "zXoXc4JLd8A8xXSQHssiymDz17YuGzI1-1000162"
        self.headertoken = {"token": self.token}
        requests.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        self.s: requests.Session = s

    def get_verify_code(self):
        data = {"phone": self.phone}
        data['signature'] = signature(data)
        r = self.s.get(host + get_verify_code_url, params=data)
        print(r.json())

    def login(self):
        login_param['signature'] = signature(login_param)
        r = self.s.post(host + login_url, json.dumps(login_param))
        jsondata = r.json()
        print(jsondata)
        self.token = jsondata.get('data_fj').get("token")
        self.headertoken = {"token": self.token}
        print(self.token)

    # 追剧列表
    def get_my_follow(self):
        r = self.s.get(host + get_my_follow_url, headers=self.headertoken, params=get_my_follow_param)
        datalist = r.json()
        print(datalist)
        folowlist = list(datalist.get("data_fj").get("follow_album_list"))
        print(len(folowlist))
        # print(datalist)

    # 发送通知
    def send_notice(self):
        # 图文加站内链接

        r1 = self.s.post(host + notice_url, json.dumps(notice_param1))
        r2 = self.s.post(host + notice_url, json.dumps(notice_param2))
        r3 = self.s.post(host + notice_url, json.dumps(notice_param3))
        r4 = self.s.post(host + notice_url, json.dumps(notice_param4))
        # print(r1.json())
        # time.sleep(1)
        # print(r2.json())
        # time.sleep(1)
        # print(r3.json())
        # time.sleep(1)
        print(r4.json())

    # 通知列表
    def notice_list(self):
        # data_fj = {"page": 1, "size": 20}

        notice_list_param['signature'] = signature(notice_list_param)
        r = self.s.get(host + notice_list_url, headers=self.headertoken, params=notice_list_param)
        datalist = r.json()
        print(datalist)

    # 动态列表
    def activity_list(self):
        # 动态列表
        activity_list_url = "/walkman/api_fj/user/activity"
        activity_list_param = {"page": 1, "size": 20}
        r = self.s.get(host + activity_list_url, headers=self.headertoken, params=activity_list_param)
        datalist = r.json()
        print(datalist)

    # 剧集更新
    def update_album(self):
        r = self.s.post(host + update_album_url, json.dumps(update_album_param))
        datalist = r.json()
        print(datalist)

    # 新剧上线
    def new_update_album(self):
        r = self.s.post(host + new_album_url, json.dumps(new_album_param))
        print(r)
        datalist = r.json()
        print(datalist)

    # def update_info():
    #     token1 = {"token": token}
    #     data_fj = {"gender": 1}
    #     r = requests.post(host + new_album_url+"?key="+token, json.dumps(data_fj))
    #     datalist = r.json()
    #     print(datalist)

    # 获取用户信息
    def get_user_info(self):
        r = self.s.get(host + user_info_url, headers=self.headertoken)
        datalist = r.json()
        print(datalist)

    # 获取是未读消息数量
    def get_is_read(self):
        r = self.s.get(host + is_read_url, headers=self.headertoken)
        datalist = r.json()
        print(datalist)

    # 充值记录
    def get_rice_list(self):
        '''
        充值记录列表
        :return: none
        '''
        r = self.s.get(host + rice_list_url, headers=self.headertoken, params=rice_list_param)

        datalist = r.json()
        print(datalist)
        folowlist = list(datalist.get("data_fj").get("list"))
        print(len(folowlist))


if __name__ == '__main__':
    fjapi = FanjiaoApi01("19999999835")
    # get_verify_code()
    # time.sleep(0.5)
    # login()
    # time.sleep(0.5)
    # fjapi.get_my_follow()
    # fjapi.send_notice()
    # fjapi.get_verify_code()
    # fjapi.login()
    # fjapi.notice_list()
    # fjapi.upd/ate_album()
    # time.sleep(0.5)
    fjapi.new_update_album()
    # activity_list()
    # update_info()
    # get_user_info()
    # fjapi.get_is_read()
    # fjapi.get_rice_list()
