salary_first = {"Lisa": 238900, "Ganesh": 8765000, "John": 3450000}
salary_second = {"Albert": 3456000, "Arya": 987600}
salary = salary_first.copy()
salary.update(salary_second)
# >>> {"Lisa": 238900, "Ganesh": 8765000, "John": 345000, "Albert": 3456000, "Ary": 987600}
