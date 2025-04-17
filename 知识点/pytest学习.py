"""
（1）测试文件以test_开头（以_test结尾也可以），注意：pytest 文件名.py不受此规则限制。

（2）测试类以Test开头，并且不能带有 __init__ 方法

（3）测试函数以test_开头

（4）断言使用基本的assert即可
"""
"""
Pytest Exit Code 含义清单

Exit code 0 所有用例执行完毕，全部通过
Exit code 1 所有用例执行完毕，存在Failed的测试用例
Exit code 2 用户中断了测试的执行
Exit code 3 测试执行过程发生了内部错误
Exit code 4 pytest 命令行使用错误
Exit code 5 未采集到可用测试用例文件
"""