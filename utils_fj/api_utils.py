"""
author :rain
Date : 2020/10/27
Description :
"""
import requests

import constant
from base_fj.fanjiao_config import FanjiaoConfig
from utils_fj.data_utils import DataUtils
from utils_fj.log_utils import LogUtils


class APIUtils:

    @staticmethod
    def send_request(params_data):
        url = constant.BASE_URL + params_data.get('url')
        params = params_data.get('params')
        type = params_data.get('type').lower()
        header = DataUtils.get_user_info()
        header.update(FanjiaoConfig.signature_fj(params, type))

        requests.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        if 'get'.__eq__(type):
            r = requests.get(url, headers=header, params=params, timeout=10)
        else:
            r = requests.post(url, headers=header, json=params, timeout=10)
        LogUtils.print_response(r, params_data.get('comment'))
        return r
