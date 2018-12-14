# coding=utf-8
from common.operation_excel import OperationExcel
from common.config import field_to_number

# 实例化一个打开用例excel的对象
open_excel = OperationExcel()
# 返回用例excel中每列对应的下标
field = field_to_number()

# 保存需要导入的模块
import_str = r"""# coding=utf-8
import unittest
from common.request_fun import schedul_fun
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
"""

# 测试类模板
test_class = """

class Test1(unittest.TestCase):
    def setUp(self):
        %s
    %s
    def tearDown(self):
        %s
"""

# 测试类中的函数
test_fun = """
    def test%s(self):
        u'''%s,参数为：%s'''
        method = "%s"
        url = "%s"
        data = '''%s'''
        code = "%s"
        schedul_fun(self, method, url, data, code)
"""

name_main_str = """

if __name__ == "__main__":
    unittest.main(verbosity=2)
"""


def create_case_py_file(file_name, test_class, path="../test_case/"):
    """创建测试py文件"""
    fi = open(path+file_name + r".py", "w")
    # 写入需要导入的模块
    fi.write(import_str)
    fi.write(test_class)
    fi.write(name_main_str)
    fi.close()


def read_excel_content():
    """读取用例excel中的内容"""
    global test_class, test_fun
    # 获取excel中的行数
    n_lines = open_excel.get_lines()
    # 逐行读取内容
    for n in range(1, n_lines):
        # 编号
        serial_number = open_excel.get_cell_value(n, field["serial_number"])
        # 接口名称
        rest_name = open_excel.get_cell_value(n, field["rest_name"])
        # 接口url
        url = open_excel.get_cell_value(n, field["url"])
        # 请求方式
        method = open_excel.get_cell_value(n ,field["method"])
        # 请求参数
        parameters = open_excel.get_cell_value(n, field["parameter"])
        # 预期结果
        expected_results = open_excel.get_cell_value(n, field["expected_result"])
        # parameter_list = parameters.strip().split("\n")
        # # for par in parameter_list:
        # #     par_list = str(par).strip().split()
        # #     print(par_list)
        # # print(parameter_list)

        # 用参数填充占位符
        test_fun_fill = test_fun % (str(1),str(rest_name), str(parameters), str(method), str(url), str(parameters), str(expected_results))
        test_class_fill = test_class % ("pass", test_fun_fill, "pass")
        create_case_py_file(serial_number, test_class_fill)

read_excel_content()