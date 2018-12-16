# -*- encoding:utf-8 -*-
__author__ = ''
import pymysql


class SqlCon():
    def __init__(self, host="localhost", user="root", password="lyh123", db_name=""):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def connect(self):
        try:
            self.db = pymysql.connect(self.host, self.user, self.password, self.db_name)
            self.cursor = self.db.cursor()
            print("database connect success!")
        except:
            print("database connect failed!")

    def run(self, _sql):
        res = self.cursor.execute(_sql)
        self.db.commit()
        return res

    def runfetchone(self, _sql):
        self.cursor.execute(_sql)
        return self.cursor.fetchone()

    def update_many(self, _sql, val):
        res = self.cursor.executemany(_sql, val)
        if res:
            self.db.commit()
        else:
            self.db.rollback()
        return res

    def runfetchmany(self, _sql, size=1):
        self.cursor.execute(_sql)
        return self.cursor.fetchmany(size)

    def runfetchall(self, _sql):
        self.cursor.execute(_sql)
        return self.cursor.fetchall()

    def dbclose(self):
        try:
            self.db.close()
            print("database close success!")
        except:
            print("database close failed")


if __name__ == "__main__":
    sqln = SqlCon(db_name="school")
    sqln.connect()
    print(sqln.runfetchall("select * from student"))
    sqln.dbclose()
