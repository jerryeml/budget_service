import unittest

from datetime import date
from budget_service import BudgetService


class Budget:
    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.b = BudgetService()

    def test_query_one_day(self):
        mock_budget = [Budget('202006', 30)]
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 1)

    def test_query_one_day_without_db_data(self):
        mock_budget = []
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 0)

    def test_query_one_day_when_year_month_budget_is_zero(self):
        mock_budget = [Budget('202006', 0)]
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 0)

    def test_query_cross_days_same_month(self):
        mock_budget = [Budget('202006', 30)]
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 30)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 30)

    def test_query_invalid_cross_days(self):
        mock_budget = [Budget('202006', 30)]
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 6, 30)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 0)

    def test_query_cross_month(self):
        mock_budget = [Budget('202005', 31), Budget('202006', 60)]
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 5, 31)
        end_date = date(2020, 6, 2)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 5)

    def test_query_cross_month(self):
        mock_budget = [Budget('202005', 31), Budget('202006', 60), Budget('202007', 90)]
        budget = self.b.get_all(mock_budget)
        start_date = date(2020, 5, 31)
        end_date = date(2020, 6, 2)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 5)
