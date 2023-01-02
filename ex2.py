import sqlite3
import re


def create_sql():
    conn = sqlite3.connect('./user_data1.db')
    cursor = conn.cursor()
    sql = '''create table user(
            id integer primary key autoincrement,  
            username text,
            password text,
            links text)'''
    cursor.execute(sql)
    cursor.close()


def add_data(username, password, links):
    flag1 = 1
    flag2 = 1
    alldata = showall()

    # Determine whether the username is unique, that is, whether it already exists in the table
    for i in alldata:
        allusers = i[1]
        if username.lower() in [allusers.lower() for j in allusers]:
            print("Username already exists, adding failed")
            flag1 = 0
        else:
            print("Username has been added successfully")
            flag2 = 1

    # add username, password and links
    if flag1 & flag2:
        sql = sqlite3.connect("user_data1.db")
        sql.execute("insert into user(username,password,links) values(?,?,?)",
                    (username, password, links))
        sql.commit()
        # print("add username, password and links ok")
        sql.close()
        return True
    else:
        return False


def get_links(username):
    sql = sqlite3.connect('user_data1.db')
    links = sql.execute("select links from user where username='%s'" % str(username)).fetchone()
    sql.close()
    return links


def showdate(username):
    sql = sqlite3.connect('user_data1.db')
    data = sql.execute("select * from user where username='%s'" % username).fetchone()
    sql.close()
    return data


def showall():
    sql = sqlite3.connect("user_data1.db")
    data = sql.execute("select * from user").fetchall()
    sql.close()
    return data


# Check if username and password match
def verify_match(username, password):
    data = showdate(username)
    if data:
        if data[2] == password:
            print("password vrai")
            return True
        else:
            print("password faux")
    else:
        print("user n'exite pas")


# plus de 3 chars, les chiffres sont autorisés mais pas les  caractères spéciauxs
def verify_username():
    alldata = showall()
    flag = 0
    for i in alldata:
        allusers = i[1]
        # print(allusers)
        # print(len(allusers))
        # if len(allusers) >= 3:
        if allusers.isalnum() & (len(allusers) >= 3):
            flag = 0
            # print('okk')
        else:
            # Count the number of wrong names
            flag = flag + 1
            # print('aaaaaaaaaaaaaaaaaa')
    # print('-----')
    # print(flag)

    if flag != 0:
        print('%d usernames are in the wrong format' % flag)
        return False
    else:
        return True


# composé de 8 chars minimum contenant au moins une majuscule,
# au moins  un caractère spécial, et au moins un chiffre et au moins 1 caractère standard
def verify_password():
    alldata = showall()
    flag = 0
    pattern = r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*,\.])[0-9a-zA-Z!@#$%^&*,\\.]{8,}$'
    for i in alldata:
        allpassword = i[2]
        # print(allpassword)
        # print(len(allusers))
        res = re.search(pattern, allpassword)
        # # print(res)
        # if res:
        #     print(11111111111)
        # else:
        #     print('ggggg')
    return True if res else False


def verify_links():
    alldata = showall()
    flag = 0
    for i in alldata:
        alllinks = i[3]
        # print(alllinks)
        # print(len(allusers))
        if alllinks.isalnum() & alllinks.islower():
            flag = 0
            # print('okkkk')
        else:
            flag = flag + 1
            # print('nononononononoonon')

    if flag != 0:
        print('%d links are in the wrong format' % flag)
        return False
    else:
        return True

# check that the database is not corrupted
def verify_rules():
    return verify_username() & verify_password() & verify_links()






# test
# create_sql()
# add_data('Lsbduiew#$5WGc88', 'Bksdnwi*&/', 'BKJKSw8294u/?+')
# add_data('w','e','r')
# add_data('dfga3849','Aa1234567890.com.cn','ef')
# add_data('º¶','d','d')
alldata = showall()
print(alldata)
# for i in alldata:
#     allusers = i[2]
#     print(allusers)
#
# verify_password('aaaa')
# if (verify_password() == True):
#     print("yeh1")
#
# if (verify_password()==False):
#     print("yeh2")
#
# if (verify_password('Aa1234567890.com.cn')):
#     print("yeh3")
#
# # print(data[3][2])
# print(len(data))
# for i in data:
#     #allusers = data[1]
#     #print(allusers)
#     #print(i)
#     allusers = i[1]
#     print(allusers)
#
# print('-----------------')
# verfy_username()
