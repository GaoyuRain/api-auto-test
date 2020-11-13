"""
author :rain
Date : 2020/07/16
Description :登录注册
"""
import json

import requests

from base_fj.fanjiao_config import FanjiaoConfig
from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils
from constant import get_verify_code_url, login_url
from utils_fj.log_utils import LogUtils


class LoginApi:

    def __init__(self):
        self.url_data = DataUtils.get_yaml_data('t01_login_api_data.yaml')

    def user_verify_code(self):
        r = APIUtils.send_request(self.url_data, 'user_verify_code')
        return r

    def user_login(self):
        r = APIUtils.send_request(self.url_data, 'user_login')
        datas = r.json().get('data_fj')
        if datas is not None:
            DataUtils.set_data(datas, 'user_info.yaml')
        return r

    def user_login_wx(self):
        r = APIUtils.send_request(self.url_data, 'user_login_wx')
        return r

    def user_tourist_login(self):
        r = APIUtils.send_request(self.url_data, 'user_tourist_login')
        return r

    def user_wx_login(self):
        r = APIUtils.send_request(self.url_data, 'user_wx_login')
        return r

    def user_wx_bind(self):
        r = APIUtils.send_request(self.url_data, 'user_wx_bind')
        return r

    def user_wx_mini_login(self):
        r = APIUtils.send_request(self.url_data, 'user_wx_mini_login')
        return r

    def user_wx_mini_bind(self):
        r = APIUtils.send_request(self.url_data, 'user_wx_mini_bind')
        return r

    def user_apple_login(self):
        r = APIUtils.send_request(self.url_data, 'user_apple_login')
        return r

    def user_apple_bind(self):
        r = APIUtils.send_request(self.url_data, 'user_apple_bind')
        return r

    def user_third_unbind(self):
        r = APIUtils.send_request(self.url_data, 'user_third_unbind')
        return r

    def user_update(self):
        r = APIUtils.send_request(self.url_data, 'user_update')
        return r

    def user_update_phone(self):
        r = APIUtils.send_request(self.url_data, 'user_update_phone')
        return r

    def user_update_wx(self):
        r = APIUtils.send_request(self.url_data, 'user_update_wx')
        return r

    def user_update_apple(self):
        r = APIUtils.send_request(self.url_data, 'user_update_apple')
        return r


if __name__ == '__main__':
    loginapi = LoginApi()
    loginapi.user_verify_code()
    loginapi.user_login()
    # loginapi.user_login_wx()
    # loginapi.user_tourist_login()
    # loginapi.user_wx_login()
    # loginapi.user_wx_bind()
    # loginapi.user_wx_mini_login()
    # loginapi.user_wx_mini_bind()
    # loginapi.user_apple_login()
    # loginapi.user_apple_bind()
    # loginapi.user_third_unbind()
    # loginapi.user_update()
    # loginapi.user_update_phone()
    # loginapi.user_update_wx()
    # loginapi.user_update_apple()

