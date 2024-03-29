import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform


class Test_avg_heart_rate_by_day_per_minute:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_avg_heart_rate_by_day_per_minute(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')

        section = "AUDITING_report"  # 传入配置文件的section,标注中的数据
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section1)

        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/ecg/avg_heart_rate_by_day_per_minute?report_id=" + str(reportId[1])
                result = Request.execute("config_reviewDr.xlsx", "ecg", "avg_heart_rate_by_day_per_minute", url)
                log.info("返回结果为：")
                log.info(result)
