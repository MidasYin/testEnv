# -*- coding:UTF-8 -*-
import time
import os
import psycopg2
import Model.config as config
import platform

class requestSQL(object):
    # init
    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/configure/sqlconf.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        print(path)
        cr = config.Configure(path)
        self.conn = psycopg2.connect(
            host=cr.Get('SQL', 'ip'),
            port=cr.Get('SQL', 'port'),
            user=cr.Get('SQL', 'user'),
            password=cr.Get('SQL', 'password'),
            database=cr.Get('SQL', 'db')
        )
        self.cursor = self.conn.cursor()

    # 须是完整的SQL语句
    def sql_exe(self, sql):
        self.cursor.execute(sql)

    # INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
    def insert(self, tbName, field, values):
        insSql = "insert into %s(%s)values %s" % (tbName, field, values)
        return self.execute(insSql)

    # select (self,表，列，where)
    def select(self, tbName, field='*', where=''):
        if where:
            where = " where "+where
        selSql = "select %s from %s %s" % (field, tbName, where)
        return self.execute(selSql)

    # UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
    def update(self, keyValues, tbName, where):
        setValue = ''
        for k,v in keyValues.items():
            setValue += '`%s`="%s",' % (k, v)
        if where:
            where = " where "+where
        updateSql = "update %s set %s %s" % (tbName, setValue[:-1], where)
        return self.execute(updateSql)

    # DELETE FROM 表名称 WHERE 列名称 = 值
    def delete(self,tbName, where):
        if where:
            where = " where "+where
        delSql = "delete from %s %s" % (tbName,where)
        return self.execute(delSql)

    # execute
    def execute(self, sql):
        try:
            if sql.find('select') != -1:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            elif sql.find('insert') != -1 or sql.find('update') != -1 or sql.find('delete') != -1:
                self.cursor.execute(sql)
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '--' + str(e))
            return False

    # __del__
    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    # requestSQL = requestSQL()
    # re = requestSQL.execute('''select * FROM "user" where login_name = 'lj-biao-yin';''')
    # print(re)
    pass
