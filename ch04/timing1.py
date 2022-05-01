# @@range_begin(list1)
# from timeit import timeit

# setup = 'from datetime import datetime'  # <1>
# statement = 'datetime.now()'  # <2>
# result = timeit(setup=setup, stmt=statement, number=1000)  # <3>
# print(f'実行時間の平均： {result / 1000}s == {result}ms')
# @@range_end(list1)

from timeit import timeit

setup = "def check_300(items): return 300 in items"
result = timeit(setup=setup, stmt="check_300(list(range(10000)))", number=1000)
print(f"実行時間の平均：{result / 1000}s == {result}ms")
