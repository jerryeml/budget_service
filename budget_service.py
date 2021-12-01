# Spec 
# 202004 的預算是 30萬  查詢4月1號 會回傳1萬
# by天的預算 金額是int
# 假設一個月 三十萬 查詢一天 回傳一萬
# 輸入查詢日期(date) 回傳預算

from monthdelta import monthdelta
from datetime import date
import datetime
from calendar import monthrange


class IBudgetReoo:
    def get_all() -> list:
        pass


class BudgetService(IBudgetReoo):
    def __init__(self) -> None:
        self.budgets = []
        self.current_v = 0

    def query_same_month_range(self, start_date, end_date):
        days = -1
        for budget in self.budgets:
            print(f'key: {budget.year_month}, value: {budget.amount}')
            year = str(start_date)[:4]
            month = str(start_date)[5:7]
            days = monthrange(int(year), int(month))[1]
            print('Number of days: {}'.format(days))
            if year == budget.year_month[:4] and month == budget.year_month[4:6]:
                self.current_v = budget.amount
            # get month budget
        diff = (end_date - start_date).days
        if days < 0 or diff < 0:
            return 0
        print(f"diff: {diff}")
        result = (diff + 1) * self.current_v // days
        return result

    def get_interval_months(self, start, end):
        keys = []
        cur_date = start + monthdelta(1)
        lookup = {}

        for b in self.budgets:
            lookup[b.year_month] = b.amount

        while cur_date < date(end.year, end.month, 1):
            keys.append(str(cur_date)[0:4] + str(cur_date)[5:7])
            cur_date = cur_date + monthdelta(1)

        total = 0
        for x in keys:
            if x in lookup:
                total += lookup[x]
        return total

    def query(self, start_date, end_date) -> float:

        if end_date < start_date:
            return 0
        start_end_date = date(start_date.year, start_date.month + 1, 1) - datetime.timedelta(days=1)
        end_start_date = date(end_date.year, end_date.month, 1)

        if start_date.year == end_date.year and start_date.month == end_date.month:
            return self.query_same_month_range(start_date, end_date)

        start_month_budget = self.query_same_month_range(start_date, start_end_date)
        interval_month_budget = self.get_interval_months(start_date, end_date)
        end_date_budget = self.query_same_month_range(end_start_date, end_date)

        return start_month_budget + interval_month_budget + end_date_budget

    def get_all(self, budgets) -> list:
        self.budgets = budgets
        return self.budgets


if __name__ == "__main__":
    pass
