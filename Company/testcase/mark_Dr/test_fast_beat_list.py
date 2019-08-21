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
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "EDITING_report"  # 传入配置文件的section,标注中的数据
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log, conf_Filename, section1)


        # 获取上一层接口（valid_dats）返回的数据
        path1 = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))) + "/configure/Mark_valid_days.yml"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        ye = yamlConf(path1)
        allList = ye.LoadAll()
        n = 0


        #分别针对每一份报告中，相应的有效时间进行请求
        for valid_days_list in allList:
            log.info("--------------------------------------------")
            log.info("开始打开报告：" + str(reportIds[n][1]) + "：")
            print("--------------------------------------------")
            print("开始打开报告：" + str(reportIds[n][1]) + "：")
            for valid_day in valid_days_list:
                if valid_day["isContainData"] == True:
                    beginTime = valid_day["day"]
                    log.info("开始执行开始时间为：" + beginTime + " " + "的fastbeatlist")
                    print("开始执行开始时间为：" + beginTime + " " + "的fastbeatlist")
                    url = '/ecg/fast_beat_list?report_id=' + str(
                        reportIds[n][1]) + '&date=' + beginTime + "&start=0&end=-1"  # 构造灵活的URL
                    result = Request.execute("config_markDr.xlsx", "ecg", "fast_beat_list", url)
                    time.sleep(1)
                    log.info("返回结果为：")
            print("结束打开报告：" + str(reportIds[n][1]) + "：")
            print("--------------------------------------------")
            log.info("结束打开此报告：" + str(reportIds[n][1]) + "：")
            log.info("----------------------------------------------")
            n=n+1


