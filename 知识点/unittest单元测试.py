#unittest
"""
单元测试框架，主要用于单元测试，具备编写用例，组织用例，执行用例，输出报告等作用
test case:自动化测试用例，一个testcase的实例就是一个测试用例
test suite:测试套件，是多个测试用例的集合
testLoader：加载器，用于加载TestCase到TestSuite,其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase,创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例
test runner:执行测试，并将测试结果保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少
test fixture:测试夹具，一个测试用例的初始化准备和环境还原，主要包含setUp()和setDown()方法

工作原理
    编写TestCase完成
    由TestLoader加载到TestCase到TestSuite
    然后TextTestRunner来运行TestSuite
    最后将运行的结果保存再TextTestResult

"""
#testcase
"""
包括测试前准备环境的搭建(SetUP)、实现测试过程的代码(run)，以及测试后环境的还原(tearDown)。

导入unittest 包
实例化一个类 
将类继承于unittest.TestCase

创建用例需要test开头
setUp（）是测试用例执行前的环境准备
teatDown（）是测试用例执行结束后的环境恢复
每个测试用例都会执行setUp()和tearDown()
"""

#断言
"""
self.assertxxx()
测试中，断言一般用于将实际结果与预期结果对比，结果一致返回true，结果不一致返回false。
常用断言方法
assertEqual(a, b)	a == b
assertNotEqual(a, b)	a != b

assertTrue(x)	bool(x) is True
assertFalse(x)	bool(x) is False

assertIs(a, b)	a is b
assertIsNot(a, b)	a is not b

assertIsNone(x)	x is None
assertIsNotNone(x)	x is not None

assertIn(a, b)	a in b
assertNotIn(a, b)	a not in b

assertIsInstance(a, b)	isinstance(a, b)
assertNotIsInstance(a, b)	not isinstance(a, b)

assertGreater(a,b)  a>b
assertGreaterEqual(a,b)  a>=b

assertLess(a,b)   a<b
assertLessEqual(a,b)   a<=b

assertSameElement  忽略顺序判断元素相同

判断顺序、元素相同
assertSequenceEqual 
assertDictEqual
assertSetEqual
assertListEqual
assertTupleEqual
"""


#跳过用例
"""
skip装饰器主要有3种：

unittest.skip(reason)：无条件跳过装饰的用例，并返回跳过的原因reason。
unittest.skipIf(condition,reason)：condition条件为真时，跳过装饰的用例，并返回跳过的原因reason。
unittest.skipUnless(condition,reason):condition条件为假时，跳过装饰的用例，并返回跳过的原因reason。
注：condition表示满足condition条件下则跳过该用例，reason表示跳过的原因。
"""

#TestSuit
"""
解决用例执行顺序的问题，让用例按配置的顺序执行
解决用例在多个py文件中分散的问题，将所需用例收集、汇总
"""

#test loader
"""
TestLoader（测试加载）一般被用来创建测试套件和搜集testcase，将搜集的testcase添加到testsuit中执行。
unittest.TestLoader().loadTestsFromTestCase(testCaseClass)	根据testcase类名寻找用例
unittest.TestLoader().loadTestsFromModule(module, pattern=None)	根据testcase所在的文件名寻找用例
unittest.TestLoader().loadTestsFromName(name, module=None)	根据用例名称寻找用例
unittest.TestLoader().loadTestsFromNames(names,module=None)	根据多个用例名称寻找用例
unittest.defaultTestLoader.discover(start_dir, pattern=‘test*.py’,top_level_dir=None)	根据正则规则匹配路径下符合规则的文件及文件中所有的用例

defaultTestLoader.discover 的使用方法（run_all.py文件）：
unittest.defaultTestLoader.discover(start_dir, pattern=‘test*.py’,top_level_dir=None)可根据正则规则匹配路径下符合规则的文件及文件中所有的用例。start_dir：代表指定目录，一般传入存放测试用例的目录路径。从指定目录开始测试模块扫描，仅加载与模式匹配的测试文件，然后返回他们的testSuite对象。pattern：代表匹配testcase文件的规则，可根据正则匹配，默认匹配指定目录下以test开头的py文件。

注：discover()方法可自动根据测试目录start_dir 匹配查找测试用例文件 test*.py ，并将查找到的测试用例组装到测试套件，因此可以直接通过 run() 方法执行 discover
"""

#test runner
"""
test runner（测试运行器）主要用来运行test case。
可配合test suit使用，执行test suit中的用例，并将测试结果保存到TextTestResult实例中。

unittet.main()	执行当前文件中的所有实例类的用例，默认按照test后首字母的ascall码顺序执行
unittest.TextTestRunner().run(test)	按照test suit中存放test case的顺序执行测试用例

runner=unittest .TextTestRunner(verbosity=0)
runner.run(suite)
verbosity ：表示测试结果的信息详细程，一共三个值，默认是1

0 (静默模式)：你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式)：非常类似静默模式 只是在每个成功的用例前面有个 . 每个失败的用例前面有个 F
2 (详细模式)：测试结果会显示每个测试用例的所有相关的信息

"""

# test Fixture
"""
测试夹具，用于测试用例环境的搭建和销毁。
即用例测试前准备环境的搭建（SetUp前置条件），测试后环境的还原（TearDown后置条件），
比如测试前需要登录获取token等就是测试用例需要的环境，运行完后执行下一个用例前需要还原环境，以免影响下一条用例的测试结果。

test fixture（测试夹具）有两种使用方式：

一种是以测试方法为维度的，分别是setUp()和setDown()
一种是以测试类为维度的，分别是：setUpClass()和tearDownClass()

类前、后置函数
只会再类的前后执行一次
需要@classmethod

"""
#参数化
"""
参数化：主要是对测试过程中的元素定位、数据进行参数化。
在自动化测试脚本的编写过程中，会需要用到数据，而数据通常是变化的、有规律的（如同：计算的公式，公式中的参数和值会变，公式本身不会变，当要对这条公式输入不同参数测试时，这时可以将参数和值进行参数化）
使用参数化可以大大减少重复的代码，提高脚本的可复用性。
2、数据驱动与关键字驱动

参数化的两种方式：

数据驱动：指同一段代码，输入不同的数据（参数），得到不同的结果（值）。如：你输入张三得到的结果是帅哥，你输入小雨得到的结果是美女。这种以数据引导代码结果的方式成为数据驱动。
关键字驱动：关键字驱动就是将数据驱动里的数据改为关键字而已，一般用于UI自动化，通过改变关键字，从而改变数据的输入位置，这就叫做关键字驱动。

3、数据驱动实例
unittest 没有自带数据驱动、关键字驱动的功能，所以使用unittest参数化时，可以使用第三方库：ddt或paramunittest，这里使用ddt做演示
"""
"""
 # 使用unittest前，需导入unittest库
import unittest
 # 导入ddt
import ddt

 # -------------------------参数化的参数-------------------
test_data = [{'username':'张三', 'psw':'123456'},
             {'username': '李四', 'psw': '321654'},
             {'username': '王五', 'psw': '654321'},]

 # ---------------------------testcase部分-------------------
 # 实例化example类，并继承于unittest.TestCase
@ddt.ddt
class example1(unittest.TestCase):
    def test_a01(self):
        print('测试用例1')

    @ddt.data(*test_data)
    def test_a02(self, data):
        print('测试用例2')
        print(data)

 # ---------------------------test runner部分-------------------
if __name__ == '__main__':
    # 执行当前文件的测试用例
    unittest.main()
"""
# 生成自动化测试报告
"""
unittest生成自动化测试报告可以使用第三方库：BeautifulReport或HTMLTestRunner

import unittest                     		# 导入unittest
from testcase.fff import example1    		# 从 testcase目录下的fff.py文件中导入example1实例类
from BeautifulReport import BeautifulReport # 导入BeautifulReport库

# -------------------------test loader部分---------------------
load_case = unittest.TestLoader().loadTestsFromTestCase(example1)   # 加载example1类下的所有用例

# ------------------------test suit部分--------------------------
suite = unittest.TestSuite()        # 构建测试套件
suite.addTest(load_case)            # 将test_cases列表添加到suite中

# ------------------------生成测试报告-----------------------------
BeautifulReport(suite).report(filename='测试报告文件名称', description='测试报告标题', report_dir='.') # report_dir='.'把report放到当前目录下


"""
# 使用unittest前，需导入unittest库
import unittest


# ---------------------------testcase部分-------------------
# 实例化example类，并继承于unittest.TestCase
class example1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类前置函数，每个测试类运行前会自动执行一次该函数")

    @classmethod
    def tearDownClass(cls):
        print('类后置函数，每个测试类运行后会自动执行一次该函数')

    def setUp(self):
        print('前置函数，每个用例运行前会自动执行一次该函数')

    def tearDown(self):
        print('后置函数，每个用例运行后会自动执行一次该函数')

    # 创建测试用例test_a01，用例需以test开头
    def test_a01(self):
        print('测试用例1')

    def test_a02(self):
        print('测试用例2')

    def test_a03(self):
        a, b = 1, 1  # 设置变量a=1,b=1
        self.assertEqual(a, b, '错误提示，a不等于b')  # 设置断言a等于b，不相等报错并输出提示文字
        print('测试用例3')
    @unittest.skipIf(1,'当1为true时，跳过test_a04用例')
    def test_a04(self):
        print('测试用例4')
"""
import unittest                     # 导入unittest
from testcase.fff import example1    # 从 testcase目录下的fff.py文件中导入example1实例类
from testcaseimport fff             # 从testcase目录下导入fff文件
"""
# 1、加载类名
# -------------------------test loader部分---------------------
load_case1 = unittest.TestLoader().loadTestsFromTestCase(example1)   # 加载example1类下的所有用例

# 2、加载模块名
# -------------------------test loader部分---------------------
load_case2 = unittest.TestLoader().loadTestsFromModule(fff)          # 加载fff.py文件下的所有用例

# 3、加载用例名称
# -------------------------test loader部分---------------------
load_case3 = unittest.TestLoader().loadTestsFromName('fff.example1.test_a01')    # 加载文件名为fff,类名为example1,用例名称为test_a01的用例

# 4、可加载多个用例名称，括号内为列表
# -------------------------test loader部分---------------------
load_case = unittest.TestLoader().loadTestsFromNames(['fff.example1.test_a01']) # 加载列表内文件名为fff,类名为example1,用例名称为test_a01的用例

# 5、正则规则匹配路径
"""
import unittest                     # 导入unittest
from static.fff import example1    # 从 testcase目录下的fff.py文件中导入example1实例类
from static import fff             # 从static目录下导入fff文件
import os 

current_directory_path = os.getcwd()    # 获取当前目录的路径,因为用例fff.py文件存放在当前目录下
# -------------------------test loader部分---------------------
load_case = unittest.defaultTestLoader.discover(start_dir=current_directory_path, pattern='fff*.py')    # 加载当前目录下的fff开头的文件下的测试用例

# --------------------------test suit部分-----------------------------------------
suite = unittest.TestSuite()        # 构建测试套件
suite.addTest(load_case) 			# 添加test load收集到的test case到suite中

# --------------------------test runner部分-------------------------------------
runner = unittest.TextTestRunner(verbosity=0)
runner.run(suite) 					# 将suit放入runner中执行
"""

# 方法1
# ---------------------------test suit部分------------------------
suite = unittest.TestSuite()        # 构建测试套件
suite.addTest(example1('test_a01')) # 添加example1类下的用例test_a01到suite中
suite.addTest(example1('test_a02')) # 添加example1类下的用例test_a02到suite中
# 方法2
# --------------------------test suit部分-----------------------------------------
suite = unittest.TestSuite()       						 # 构建测试套件
test_cases = [example1('test_a01'),example1('test_a02')] # 将test_a01、test_a02添加到test_cases列表
suite.addTests(test_cases)            					# 将test_cases列表添加到suite中
# text loader对应方法
# --------------------------test suit部分-----------------------------------------
suite = unittest.TestSuite()        # 构建测试套件
suite.addTest(load_case) 			# 添加test load收集到的test case到suite中


# 方法1
# ---------------------------test runner部分-------------------
if __name__ == '__main__':
    # 执行当前文件的测试用例
    unittest.main()
# 方法2
# --------------------------test runner部分-------------------------------------
runner = unittest.TextTestRunner(verbosity=0)
runner.run(suite) 					# 将suit放入runner中执行
