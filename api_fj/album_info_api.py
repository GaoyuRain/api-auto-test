"""
author :rain
Date : 2020/10/21
Description :专辑详情页面
"""

# DataUtils

from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class AlbumInfoAPI:

    def __init__(self):
        self.url_data = DataUtils.get_yaml_data('t05_album_info_api_data.yaml')

    def album_info(self):
        r = APIUtils.send_request(self.url_data, 'album_info')
        return r

    def actor_cv(self):
        r = APIUtils.send_request(self.url_data, 'actor_cv')
        return r

    def album_audio(self):
        r = APIUtils.send_request(self.url_data, 'album_audio')
        return r

    def album_recommend(self):
        r = APIUtils.send_request(self.url_data, 'album_recommend')
        return r

    def buy_album(self):
        r = APIUtils.send_request(self.url_data, 'buy_album')
        return r

    def follow_album(self):
        r = APIUtils.send_request(self.url_data, 'follow_album')
        return r

    def album_history(self):
        r = APIUtils.send_request(self.url_data, 'album_history')
        return r

    def album_list(self):
        r = APIUtils.send_request(self.url_data, 'album_list')
        return r

    def reward_buy(self):
        r = APIUtils.send_request(self.url_data, 'reward_buy')
        return r

    def reward_rank(self):
        r = APIUtils.send_request(self.url_data, 'reward_rank')
        return r


if __name__ == '__main__':
    albuminfo = AlbumInfoAPI()
    albuminfo.reward_buy()
    albuminfo.album_info()
    albuminfo.actor_cv()
    albuminfo.album_audio()
    albuminfo.album_recommend()
    albuminfo.buy_album()
    albuminfo.follow_album()
    albuminfo.album_history()
    albuminfo.album_list()
    albuminfo.reward_rank()
