# Spec 
# 202004 的預算是 30萬  查詢4月1號 會回傳1萬
# by天的預算 金額是int
# 假設一個月 三十萬 查詢一天 回傳一萬
# 輸入查詢日期(date) 回傳預算


class IBudgetReoo:
    def get_all() -> list:
        pass


class BudgetService(IBudgetReoo):
    def __init__(self) -> None:
        pass

    def query(self, start_time, end_time) -> float:
        pass

    def get_all(budgets) -> list:
        return budgets