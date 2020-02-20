import pytest
import datetime
from Model import Budget_Manager

@pytest.fixture
def budget_manager():
    budget_manager = Budget_Manager()
    budget_manager.db.reset_budget_table()
    budget_manager.Add_budget('202002', 29)
    budget_manager.Add_budget('202003', 62)

    return budget_manager


def test_one_whole_month(budget_manager):
    start_date = datetime.datetime(2020, 2, 1)
    end_date = datetime.datetime(2020, 2, 29)
    total_amount = budget_manager.totalAmount(start_date, end_date)
    assert total_amount == 29