from db import Database

class Status:
    Create = "Create Success"
    Update = "Update Success"
    MonthErr = "Error: Month should be between 1~12"
    AmountIsNegative = "Error: Amount should not be negative value"

class Budget_Manager:
    def __init__(self):
        self.db = Database()
        return

    def Add_budget(self, Date, Amount):
        if Date[-2:] > 12 or Date[-2:] < 1:
            return Status.MonthErr
        if Amount < 0:
            return Status.AmountIsNegative

        if Database.is_budget_exists(str(Date)) is True:
            Database.replace_budget(str(Date), str(Amount))
            return Status.Update
        else:
            Database.insert_budget(str(Date), str(Amount))
            return Status.Create

    def totalAmount(self, Start, End):
        return 0.00