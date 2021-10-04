import psycopg2
from sqlalchemy import create_engine


class Dbload:
    def __init__(self, password, host):
        self.password = password
        self.host = host
        self.tablename = 'YoutubeData'
        self.engine = create_engine(f"postgresql+psycopg2://postgres:{password}@{host}:5432/postgres")
        self.conn = psycopg2.connect(f"dbname=postgres user=postgres password={password} host=3.21.144.229 port=5432")

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS YoutubeData")
        cursor.execute(
            "CREATE TABLE YoutubeData (title VARCHAR(255), description VARCHAR(500), hash_tags VARCHAR(30), "
            "views VARCHAR(30), comments VARCHAR(20000))")
        self.conn.commit()

    def read_table(self, tbl):
        self.engine.execute(f'''SELECT * FROM {tbl}
            LIMIT 20''').fetchall()


if __name__ == '__main__':
    sv = Dbload('Oladayo120!', '3.21.144.229')
    sv.create_table()
