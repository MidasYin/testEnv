import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform

class Test_flow:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_flow_All(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "All_report" # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")

    def test_flow_Finish(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "FINISH_report" # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_AUDIT_PASS(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "AUDIT_PASS_report" # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")

    def test_flow_AUDITING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "AUDITING_report" # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_EDITING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "EDITING_report" # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_WAIT_FOR_EDIT(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "WAIT_FOR_EDIT_report"  # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_ANALYZE_FAILED(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "ANALYZE_FAILED_report"  # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_ANALYZING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "ANALYZING_report"  # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_WAIT_FOR_ANALYZE(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "WAIT_FOR_ANALYZE_report"  # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_UPLOAD_FAILED(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "UPLOAD_FAILED_report"  # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")


    def test_flow_INITIAL(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "INITIAL_report"  # 传入配置文件的section
        # 把PDF状态传到temp.ini中，1为True 0为False
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)
        if reportIds != []:
            for reportId in reportIds:
                log.info("开始打开报告：" + str(reportId[1]) + "：")
                url = "/reports/" + str(reportId[1]) + "/flows"
                result = Request.execute("config_superAdmin.xlsx", "report", "flows", url)
                log.info("返回结果为：")
                log.info(result)
                # log.info(result.content)
                log.info("-------------")
        else:
            log.info(section + ":"+ "没有报告")