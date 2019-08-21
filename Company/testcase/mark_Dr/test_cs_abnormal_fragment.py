import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
from Model.yamlConf import yamlConf
import platform
import time
listPosition = []

class Test_abnormal_fragment:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_abnormal_fragment(self):
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

        section1 = "login" #传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log,conf_Filename,section1)


        #获取上一层接口（classification_rhythm_abnormal_list）返回的数据
        path1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/Mark_classification_rhythm_abnormal_list.yml"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        ye = yamlConf(path1)
        results = ye.LoadAll()
        n=0


        ##分别针对每一份报告中，相应的position进行请求
        if reportIds != []:
            for result in results:
                log.info("--------------------------------------------")
                log.info("开始打开报告：" + str(reportIds[n][1]) + "：")
                print("--------------------------------------------")
                print("开始打开报告：" + str(reportIds[n][1]) + "：")
                for positions in result:
                    listPosition = positions["position"]
                    url = "/ecg/abnormal_fragment?report_id="+str(reportIds[n][1])+"&position="+str(listPosition)+"&label=V"
                    result = Request.execute("config_markDr.xlsx", "ecg", "abnormal_fragment", url)
                    log.info("返回结果为：")
                    # log.info(result)
                    log.info("-------------")
                    time.sleep(1)
                print("结束打开报告：" + str(reportIds[n][1]) + "：")
                print("--------------------------------------------")
                log.info("结束打开此报告：" + str(reportIds[n][1]) + "：")
                log.info("----------------------------------------------")
                n=n+1
        else:
            log.info(section + ":"+ "没有报告")



