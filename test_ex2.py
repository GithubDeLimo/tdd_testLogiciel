import sqlite3
import unittest
from ex2 import create_sql, add_data, get_links, showall, verify_match, verify_username, verify_password, \
    verify_links, verify_rules

conn = sqlite3.connect('./user_data1.db')
cursor = conn.cursor()


class Test_ex1(unittest.TestCase):
    def test1_create_sql(self):
        cursor.execute('drop table if exists user;')
        create_sql()
        username = ''
        sql = "select * from user;"
        for row in cursor.execute(sql).fetchall():
            username = row[0]
        self.assertEqual(username, '')


    def test2_add_data(self):
        add_data('yolaine12', 'Lm23004x!111', 'www.google.fr')
        sql = "select username from user where username ='yolaine12';"
        username = ''
        for row in cursor.execute(sql):
            username = row[0]
        self.assertEqual(username, 'yolaine12')

        sql = "select password from user where username ='yolaine12';"
        password = ''
        for row in cursor.execute(sql):
            password = row[0]
        self.assertEqual(password, 'Lm23004x!111')

        sql = "select links from user where username ='yolaine12';"
        links = ''
        for row in cursor.execute(sql):
            links = row[0]
        self.assertEqual(links, 'www.google.fr')


    def test3_get_links(self):
        sql = "select links from user where username ='yolaine12';"
        links = ''
        for row in cursor.execute(sql):
            links = row[0]
            print(links)
        self.assertEqual((links,), get_links('yolaine12'))


    def test4_showall(self):
        sql = "select * from user;"
        for row in cursor.execute(sql).fetchall():
            alldata = row
        self.assertEqual([alldata], showall())


    def test5_verify_match(self):
        add_data('benoit6', 'Lsidjew*&&6dc', 'www.f98jue.com')
        add_data('an1343n', 'UDIW8w29;s!', 'fhiw938fh9.daf')
        add_data('barbara', '(jei#Tvc24', 'http://www.ahufdy288tr74f.com')

        self.assertTrue(verify_match('benoit6', 'Lsidjew*&&6dc'))
        self.assertTrue(verify_match('an1343n', 'UDIW8w29;s!'))
        self.assertFalse(verify_match('barbara', '666'))


    def test6_verify_username(self):
        # 'ar' and 'å¨√∫∆†ƒ' are in the wrong format
        add_data('ar', 'sahe(dh92', '28hsafbke.de')
        add_data('å¨√∫∆†ƒ', '˙ˆˆ´´ç∑œ£∞', '´¨¨øœœ≈ç∫µå¡')

        self.assertFalse(verify_username())

    def test7_verify_password(self):
        add_data('uhei87', '12', 'Apple.com')
        self.assertFalse(verify_password())

    def test8_verify_links(self):
        self.assertFalse(verify_links())


    def test9_verify_rules(self):
        self.assertFalse(verify_rules())




if __name__ == '__main__':
    unittest.main()
    conn.commit()
    conn.close()
