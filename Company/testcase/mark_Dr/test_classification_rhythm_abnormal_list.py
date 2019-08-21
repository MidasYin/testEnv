import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform
from Model.yamlConf import yamlConf
listJson = []


class Test_classification_rhythm_abnormal_list:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_classification_rhythm_abnormal_list(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')

        section = "EDITING_report"  # 传入配置文件的section,标注中的数据
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login" #传入配置文件的section
        conf_Filename = "markDr.ini"
        rhythm = "V"
        Request = requestAPI(log,conf_Filename,section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/ecg/classification_rhythm_abnormal_list?abnormal_name="+rhythm+"&"+"report_id="+str(reportId[1])+"&start=0&limit=5"
                result = Request.execute("config_markDr.xlsx", "ecg", "classification_rhythm_abnormal_list", url)
                log.info("返回结果为：")
                log.info(result.json())
                listJson.append(result.json())


            #放入返回结果入相应的yml文件中，后续调用
            path = os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/Mark_classification_rhythm_abnormal_list.yml"
            if 'Windows' in platform.system():
                # windows os
                path = path.replace('/', '\\')

            #把返回值放入yaml文件中：

            ye = yamlConf(path)
            ye.DumpAll(listJson)

        else:
            log.info(section + ":"+ "没有报告")




