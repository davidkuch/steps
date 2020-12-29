import psycopg2
import credentials
# attention: cor/con.close()?---


class DbManager:
    def __init__(self):
        self.con = psycopg2.connect(credentials.creds)
        print("connected to db")
        self.cur = self.con.cursor()

    def end(self):
        self.con.commit()
        self.con.close()

    def make_db(self):
        self.cur.execute('CREATE TABLE test1 ('
                    'name varchar(35) primary key,'
                    'age integer,'
                    'score integer)')
        self.end()
        print("db created")

    def read_db(self):
        self.cur.execute('select * from test1')
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.end()

    def save_result(self, iname, iage, iscore):
        self.cur.execute(f"insert into test1 (name, age , score) values('{iname}',{iage},{iscore});")
        self.end()
        print("data added")
