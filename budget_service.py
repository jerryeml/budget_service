# Spec 
# 202004 的預算是 30萬  查詢4月1號 會回傳1萬
# by天的預算 金額是int
# 假設一個月 三十萬 查詢一天 回傳一萬
# 輸入查詢日期(date) 回傳預算
from datetime import date
from calendar import monthrange


class IBudgetReoo:
    def get_all() -> list:
        pass


class BudgetService(IBudgetReoo):
    def __init__(self) -> None:
        self.budgets = []
        self.current_v = 0

    def query(self, start_date, end_date) -> float:

        days = -1

        lookup = {}

        for budget in self.budgets:
            print(f'key: {budget.year_month}, value: {budget.amount}')
            year = str(start_date)[:4]
            month = str(start_date)[5:7]
            days = monthrange(int(year), int(month))[1]
            print('Number of days: {}'.format(days))
            if year == budget.year_month[:4] and month == budget.year_month[4:6]:
                lookup[budget.year_month] = budget.amount
                # self.current_v = budget.amount

        # get month budget
        diff = (end_date - start_date).days
        if days < 0 or diff < 0:
            return 0
        print(f"diff: {diff}")
        result = (diff + 1) * self.current_v // days
        return result

    def get_all(self, budgets) -> list:
        self.budgets = budgets
        return self.budgets


if __name__ == "__main__":
    pass
