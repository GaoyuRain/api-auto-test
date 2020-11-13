"""
author :rain
Date : 2020/07/21
Description :我的页面
"""
import requests

import constant
from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils
from utils_fj.log_utils import LogUtils


class MyApi:

    def __init__(self):
        self.url_data = DataUtils.get_yaml_data('t03_my_api_data.yaml')

    def user_info(self):
        r = APIUtils.send_request(self.url_data, 'user_info')
        return r

    def user_attention_list(self):
        r = APIUtils.send_request(self.url_data, 'user_attention_list')
        return r

    def user_fans(self):
        r = APIUtils.send_request(self.url_data, 'user_fans')
        return r

    def user_my_flow(self):
        r = APIUtils.send_request(self.url_data, 'user_my_flow')
        return r

    def user_flow_albumlist(self):
        r = APIUtils.send_request(self.url_data, 'user_flow_albumlist')
        return r

    def user_not_read(self):
        r = APIUtils.send_request(self.url_data, 'user_not_read')
        return r

    def user_notice(self):
        r = APIUtils.send_request(self.url_data, 'user_notice')
        return r

    def user_activity(self):
        r = APIUtils.send_request(self.url_data, 'user_activity')
        return r

    def user_read_album(self):
        r = APIUtils.send_request(self.url_data, 'user_read_album')
        return r

    def user_purchase_list(self):
        r = APIUtils.send_request(self.url_data, 'user_purchase_list')
        return r

    def follow_user(self):
        r = APIUtils.send_request(self.url_data, 'follow_user')
        return r


if __name__ == '__main__':
    myapi = MyApi()
    # myapi.user_info()
    # myapi.user_attention_list()
    # myapi.user_fans()
    # myapi.user_my_flow()
    # myapi.user_flow_albumlist()
    myapi.user_not_read()
    # myapi.user_notice()
    # myapi.user_activity()
    # myapi.user_read_album()
    # myapi.user_purchase_list()
    # myapi.follow_user()
