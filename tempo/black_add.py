import time

from pymysql.connections import Connection
import requests
import pymysql
from sshtunnel import SSHTunnelForwarder
from threading import Lock

# post
# remove_blcak='http://test-api.rela.me/interface/stay/appUser!removeFromBlackList.do'
# debug=0&lng=121.485951&language=zh_CN_%23Hans&clientVersion=50209&userId=106759842&deviceId=sm_202002241750093303ef416552e65f37bd12e40ca96a61016a361a53e82a63
# &key=17yNWtrcpykXaMXsPi7fIYV2kPaKDVZT-106789885&lat=31.24588&mobileOS=Android%2010

userids = []


# 850：106800022
def get_userlist():
    # connc = Connection(host="39.100.228.129", port=4000, database="stay", user="admin",
    #                    password="testadminds2019", charset="utf8")

    connc = Connection(host="39.100.228.129", port=4000, database="stay", user="admin",
                       password="testadminds2019", charset="utf8")
    cursor = connc.cursor()
    # 1100
    q_sql = "select * from stay.app_user limit 1100,100"

    cursor.execute(q_sql)
    rowcount = cursor.rowcount
    print(rowcount)
    # 获取所有查询内容
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        # print("-" * 20)
        # print("id:", row[0])
        userids.append(row[0])

    cursor.close()
    connc.close()


def add_black():
    # get_userlist()
    url = 'http://test-api.rela.me/v3/interface/stay/pullUserIntoBlackList'
    data1 = {'userId': '34', 'key': 'o5ZPxFlpaRXDYxqM51bPldqdWFvUrhlp-106851715', 'lat': '31.2 45887',
             'lng': '121.485891', 'language': 'zh_CN_%23Hans', 'mobileOS': 'Android+10',
             'deviceId': 'sm_20190411160642ade026b965810f1d2fc433ac1dfd0d8a0135b82a64d134bf', 'apptype': '',
             'clientVersion': '50209'}
    # r = requests.post(url, data1)
    # print(r.json())
    for i in userids:
        print(i)
        data1.update({'userId': i})
        r = requests.post(url, data1)
        print(r.json())
        time.sleep(0.3)

def read_ids():
    # 读取用户id
    global userids
    with open('../data_fj/tempodata/userids', 'r', encoding='utf-8') as cont:
        aa = cont.readlines()
    for i in aa:
        userids.append(i.strip("\n"))
    print(userids)


def conect():
    with SSHTunnelForwarder(
            ('47.92.64.250', 6022),  # ssh IP和port
            ssh_username="admin",  # 这里是运维给你的用户名，而不是数据库的用户名
            ssh_pkey="~/.ssh/id_rsa",  # 这里是运维给你的公钥文件存放地址
            remote_bind_address=('47.92.64.250', 2222)) as server:
        conn = pymysql.connect(
            host='127.0.0.1',
            # host='pc-8vbl25i85y93w1ml9.mysql.polardb.zhangbei.rds.aliyuncs.com',
            port=server.local_bind_port,
            user='yugao',
            passwd='c3883Ga2f6621#Q2',
            db='stay'
        )
        cur = conn.cursor()
        lock = Lock()
        lock.acquire()
        cur.execute("select * from stay.app_user limit 1100,100")
        lock.release()
        print(cur.fetchall())


if __name__ == '__main__':
    # add_black()
    # conect()
    read_ids()
    add_black()

