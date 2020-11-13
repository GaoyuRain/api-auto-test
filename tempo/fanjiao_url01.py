# 获取验证码
get_verify_code_url = "/walkman/api_fj/user/verify_code"

# 登录
login_url = "/walkman/api_fj/user/login"
login_param = {"zone": "+99","phone": "19999999835", "verify_code": "0000", "device_type": 2}

# 个人信息
user_info_url = "/walkman/api_fj/user/info"

# 追剧列表
get_my_follow_url = '/walkman/api_fj/user/my_follow'
get_my_follow_param = {"page": 1, "size": 20}

# 发送通知
notice_url = "/walkman/internal/api_fj/user/notice"
# 纯文字通知 客服通知 单体用户
notice_param1 = {"type": 3, "uid": 294801, "from_uid": 100000, "title": "0426文字通知标题",
                 "content": "0426您的评论违规已被删除1111111111111111111111111111111111"}
# 图文通知 活动推送 全体用户
notice_param2 = {"type": 2, "from_uid": 362890, "title": "0426图文通知标题1",
                 "content": "0426图文通知内容图文通知内容图文通知内容图文通知内容图文通知内容",
                 "cover": "https://wx.qlogo.cn/mmopen/vi_32/PsttDWUPeRluldpMctHiaSMe7lOHrhCf2ib92E0gN4Abr8ibS6oguug25Bqu1N9TZRESKWIhFlNouRUqoy9ZClQTA/132",
                 "link": ""}
# 图文加站外链接
notice_param3 = {"type": 2, "from_uid": 362890, "title": "0426图文加站外链接通知标题1",
                 "content": "0426图文加链接通知内容，图文加链接通知内容，图文加链接通知内容",
                 "cover": "http://static.rela.me/BuZzE1MzQ3NDkxNjE3NTA=.png",
                 "link": "https://www.baidu.com/"}
# 剧集更新通知
notice_param4 = {"type": 1, "title": "0427寻秋更新了", "from_uid": 362890,
                 "album_id": 368, "album_name": "寻秋2",
                 "audio_name": "寻秋：雷音原创，双子星工作室出品，全年龄剧情广播剧",
                 "cover": "http://static.rela.me/BuZzE1MzQ3NDkxNjE3NTA=.png",
                 "content": "11"
                 # "cover": "http://static.rela.me/BuZzE1MzQ3NDkxNjE3NTA=.png"
                 }
# 通知列表
notice_list_url = "/walkman/api_fj/user/notice"
notice_list_param = {"page": 1, "size": 20}

# 动态列表
activity_list_url = "/walkman/api_fj/user/activity"
activity_list_param = {"page": 1, "size": 20}

# 追剧更新
update_album_url = "/walkman/internal/api_fj/push/album/update"
update_album_param = {"album_id": 368, "album_name": "《427寻秋》", "audio_name": "427寻秋：雷音原创，双子星工作室出品，全年龄剧情广播剧"}

# 新剧上线
new_album_url = "/walkman/internal/api_fj/push/album/new"
new_album_param = {"title": "新剧上线：《427寻秋》01", "content": "4727《寻秋》测试内容11111112222222222222222222222222222222222222222",
                   "album_id": 368}

# 更新用户信息/编辑资料
update_user_info_url = "/walkman/api_fj/user/update"

# 小铃铛接口
is_read_url = "/walkman/api_fj/user/not_read"

# 充值列表
rice_list_url = "/walkman/api_fj/account/rice/list"
rice_list_param = {"page": 1, "size": 20}
