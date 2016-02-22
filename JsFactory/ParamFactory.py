# -*- coding:utf-8 -*-
from pyv8 import PyV8
import JSource
__author__ = 'shadowmydx'


class ParamFactory:

    def __init__(self):
        self.js_env = PyV8.JSContext()
        self.js_env.enter()
        code = JSource.all_code
        self.js_env.eval(code)

    def get_params(self, ids):
        exe_code = '''
        bHl = asrsea('{"ids":"[input]","br":128000,"csrf_token":""}', test1(["流泪", "强"]), test1(mdmd), test1(["爱心", "女孩", "惊恐", "大笑"]));
        encText = bHl.encText;
        encSecKey = bHl.encSecKey;
        '''
        exe_code = exe_code.replace('input', ids)
        self.js_env.eval(exe_code)
        js_vars = self.js_env.locals
        enc_text = js_vars.encText
        enc_sec_key = js_vars.encSecKey
        return enc_text, enc_sec_key
