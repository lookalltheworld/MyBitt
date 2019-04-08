from appium import webdriver
import datetime
import time
import pymysql
def phone_code(mobile_phone):

    try:
        db = pymysql.connect("10.0.17.104", "root", "maon123456", "mrlextdb", charset='utf8')
    except:
        print("无法连接数据库")
    cursor = db.cursor()

    cursor.execute("select * from  tm_sms_send where phone='%s' ORDER BY create_time DESC LIMIT 1 ;",
                   mobile_phone)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print(data)
    p = data[2].split('：')
    a = p[1].split('，')
    b = a[0]

    # 关闭数据库连接
    db.close()
    return b
phone_code(13978637441)