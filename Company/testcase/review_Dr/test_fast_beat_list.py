import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
from Model.yamlConf import yamlConf
import time
import platform
valid_days = []


class Test_fast_beat_list:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_fast_beat_list(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section)

        #获取审核中的报告：
        section1 = "AUDITING_report"  # 传入配置文件的section,审核中的数据
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section1)  # 取出所有setion下面的键值对


        # 获取上一层接口（valid_dats）返回的数据
        path1 = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))) + "/configure/Review_valid_days.yml"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        ye = yamlConf(path1)
        allList = ye.LoadAll()


        #找出有效时间
        for valid_day in allList:
            if valid_day["isContainData"] == True:
                    valid_days.append(valid_day["day"])


        #使用有效时间进行遍历访问,由于是审核中的报告，只会有一个报告，所以直接取得reportIds[0][1]
        for day in valid_days:
            beginTime = day
            log.info("开始执行开始时间为：" + beginTime + " " + "的fastbeatlist")
            print("开始执行开始时间为：" + beginTime + " " + "的fastbeatlist")
            url = '/ecg/fast_beat_list?report_id='+ str(reportIds[0][1]) +'&date='+ beginTime + "&start=0&end=-1" #构造灵活的URL
            result = Request.execute("config_markDr.xlsx", "ecg", "fast_beat_list", url)
            time.sleep(1)
            log.info("返回结果为：")
