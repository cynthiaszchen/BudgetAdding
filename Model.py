from db import BudgetRepo
import datetime

class Status:
    Create = "Create Success"
    Update = "Update Success"
    MonthErr = "Error: Month should be between 1~12"
    AmountIsNegative = "Error: Amount should not be negative value"

class Budget_Manager:

    Day_Budget_List = []

    def __init__(self):
        self.db = BudgetRepo()
        return

    def Add_budget(self, Date, Amount):
        if int(Date[-2:]) > 12 or int(Date[-2:]) < 1:
            return Status.MonthErr
        if int(Amount) < 0:
            return Status.AmountIsNegative

        if self.db.is_budget_exists(Date) is True:
            self.db.replace_budget(Date, Amount)
            return Status.Update
        else:
            self.db.insert_budget(Date, Amount)
            return Status.Create

    def totalAmount(self, Start:datetime.datetime , End:datetime.datetime):
        BudgetDict = self.db.Get_All( )

        if not BudgetDict:
            return 0.00

        #for budget in BudgetDict:
        #    Day_Budget_List.append()


        if BudgetDict[int(Start.strftime('%y%m'))]:
            return BudgetDict[int(Start.strftime('%y%m'))]

        return 0.00

