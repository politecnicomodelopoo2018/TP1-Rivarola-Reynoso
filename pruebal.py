import pymysql

db= pymysql.connect(host="localhost", user= "root", passwd= "alumno", db="prueba", charset="utf8", autocommit=True)

inserts = db.cursor()



inserts.execute("update empleados set nombre='Lanata' where id_empleado='1'")



db.close()