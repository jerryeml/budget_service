
import pytest
from datetime import date
from budget_service import BudgetService

def setup():
    b = BudgetService()
    return b

def test_query_one_day():
    b = setup()
    mock_budget = [("202006", 30)]

    budget = b.get_all(mock_budget)
    
    start_date = date(2020,6,1)
    end_date = date(2020,6,1)
    result = b.query(start_date, end_date)
    assert result == 1
