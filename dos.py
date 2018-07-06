import pymysql

class DB(object):

    def run (query):
            db = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="alumno",
                                 db="classicmodels",
                                 charset="utf8",
                                 autocommit=True)

            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            db.close()
            return cursor



