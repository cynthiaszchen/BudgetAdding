import pytest
import datetime
from Model import Budget_Manager

def create_budget_manager(bm):
    budget_manager = Budget_Manager()
    budget_manager.db.reset_budget_table()
    for yearmonth, amount in bm:
        budget_manager.Add_budget(yearmonth, amount)
    return budget_manager

def test_no_budget():
    budget_manager = create_budget_manager([])
    start_date = datetime.datetime(2020, 2, 1)
    end_date = datetime.datetime(2020, 2, 29)
    total_amount = budget_manager.totalAmount(start_date, end_date)
    assert total_amount == 0.00

def test_one_whole_budget():
    budget_manager = create_budget_manager([('202002', 29),
                                            ('202003', 62)])
    start_date = datetime.datetime(2020, 2, 1)
    end_date = datetime.datetime(2020, 2, 29)
    total_amount = budget_manager.totalAmount(start_date, end_date)
    assert total_amount == 29.00

def test_one_day_budget():
    budget_manager = create_budget_manager([('202003', 31000)])
    start_date = datetime.datetime(2020, 3, 1)
    end_date = datetime.datetime(2020, 3, 1)
    total_amount = budget_manager.totalAmount(start_date, end_date)
    assert total_amount == 1000.00

def test_two_whole_month_budget():
    budget_manager = create_budget_manager([('201901', 930),
                                            ('201902', 280)])
    start_date = datetime.datetime(2019, 1, 1)
    end_date = datetime.datetime(2019, 2, 28)
    total_amount = budget_manager.totalAmount(start_date, end_date)
    assert total_amount == 1210.00

def test_cross_month_one_month_no_budget():
    budget_manager = create_budget_manager([('202001', 310)])
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2020, 2, 14)
    total_amount = budget_manager.totalAmount(start_date, end_date)
    assert total_amount == 310.00
