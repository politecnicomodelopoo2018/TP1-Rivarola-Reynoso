import pymysql

class DB(object):

    def run (self,query):
            db = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="alumno",
                                 db="classicmodels",
                                 charset="utf8",
                                 autocommit=True)

            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            cursor_fetcheado = cursor.fetchall()
            db.close()
            return cursor_fetcheado




