import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform

# 初始化列表
reportList_All = []
reportList_finish = []
reportList_AUDIT_PASS = []
reportList_AUDITING = []
reportList_EDITING = []
reportList_WAIT_FOR_EDIT = []
reportList_ANALYZE_FAILED = []
reportList_ANALYZING = []
reportList_WAIT_FOR_ANALYZE = []
reportList_UPLOAD_FAILED = []
reportList_INITIAL = []


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
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_All")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到所有的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_All.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_All)):
                conf.Set("All_report", "report" + str(i), str(reportList_All[i]))
        else:
            result["users"]

    def test_user_patient_finish(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList")

        # print(result)
        log.info("返回结果为：")
        log.info(result)
        # print(result["users"])

        # 取到已完成的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)
            for user in result["users"]:
                reportList_finish.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_finish)):
                conf.Set("FINISH_report", "report" + str(i), str(reportList_finish[i]))
        else:
            return result["users"]

    def test_user_patient_AUDIT_PASS(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_AUDIT_PASS")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到已审核的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_AUDIT_PASS.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_AUDIT_PASS)):
                conf.Set("AUDIT_PASS_report", "report" + str(i), str(reportList_AUDIT_PASS[i]))
        else:
            return result["users"]

    def test_user_patient_AUDITING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_AUDITING")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到审核中的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_AUDITING.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_AUDITING)):
                conf.Set("AUDITING_report", "report" + str(i), str(reportList_AUDITING[i]))
        else:
            return result["users"]

    def test_user_patient_EDITING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_EDITING")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到标注中的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_EDITING.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_EDITING)):
                conf.Set("EDITING_report", "report" + str(i), str(reportList_EDITING[i]))
        else:
            return result["users"]

    def test_user_patient_WAIT_FOR_EDIT(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_WAIT_FOR_EDIT")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到已标注的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_WAIT_FOR_EDIT.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_WAIT_FOR_EDIT)):
                conf.Set("WAIT_FOR_EDIT_report", "report" + str(i), str(reportList_WAIT_FOR_EDIT[i]))
        else:
            return result["users"]

    def test_user_patient_ANALYZE_FAILED(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_ANALYZE_FAILED")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到分析失败的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_ANALYZE_FAILED.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_ANALYZE_FAILED)):
                conf.Set("ANALYZE_FAILED_report", "report" + str(i), str(reportList_ANALYZE_FAILED[i]))
        return result["users"]

    def test_user_patient_ANALYZING(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_ANALYZING")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到分析中的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_ANALYZING.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_ANALYZING)):
                conf.Set("ANALYZING_report", "report" + str(i), str(reportList_ANALYZING[i]))
        else:
            return result["users"]

    def test_user_patient_WAIT_FOR_ANALYZE(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_WAIT_FOR_ANALYZE")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到待分析的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_WAIT_FOR_ANALYZE.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_WAIT_FOR_ANALYZE)):
                conf.Set("WAIT_FOR_ANALYZE_report", "report" + str(i), str(reportList_WAIT_FOR_ANALYZE[i]))
        else:
            return result["users"]

    def test_user_patient_UPLOAD_FAILED(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_UPLOAD_FAILED")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到上传失败的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_UPLOAD_FAILED.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_UPLOAD_FAILED)):
                conf.Set("UPLOAD_FAILED_report", "report" + str(i), str(reportList_UPLOAD_FAILED[i]))
        else:
            return result["users"]

    def test_user_patient_INITIAL(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "patientList_INITIAL")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

        # 取到未上传的报告ID放入 dataManager.ini中

        if result["users"] != []:
            conf = Configure(path)

            for user in result["users"]:
                reportList_INITIAL.append(user["record_id"])

                # 把List状态传到dataManager.ini中
            for i in range(0, len(reportList_INITIAL)):
                conf.Set("INITIAL_report", "report" + str(i), str(reportList_INITIAL[i]))

        else:
            return result["users"]
