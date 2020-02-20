import pytest

from db import db
from Model import Status
from Model import Budget_Manager


@pytest.fixture()
def amount():
    return 1000


@pytest.fixture
def date():
    return '202002'


def test_add_budget_create(date, amount):
    budget_manager = Budget_Manager()
    budget_manager.db.reset_budget_table()

    assert Status.Create == budget_manager.Add_budget(date, amount)


def test_add_budget_update(date, amount):
    budget_manager = Budget_Manager()
    budget_manager.db.reset_budget_table()
    # insert first
    budget_manager.db.insert_budget(date, 10)

    assert Status.Update == budget_manager.Add_budget(date, amount)


def test_verify_data_insert(date, amount):
    db.reset_budget_table()
    db.insert_budget(date, amount)
    assert db.is_budget_exists(date)


def test_get_all_exists_one_data():
    db.reset_budget_table()
    db.insert_budget('202002', 31)
    assert db.Get_All() == {202002: 31}


def test_get_all_exists_multiple_data():
    db.reset_budget_table()
    db.insert_budget('202002', 450)
    db.insert_budget('202003', 500)
    db.insert_budget('202005', 550)
    assert db.Get_All() == {202002: 450, 202003: 500, 202005: 550}
