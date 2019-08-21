import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform
import time

class Test_pdf_generate:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_pdf_generate(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/uploaderDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')

        section = "FINISH_report"  # 传入配置文件的section,标注中的数据
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_Filename = "uploaderDr.ini"
        Request = requestAPI(log, conf_Filename, section1)

        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/pdf/generate/?report_id=" + str(reportId[1])
                result = Request.execute("config_uploaderDr.xlsx", "pdf", "pdf_generate", url)
                time.sleep(1)
                log.info("返回结果为：")
                log.info(result)


