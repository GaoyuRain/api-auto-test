"""
author :rain
Date : 2020/07/20
Description :
"""
import unittest

from api_fj.live_api import LiveApi


class TestLive(unittest.TestCase):

    @unittest.skip("直播暂时不可用")
    def test_01_gift_list(self):
        """礼物列表"""
        r = LiveApi.get_gift_list()
        data = dict(r.json()).get('data_fj')
        print(data)
        giftList: list = data.get('list')
        print(len(giftList))
        self.assertTrue(len(giftList) > 0)
        for i in range(len(giftList)):
            self.assertIsNotNone(giftList[i].get('gift_id'))
            self.assertTrue(len(giftList[i].get('name')) > 0)
            self.assertTrue(giftList[i].get('rice') > 0)
            self.assertTrue(len(giftList[i].get('icon')) > 0)
            if giftList[i].get('duration') > 0:
                self.assertTrue(len(giftList[i].get('video_url')) > 0)


if __name__ == '__main__':
    unittest.main()
