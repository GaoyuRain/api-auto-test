"""
author :rain
Date : 2020/07/16
Description :
# 对外 api_fj 前缀：/walkman/api_fj
# 对内 api_fj 前缀：/walkman/internal/api_fj （对内接口需走 svc
"""
import os


# from base_fj.fanjiao_config import get_host

# BASE_URL_INNER = BASE_URL + "/walkman/internal/api_fj"

def get_host(type):
    cur_host = ""
    if 'test'.__eq__(type):
        cur_host = "http://test-api.fanjiao.co/walkman/api"
    elif 'pre'.__eq__(type):
        cur_host = "http://pre-api.fanjiao.co/walkman/api"
    else:
        cur_host = 'http://api.fanjiao.co/walkman/api'
    return cur_host


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_URL = get_host('pro')
# 用户信息
user_info = None
# 是否打印log
hasLog = True

"""登录"""
# 获取验证码
get_verify_code_url = BASE_URL + "/user/verify_code"
# 登录
login_url = BASE_URL + "/user/login"

"""直播相关"""
# 礼物列表 get
get_gift_list_url = BASE_URL + "/gift/list"
# 守护总榜 get
gift_top_ranking_url = BASE_URL + "/gift/top_ranking"
# 本场守护榜 get
gift_current_ranking_url = BASE_URL + '/gift/current_ranking'

# 礼物赠送 post
# send_gift_url = BASE_URL_INNER + "/gift/send"
# # 清除直播场次榜单 post
# clear_current_ranking = BASE_URL_INNER + "/clear/current_ranking"
# # 查询用户饭票数 get
# get_user_ticket = BASE_URL_INNER + "/gift/user/rice_ticket"
# # 查询用户当前房间榜单名次 get
# get_user_ranking = BASE_URL_INNER + "/gift/user/ranking"
# 直播间举报
live_report_url = BASE_URL + "/live/report"
#


"""我的页面"""
# 个人信息页面
user_info_url = BASE_URL + "/user/info"
# 用户关注列表
user_attention_url = BASE_URL + "/user/attention"
# 用户粉丝列表
user_fans_url = BASE_URL + "/user/fans"
# 我的追剧列表
user_my_flow = BASE_URL + "/user/my_follow"
# 用户追剧列表
user_flow_albumlist = BASE_URL + "/user/follow/album_list"
# 小铃铛（轮询接口）
user_not_read = BASE_URL + "/user/not_read"
# 通知列表
user_notice = BASE_URL + "/user/notice"
# 动态列表
user_activity = BASE_URL + "/user/activity"
# 追剧更新已读（用于 我的->追剧栏中跳转）
user_read_album = BASE_URL + "/user/read_album"
# 已购列表
user_purchase_list = BASE_URL + "/user/purchase_list"
# 关注/取消关注user
user_follow = BASE_URL + "/user/follow_user"

# 直播中心-直播饭票数
user_live_ticket_url = BASE_URL + "/gift/user/live_ticket"
# 用户余额
account_detail_url = BASE_URL + "/account/detail"
# 充值记录
account_rice_list_url = BASE_URL + "/account/rice/list"
# 消费记录
account_consume_list_url = BASE_URL + "/account/consume/list"

"""首页"""
# 首页/直播列表/直播中心 banner
banner_url = BASE_URL + "/recommend/banner"

if __name__ == '__main__':
    print(BASE_DIR)
    print(BASE_URL)
