import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform

reportList_All = []
reportList_FINISH = []
reportList_AUDIT_PASS = []
reportList_AUDITING= []

class Test_user_patientList:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_user_patient_All(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_reviewDr.xlsx","common","patientList_All")


        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_All.append(user["record_id"])

                # 把List状态传到reviewDr.ini中
            for i in range(0, len(reportList_All)):
                conf.Set("All_report", "report" + str(i), str(reportList_All[i]))
        else:
            log.info("当前状态下没有报告")
            

    def test_user_patient_FINISH(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_reviewDr.xlsx", "common", "patientList_FINISH")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_FINISH.append(user["record_id"])

                # 把List状态传到reviewDr.ini中
            for i in range(0, len(reportList_FINISH)):
                conf.Set("FINISH_report", "report" + str(i), str(reportList_FINISH[i]))
        else:
            log.info("当前状态下没有报告")
            
            
            
    def test_user_patient_AUDIT_PASS(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_reviewDr.xlsx", "common", "patientList_FINISH")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_AUDIT_PASS.append(user["record_id"])

                # 把List状态传到reviewDr.ini中
            for i in range(0, len(reportList_AUDIT_PASS)):
                conf.Set("AUDIT_PASS_report", "report" + str(i), str(reportList_AUDIT_PASS[i]))
        else:
            log.info("当前状态下没有报告")



    def test_user_patient_AUDITING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_reviewDr.xlsx", "common", "patientList_AUDITING")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_AUDITING.append(user["record_id"])

                # 把List状态传到markDr.ini中
            for i in range(0, len(reportList_AUDITING)):
                conf.Set("AUDITING_report", "report" + str(i), str(reportList_AUDITING[i]))
        else:
            log.info("当前状态下没有报告")