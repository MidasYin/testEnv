import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
from Model.Get_time import getTime
from Model.yamlConf import yamlConf

import platform
import  time

listLen = []


class Test_overlay_positions:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_overlay_positions(self):
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


        # 打开配置文件Mark_valid_days.yml
        path1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/Mark_valid_days.yml"
        if 'Windows' in platform.system():
            # windows os
            path1 = path1.replace('/', '\\')


        ye = yamlConf(path1)
        results = ye.LoadAll()
        gettime = getTime()
        n = 0


        #分别针对每一份报告中，相应的有效时间进行请求
        if reportIds != []:
            for result in results:
                log.info("--------------------------------------------")
                log.info("开始打开报告：" + str(reportIds[n][1]) + "：")
                print("--------------------------------------------")
                print("开始打开报告：" + str(reportIds[n][1]) + "：")
                for res in result:
                    if res["isContainData"] == True:
                        beginTime = res['day'].replace('-', "/") + " " + "00:00:00"
                        endTime = gettime.date_addta(beginTime, 1, "%Y/%m/%d %H:%M:%S")
                        log.info("开始执行开始时间：" + beginTime + " " + "结束时间为：" + endTime + " " + "的预加载N")
                        print("开始执行开始时间：" + beginTime + " " + "结束时间为：" + endTime + " " + "的预加载")
                        url = "/overlay/load/" + str(reportIds[n][1])
                        result = Request.execute("config_markDr.xlsx", "overlay", "overlay_load",url,beginTime=beginTime,
                                                     endTime=endTime, beatType="N")
                        time.sleep(1)
                        log.info("开始执行开始时间：" + beginTime + " " + "结束时间为：" + endTime + " " + "SLOT0")
                        print("开始执行开始时间：" + beginTime + " " + "结束时间为：" + endTime + " " + "SLOT0")
                        url = "/overlay/positions/"+str(reportIds[n][1])+"/SLOT_0"
                        result = Request.execute("config_markDr.xlsx", "overlay", "overlay_positions",url)
                        log.info("返回结果为：")
                print("结束打开报告：" + str(reportIds[n][1]) + "：")
                print("--------------------------------------------")
                log.info("结束打开此报告：" + str(reportIds[n][1]) + "：")
                log.info("----------------------------------------------")
                n=n+1
        else:
            log.info("当前没有报告")








