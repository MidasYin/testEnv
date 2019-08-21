import pytest
import os
import platform
from Model.Get_time import getTime

def getAddr(Addr):
    base_Addr = os.path.dirname(os.path.abspath(__file__))
    full_Addr = base_Addr + Addr
    if 'Windows' in platform.system():
        # windows os
        Addr = full_Addr.replace('/', '\\')
        return Addr
    return full_Addr

def getResult():
    base_Addr = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_Addr = base_Addr + "/Result/"
    if 'Windows' in platform.system():
        # windows os
        Addr = full_Addr.replace('/', '\\')
        return Addr
    return full_Addr



if __name__ == '__main__':
    DateNow = getTime()
    dateNow = DateNow.dateNow_format()

    pytest.main(['--html=' + getResult() +  '/' + 'report'+ dateNow + '.html', '-v', '-s', getAddr("")]) #执行所有用例
    #pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s', getAddr("/superadmin/")])   #执行superadmin用例
    #pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s', getAddr("/data_Manager/")]) #执行dataManager用例
    #pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s',getAddr("/review_Dr/")])  # 执行review_Dr用例
    #pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s',getAddr("/mark_Dr/")])  # 执行mark_Dr用例
    #pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s',getAddr("/Uploader_Dr/")])  # 执行uploader_Dr用例
    #pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s', getAddr("/data_Manager/") + "dataManage_login_test.py"]) #执行dataManager用例
    # pytest.main(['--html=' + getResult() + '/' + 'report' + dateNow + '.html', '-v', '-s', getAddr("/mark_Dr/")+ "mark_login_test.py",getAddr("/mark_Dr/")+ "test_ab_patientList.py"
    #               ,getAddr("/mark_Dr/")+ "test_b_valid_days.py",getAddr("/mark_Dr/")+ "test_fast_beat_list.py"])  # 执行mark_Dr用例

