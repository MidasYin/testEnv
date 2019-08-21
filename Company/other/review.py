import requests
import yaml
import os
import platform


####################################
#获取baseUrl
####################################
path = os.path.dirname(os.path.abspath(__file__)) + "/config.yml"
if 'Windows' in platform.system():
    # windows os
    path = path.replace('/', '\\')

try:
    result = yaml.load(open(path), Loader=yaml.FullLoader)
except yaml.YAMLError as err:
    print("YAMLError: ", err)
    result = ""
baseUrl = result["baseUrl"]


#####################################
# 输入nick_name,login_name,password
#####################################
nick_name = input("please input nick_name:") #res-xiaobai
login_name = input("please input login_name:") #res-xiaobai
password = input("please input password:") #传AUDIT_PASS/AUDITING


#####################################
# 请求创建审核医生接口
# 请求方式：post
# 请求参数：nick_name 用户昵称(必传)
#           login_name 用户账户名(必传)
#           password 密码(可不传,默认123456)
#           role 角色(必传，传ROLE_AUDITOR)
#返回码：200成功
#####################################

#需要先登录对方admin账号
t_url = baseUrl + "/user/login/"
params = {'username':'res-admin',
'password' :'8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'
}

response = requests.post(t_url,data=params)
cookies = requests.utils.dict_from_cookiejar(response.cookies)  # 返回值 sessionid
result = response.json()  # 返回值 json
role = result["data"]["role"]
user_id = (result["data"]["user_id"])
# 处理cookies格式
key = cookies["SESSION"]
cookies = "SESSION" + "=" + key
print(cookies)


#在请求创建审核医生
t_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
    "Cookie": cookies
}
url = baseUrl+"/users/"
params = {
'nick_name':nick_name,
'login_name':login_name,
'role':'ROLE_AUDITOR',
'password':password
}
response = requests.post(url,data=params,headers=t_headers)
print(response.status_code)
print(response.text)
