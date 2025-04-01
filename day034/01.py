import mysql.connector

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'rootpassword',
    'database': 'vsearchlogdb'
}


class UseDataBase:

    def __int__(self) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'rootpassword',
        'database': 'vsearchlogdb'
    }
    with UseDataBase() as cursor:
        print(cursor)
