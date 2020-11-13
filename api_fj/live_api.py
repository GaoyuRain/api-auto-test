"""
author :rain
Date : 2020/07/16
Description :直播相关
"""

import requests

import constant
from utils_fj.data_utils import DataUtils
from utils_fj.file_utils import FileUtils
from constant import get_gift_list_url


class LiveApi:

    @staticmethod
    def get_gift_list():
        """礼物列表"""
        get_my_follow_param = {'page': 1, 'size': 20}
        # r = requests.get(get_gift_list_url, headers=DataUtils.get_user_info(), params=get_my_follow_param)
        print(get_gift_list_url)
        r = requests.get(get_gift_list_url, headers=DataUtils.get_user_info())
        print(r)
        print(r.json())
        data = dict(r.json())
        DataUtils.set_data(data.get('data_fj').get('list'), 'gift_list.yaml')
        FileUtils.downdload_gift_icon()
        return r

    @staticmethod
    def get_top_ranking(owneruid: int):
        '''
        守护总榜单
        :param owneruid: 房间拥有者id
        :return:
        '''
        top_ranking_param = {'owner_uid': owneruid}
        r = requests.get(constant.gift_top_ranking_url, headers=DataUtils.get_user_info(), params=top_ranking_param)
        print(r)
        print(r.json())

    @staticmethod
    def get_current_ranking(owneruid: int):
        """本场守护榜"""
        top_ranking_param = {'owner_uid': owneruid}
        r = requests.get(constant.gift_current_ranking_url, headers=DataUtils.get_user_info(), params=top_ranking_param)
        print(r)
        print(r.json())

    @staticmethod
    def live_report(reportee, room_id):
        """直播间举报"""
        live_report_param = {
            # "reporter": DataUtils.get_user_info('user').get('uid'),
            "reportee": reportee,
            "report_type": 1,
            "reason": "hahaha6666",
            "room_id": room_id,
            "reportee_type": 1
            # "pics": "[]"
        }
        r = requests.post(constant.live_report_url, headers=DataUtils.get_user_info(),
                          json=live_report_param)
        print(r.json())


if __name__ == '__main__':
    LiveApi.get_gift_list()
    # LiveApi.get_top_ranking(1000089)
    # LiveApi.get_current_ranking(1000089)
    # LiveApi.live_report(1000089, "fanjiao-1000089")
