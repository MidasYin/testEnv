import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform

reportList_All = []
reportList_WAIT_FOR_EDIT = []
reportList_EDITING = []
reportList_EDITED= []

class Test_user_patientList:
    @classmethod
    def setup_class(cls):
        print("start manager login case:")
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_user_patient_All(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_markDr.xlsx","common","patientList_All")


        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_All.append(user["record_id"])

                # 把List状态传到markDr.ini中
            for i in range(0, len(reportList_All)):
                conf.Set("All_report", "report" + str(i), str(reportList_All[i]))
        else:
            log.info("当前状态下没有报告")


    def test_user_patient_WAIT_FOR_EDIT(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_markDr.xlsx","common","patientList_WAIT_FOR_EDIT")


        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_WAIT_FOR_EDIT.append(user["record_id"])

                # 把List状态传到markDr.ini中
            for i in range(0, len(reportList_WAIT_FOR_EDIT)):
                conf.Set("WAIT_FOR_EDIT_report", "report" + str(i), str(reportList_WAIT_FOR_EDIT[i]))
        else:
            log.info("当前状态下没有报告")



    def test_user_patient_EDITING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_markDr.xlsx", "common", "patientList_EDITING")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_EDITING.append(user["record_id"])

                # 把List状态传到markDr.ini中
            for i in range(0, len(reportList_EDITING)):
                conf.Set("EDITING_report", "report" + str(i), str(reportList_EDITING[i]))
        else:
            log.info("当前状态下没有报告")


    def test_user_patient_EDITED(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_markDr.xlsx", "common", "patientList_EDITED")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_EDITED.append(user["record_id"])

                # 把List状态传到markDr.ini中
            for i in range(0, len(reportList_EDITED)):
                conf.Set("EDITED_report", "report" + str(i), str(reportList_EDITED[i]))
        else:
            log.info("当前状态下没有报告")



