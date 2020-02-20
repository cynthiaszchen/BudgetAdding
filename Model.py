from db import BudgetRepo
import datetime
import calendar

class Status:
    Create = "Create Success"
    Update = "Update Success"
    MonthErr = "Error: Month should be between 1~12"
    AmountIsNegative = "Error: Amount should not be negative value"

class Budget_Manager:

    def __init__(self):
        self.db = BudgetRepo()


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

        total_amount = 0.00

        if not BudgetDict:
            return total_amount

        budget_per_day_dict = {}

        for year_month in BudgetDict:
            month_budget = BudgetDict[year_month]
            year_month = str(year_month)
            year = int(year_month[0: 4])
            month = int(year_month[4:6])
            days_of_month = calendar.monthrange(year, month)[1]

            budget_per_day = month_budget / days_of_month
            budget_per_day_dict[year_month] = budget_per_day

        for dt in daterange(Start, End):
            year_month = dt.strftime('%Y%m')
            if year_month not in budget_per_day_dict:
                continue
            total_amount += budget_per_day_dict[year_month]

        return total_amount


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)