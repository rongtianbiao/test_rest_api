# coding=utf-8
"""
此模块用于存放通用的方法
"""

import requests
import json


def send_req(method, url, data=None):
    """
    发送get、post请求函数，返回接口数据
    """
    method = method.lower()
    if method == "post":
        data = json.dumps(data)
        req = requests.post(url, data)
        return req.text
    if method == "get":
        req = requests.get(url, data)
        return req.text


def return_err_code(info):
    """
    返回err或code的值，如果字典中没这两项就返回info
    """
    try:
        print(info)
        info = json.loads(info)
        if "err" in info:
            return info["err"]
        if "code" in info:
            return info["code"]
        return info
    except:
        return info


def schedul_fun(self, method, url, data, code):
    """负责程序执行的调度函数"""
    info = send_req(method, url, data)
    res_code = return_err_code(info)
    if res_code in [0, 1, "1", "0"]:
        self.assertEqual(code, int(res_code), "与预期输入的code码:" + str(code) + "；不一致, bug")
    elif not res_code:
        print u"返回结果为：" + str(res_code)
        self.assertTrue(res_code, u"返回结果为：" + str(res_code))
    else:
        print u"返回结果为：" + str(res_code)
        self.assertFalse(res_code, u"返回结果为：" + str(res_code))