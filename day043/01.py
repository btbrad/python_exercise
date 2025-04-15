import pymysql

class DBUtil:

    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '123456',
        'database': 'test',
        'charset': 'utf8'
    }

    def __init__(self):
        self.connection = pymysql.connect(**DBUtil.config)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:  
            self.connection.close()    

    def exeDML(self, sql, *args):
        try:
            count = self.cursor.execute(sql, args)
            self.connection.commit()
            return count
        except Exception as e:
            print(e)
            if self.connection:
                self.connection.rollback()
        finally:
            self.close()        

    def queryOne(self, sql, *args):
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close()
    
    def queryAll(self, sql, *args):
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()
    
if __name__ == '__main__':
    dbUtils = DBUtil()
    sql = "select * from employees"
    result = dbUtils.queryAll(sql)
    for row in result:
        print(row)