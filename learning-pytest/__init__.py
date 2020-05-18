

# pytest 执行时使用 -s 阻止消息被吞 pytest -s

# 第一种，显式指定函数名，通过 :: 标记。pytest tests/test-function/test_no_mark.py::test_func1

# 第二种，使用模糊匹配，使用 -k 选项标识。 pytest -k func1 tests/test-function/test_no_mark.py

# 运行测试时使用 -m 选项可以加上逻辑，如：
# pytest -m "finished and commit"
#
# pytest -m "finished and not merged"

# 使用 -v 执行测试  （可查看id）

# 如果想更细的跟踪固件执行，可以使用 --setup-show 选项 pytest --setup-show tests/fixture/test_db.py
