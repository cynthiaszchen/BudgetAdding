from pathlib import Path
import sqlite3


DATABASE_DIR = Path("database/db.db")
DATABASE_DIR.parent.mkdir(exist_ok=True, parents=True)
DATABASE_URI = str(DATABASE_DIR.absolute())

class BudgetRepo:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_URI, check_same_thread=False)
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

    def search_budget(self, date):
        sql = """
        SELECT date, amount FROM Budget
        WHERE date = ?
        """

        return self.cursor.execute(sql, (date,))

    def is_budget_exists(self, date):
        cursor = self.search_budget(date)
        found = False
        for row in cursor:
            found = True
            break

        return found

    def replace_budget(self, date, amount):
        sql = """
        UPDATE Budget SET amount = ? WHERE date = ?
        """

        self.cursor.execute(sql, (amount, date))
        self.conn.commit()

    def Get_All(self):
        sql = """
        SELECT date, amount FROM Budget 
        """

        date_amount_dict = {}

        for row in self.cursor.execute(sql).fetchall():
            date = int(row[0])
            amount = int(row[1])
            date_amount_dict[date] = amount

        return date_amount_dict


db = BudgetRepo()
db.reset_budget_table()




