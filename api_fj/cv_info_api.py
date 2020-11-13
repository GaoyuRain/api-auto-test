"""
author :rain
Date : 2020/10/28
Description :cv信息
"""
from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class LoginApi:

    def __init__(self):
        self.url_data = DataUtils.get_yaml_data('t04_cv_info_api_data.yaml')

    def cv_info(self):
        r = APIUtils.send_request(self.url_data, 'cv_info')
        return r

    def album_cv_list(self):
        r = APIUtils.send_request(self.url_data, 'album_cv_list')
        return r

    def user_follow_cv(self):
        r = APIUtils.send_request(self.url_data, 'user_follow_cv')
        return r

    def cv_attention(self):
        r = APIUtils.send_request(self.url_data, 'cv_attention')
        return r

    def cv_fans(self):
        r = APIUtils.send_request(self.url_data, 'cv_fans')
        return r


