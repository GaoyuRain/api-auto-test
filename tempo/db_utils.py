import sys

from pymysql.connections import Connection


class DButils:
    '''
    饭角数据库连接
45.124.124.176
admin： ff433e6d1fc118
    '''
    connc = None
    idc_host = "45.124.124.176"
    idc_user = "admin"
    idc_password = "ff433e6d1fc118"

    # @classmethod
    # def get_connc_info(cls):
    #     connc = Connection(host="127.0.0.1", port=3306, database="books", user="root",
    #                        password="root", charset="utf8")
    #     cursor = connc.cursor()
    #     return connc, cursor
    #
    # @classmethod
    # def close_resourse(cls, conc: Connection, cursor):
    #     if conc:
    #         conc.close()
    #         conc = None
    #         print('conc0:', conc)
    #     if cursor:
    #         cursor.close()
    #         cursor = None
    #         print('cursor0:', cursor)

    @staticmethod
    def get_token(phone):
        connc = Connection(host=DButils.idc_host, port=3306, database="walkman", user=DButils.idc_user,
                           password=DButils.idc_password, charset="utf8")
        cursor = connc.cursor()
        # 1100
        q_sql = "select uid from walkman.user_info where phone=" + phone + " limit 1"
        cursor.execute(q_sql)
        rowcount = cursor.rowcount
        print(rowcount)
        # 获取所有查询内容
        rows1 = cursor.fetchall()
        print(rows1)
        uid = ''
        for row in rows1:
            print("-" * 20)
            uid = str(row[0])
            print("usderid:", uid)

        q_sql1 = "select token from walkman.user_login where uid=" + uid
        cursor.execute(q_sql1)
        rows2 = cursor.fetchall()
        print(rows2)
        token = ""
        for row in rows2:
            print("-" * 20)
            token = row[0]
            print("token:", token)
        #     userids.append(row[0])

        cursor.close()
        connc.close()
        return token


if __name__ == '__main__':
    dbutils = DButils()
    dbutils.get_token("+8615225111055")
