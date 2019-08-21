import requests
import json
import configparser
conf = configparser.ConfigParser()
conf.read(r"C:\Users\Yin\PycharmProjects\ceshi\lanjing\configure\dataManager.ini","utf-8")   #读取temp配置文件
cookies = conf.get("login","cookies")


#后续请求可以封装成一个公共类
for i in range(20,34):

    url = "http://ecg-java-release.landmind.cn/users"
    parms = {
        'nick_name':'auto-biao'+str(i),
        'role':'ROLE_EDITOR',
        'login_name':'lj-auto-biao'+str(i),
        'description':'auto create',
        'signature': 'null'                        # 00 上传医生 1 标注医生 2 审核医生 3 数据管理员;   数据库对应type 0 上传医生 1 标注医生 2 审核医生 3 数据管理员
    }
    headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
             "Cookie": cookies  }

    result = requests.post(url,data=parms,headers=headers)
    status = result.status_code
    #print(result.text)

    if status==200:
        # result = json.loads(result.text)  # python str 转换为json 数据类型 （dict）
        print(result)
        print(type(result))
    else:
        print("访问失败")
