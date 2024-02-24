
import psycopg2 as py
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, typ):
        db = py.connect(
            database=os.getenv('DB_NAME'),
            host=os.getenv("DB_HOST"),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        cursor = db.cursor()
        cursor.execute(query)
        datas = ['create', 'insert', 'update', 'delete']
        if typ in datas:
            if typ == 'create':
                db.commit()
                return 'created successful'
            elif typ == 'insert':
                db.commit()
                return 'insert successful'
            elif typ == 'update':
                db.commit()
                return 'update successful'
            else:
                db.commit()
                return 'delete successful'
        elif typ == 'select':
            return cursor.fetchall()


