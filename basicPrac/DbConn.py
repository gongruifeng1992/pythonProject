# python3.8.2,使用pymysql
# 1-导包
import pymysql


def conn_demo():
    # 2-创建链接
    connection = pymysql.connect(host='localhost', user='root', password='13219709580.grF', db='test', charset='utf8')
    print("数据库版本：", connection.get_server_info())
    print("连接地址：", connection.host)

    # 3-创建游标，用于执行sql语句
    cursor = connection.cursor()

    # 4-执行sql语句，获取结果集
    sql = "select * from `order`"  # 注意引号，不然要报错
    row_count = cursor.execute(sql)
    print("获取到数据行数为：", row_count)

    # 5-操作结果集
    data1 = cursor.fetchone()  # 获取一条数据，元组封装
    data2 = cursor.fetchmany(2)  # 获取2条数据，元组嵌套
    data3 = cursor.fetchall()  # 获取所有数据

    for line in data3:
        print(line)

    # 6-释放资源
    cursor.close()
    connection.close()


# create table poets(
#     id int PRIMARY KEY ,
# username VARCHAR(10),
# birthday INT,
# masterpiece VARCHAR(10)

# 1-增加数据
def add_data():
    conn = pymysql.connect(host='localhost', user='root', password='13219709580.grF', db='test', charset='utf8')
    cursor = conn.cursor()
    sql = 'INSERT INTO `test`.`poets` (`id`, `username`, `birthday`, `masterpiece`) VALUES (null, \'李白\', 701, \'将进酒\');'
    row_count = cursor.execute(sql)
    print("受影响行数：", row_count)
    conn.commit()
    cursor.close()
    conn.close()

# 2-修改数据
def update_date():
    conn = pymysql.connect(host='localhost', user='root', password='13219709580.grF', db='test', charset='utf8')
    cursor = conn.cursor()
    sql = 'UPDATE `test`.`poets` SET `username` = \'李白\', `birthday` = 701, `masterpiece` = \'静夜思\' WHERE `id` = 1;'
    row_count = cursor.execute(sql)
    print("受影响行数：", row_count)
    conn.commit()
    cursor.close()
    conn.close()

# 3-删除数据
def delete_data():
    conn = pymysql.connect(host='localhost', user='root', password='13219709580.grF', db='test', charset='utf8')
    cursor = conn.cursor()
    sql = 'DELETE FROM poets WHERE `masterpiece` = \'静夜思\';'
    row_count = cursor.execute(sql)
    print("受影响行数：", row_count)
    conn.commit()
    cursor.close()
    conn.close()

# 4-注入
def attack():
    uname = input("Please input your account:")
    pwd = input("Please input your password:")

    conn = pymysql.connect(host='localhost', user='root', password='13219709580.grF', db='test', charset='utf8')
    cursor = conn.cursor()

    sql="select * from `user` where `username`='%s' and `password`='%s';"%(uname,pwd)
    row_count = cursor.execute(sql)

    print("登录成功" if row_count > 0 else "登录失败")
    cursor.close()
    conn.close()

# 5-事务处理
def transaction():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='13219709580.grF', db='test', charset='utf8')
        cursor = conn.cursor()

        conn.begin() #事务由此开始
        sql1="update wallet set money = money - 1000 where name = '张三';"
        row_count1=cursor.execute(sql1)
        result=3/0
        print("影响行数：",row_count1)
        sql2="update wallet set money = money + 1000 where name = '李四';"
        row_count2=cursor.execute(sql2)
        print("影响行数：",row_count2)
    except Exception as e:
        conn.rollback()
        print(e.__context__)
        print("转账异常，请稍后重试！")

    else:
        conn.commit()
        print("转账成功！" if row_count1==1 and row_count2==1 else "转账失败！")
    finally:
        cursor.close()
        conn.close()
        print("资源释放完毕")

if __name__ == '__main__':
    transaction()
