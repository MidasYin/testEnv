# -*- coding:UTF-8 -*-
import json
import xlrd
import os
import re

# 获取参数结果
def get_data(result):
    try:
        my_result = json.loads(result)
        data_result = my_result['data']
        return data_result
    except:
        print("Not Found Data")
        return None


# 获取接口message结果
def get_message(result):
    try:
        my_result = json.loads(result)
        message_result = my_result['message']
        return message_result
    except:
        print("Not Found Message")


# 获取验证码
def get_smsCode(test_phone, test_sms):
    # f = open(test_sms, 'r')
    for i in test_sms.readlines():
        phone = re.findall(r"\"phone\":\"(.+?)\"", i)
        if phone[0] == test_phone:
            print(phone[0])
            code = re.findall(r"您的验证码是(.+?),", i)
            print(code[0])
            return code[0]