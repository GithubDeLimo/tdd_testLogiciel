import sqlite3


# def create_sql():
#     sql = sqlite3.connect("user_data.db")
#     sql.execute("""create table if not exists
#         %s(
#         %s integer primary key autoincrement,
#         %s varchar(128),
#         %s varchar(128),
#         %s varchar(128))"""
#                 % ('user',
#                    'id',
#                    'username',
#                    'password',
#                    'links'
#                    )
#                 )
#     sql.close()
#     create_sql()

# 原来 id INT AUTO_INCREMENT PRIMARY KEY, 不自增 已解决
def create_sql():
    conn = sqlite3.connect('./user_data.db')
    cursor = conn.cursor()
    sql = '''create table user(
            id integer primary key autoincrement,  
            username text,
            password text,
            links text)'''
    cursor.execute(sql)
    cursor.close()


# def add_data():
#     input_username = input("please input your username")
#     input_password = input("please input your password")
#     input_links = input("please input your links")
#
#     sql = sqlite3.connect("user_data.db")
#     sql.execute("insert into user(username,password,links) values(?,?,?)",
#                 (input_username, input_password, input_links))
#     sql.commit()
#     print("add username, password and links ok")
#     sql.close()
def add_data(username, password, links):
    flag1 = 1
    flag2 = 1
    alldata = showall()
    for i in alldata:
        allusers = i[1]
        if username.lower() in [allusers.lower() for j in allusers]:
            print("用户已存在，请输入别的用户名。")
            flag1 = 0
        else:
            print("该用户名可以使用。")
            flag2 = 1

    if flag1 & flag2:
        print('kkk')
        sql = sqlite3.connect("user_data.db")
        sql.execute("insert into user(username,password,links) values(?,?,?)",
                    (username, password, links))
        sql.commit()
        print("add username, password and links ok")
        sql.close()
        return True
    else:
        print('ooo')
        return False



# # 只能一个字母 ("DELETE FROM person WHERE personid = ?",
# #                 new String[]{id});
# def add_links():
#     input_links = input("please input links")
#     input_id = input("please input id")
#
#     sql = sqlite3.connect("user_data.db")
#     sql.execute("insert into user(links) values(?) where id = (?)",
#                 (input_links, input_id))
#     sql.commit()
#     print("add links ok")
#     sql.close()
# def add_links():
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#
#     while True:
#         input_links = input("please input links")
#         # '''insert语句 把一个新的行插入到表中'''
#         sql = ''' insert into user
#               (links)
#               values
#               (:input_links)'''
#         # 把数据保存到name username和 id_num中
#         cursor.execute(sql, {'links': input_links})
#         conn.commit()
#         cont = ('Another student? ')
#         if cont[0].lower() == 'n':
#             break
#     cursor.close()

# sql='select content from article where content_id='+str(ids)
def showall():
    sql = sqlite3.connect("user_data.db")
    links = sql.execute("select * from user").fetchall()
    sql.close()
    return links


def get_links():
    sql = sqlite3.connect('user_data.db')
    input_username = input("please input your username who you want its links")
    data = sql.execute("select links from user where username='%s'" % str(input_username)).fetchone()
    sql.close()
    return data


# plus de 3 chars, les chiffres sont autorisés mais pas les  caractères spéciaux
# def verify_user():


### test
# create_sql()
print("""
1:增加用户
2:获得指定用户链接
3.显示全部表格
q:退出
""")
while 1:
    option = None
    cho = input('选择您想要的进行的操作:')
    if cho == '1':
        add_data('builhjl777',2,3)
    elif cho == '2':
        links = get_links()
        print(links)
    elif cho == '3':
        data = showall()
        print(data)
    elif cho == 'q':
        break
    else:
        "输入错误"
