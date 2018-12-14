# coding=utf-8
"""此文件用来保存配置相关信息"""


def field_to_number():
    """测试用例excel中，返回每列字段对应的数字"""
    return {
        "serial_number": 0,  # 编号
        "rest_name": 1,  # 接口名称
        "url": 2,    # 接口url
        "method": 3,    # 请求方式
        "parameter": 4,    # 请求参数
        "expected_result": 5    # 预期结果
    }

