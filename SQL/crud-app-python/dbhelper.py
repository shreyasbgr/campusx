import mysql.connector

class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = "localhost",user="root",password="",database="hit-db-demo")
            self.cursor = self.conn.cursor()
        except:
            print("Some error occured")
        else:
            print("Connected to database")

    def register(self,name,email,password):
        try:
            self.cursor.execute("""
            INSERT INTO `user` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    
    def search(self,email,password):
        self.cursor.execute("""
        SELECT * FROM `user` WHERE `email` LIKE '{}' AND `password` LIKE '{}'
        """.format(email,password))
        data = self.cursor.fetchall()
        return data