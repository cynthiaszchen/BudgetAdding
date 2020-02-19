from pathlib import Path
import sqlite3


#DATABASE_URI = 'sqlite:///db.db'

DATABASE_DIR = Path("db/db.db")
DATABASE_DIR.parent.mkdir(exist_ok=True, parents=True)
DATABASE_URI = str(DATABASE_DIR.absolute())
#DATABASE_URI = 'D:\Cynthia\Study\TestableCode\Lab\BudgetAdding\db.db'

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_URI)
        self.cursor = self.conn.cursor()

    def create_budget_table(self):
        sql = """
        CREATE TABLE "Budget" (
            "Date"	INTEGER NOT NULL UNIQUE,
            "Amount"	NUMERIC NOT NULL,
            PRIMARY KEY("Date")
        );
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_budget_table(self):
        sql = """
        DROP TABLE IF EXISTS "Budget";
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def reset_budget_table(self):
        self.delete_budget_table()
        self.create_budget_table()

    def insert_budget(self, date, amount):
        sql = """
        INSERT INTO Budget (date, amount)
              VALUES(?,?) 
        """

        self.cursor.execute(sql, (date, amount))
        self.conn.commit()

if __name__ == '__main__':
    db = Database()
    db.reset_budget_table()
    db.insert_budget("202002", 10000)

    #engine = create_engine('sqlite:///budget.db', echo=True)
    #cus = engine.connect()
    #sql = ("create table budget (id integer primary key,yearmonth integer UNIQUE,amount integer)")
    #cus.execute(sql)
    #cus.close()


