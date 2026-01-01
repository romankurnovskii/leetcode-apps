from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        table_orders = defaultdict(lambda: defaultdict(int))

        for _, table, food in orders:
            foods.add(food)
            table_orders[int(table)][food] += 1

        foods = sorted(foods)
        tables = sorted(table_orders.keys())

        res = [["Table"] + foods]
        for table in tables:
            row = [str(table)]
            for food in foods:
                row.append(str(table_orders[table][food]))
            res.append(row)

        return res
