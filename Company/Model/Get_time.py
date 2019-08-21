from datetime import date, datetime, timedelta
import time


#########################################
#  此模块主要完成：
#  1、str 转为date，date转为 str
#  2、完成指定时间增加以及减少相应天数
##########################################


class getTime():

    def __init__(self):
        pass

    def str2date(self,str, date_format):
        date = datetime.strptime(str, date_format)
        return date

    def date2str(self,date, date_formate):
        str = date.strftime(date_formate)
        return str

    def date_delta(self,dateStr, gap, formate):
        date = self.str2date(dateStr,formate)
        pre_date = date + timedelta(days=-gap)
        pre_str = self.date2str(pre_date, formate)  # date形式转化为str
        return pre_str


    def date_addta(self,dateStr, gap, formate):
        date = self.str2date(dateStr,formate)
        pre_date = date + timedelta(days=gap)
        pre_str = self.date2str(pre_date, formate)  # date形式转化为str
        return pre_str


    def dateNow_format(self):
        return time.strftime('%Y%m%d%H%M%S', time.localtime())

