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
# 输入username,filename,filepath
#####################################
username = input("please input username:") #res-xiaobai
record_id = input("please input record_id:") #1266
state = input("please input state:") #传AUDIT_PASS/AUDITING


# #####################################
# # 审核医生请求login接口，获取session
# #####################################

url = baseUrl + "/user/login/"
params = {'username':username,
'password' :'8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'
}

response = requests.post(url,data=params)
cookies = requests.utils.dict_from_cookiejar(response.cookies)  # 返回值 sessionid
result = response.json()  # 返回值 json
role = result["data"]["role"]
user_id = (result["data"]["user_id"])
# 处理cookies格式
key = cookies["SESSION"]
cookies = "SESSION" + "=" + key
print(cookies)



# #####################################
# 通过审核接口/取消审核接口
# 接口路径：/user/record_state/
# 请求方式：post
# 请求参数：record_id 报告id(必传)
#           state 报告状态(必传, 传AUDIT_PASS/AUDITING）
# #####################################

url = baseUrl + "/user/record_state/"
t_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
    "Cookie": cookies
}
params = {'record_id':record_id,
'state' :state
}
response = requests.post(url,data=params,headers=t_headers)
print(response.status_code)
print(response.text)

