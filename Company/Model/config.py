# _*_ coding:UTF-8 _*_

import configparser


class Configure:

    def __init__(self, path):
        self.path = path
        self.cr = configparser.ConfigParser()
        self.cr.read(path, encoding="utf-8-sig")



    def Get(self, section, key):
        try:
            result = self.cr.get(section, key)
        except configparser.NoOptionError as err:
            print("configparser.NoOptionError: ", err)
            result = ""
        except configparser.NoSectionError as err:
            print("configparser.NoSectionError: ", err)
            result = ""
        return result

    def Get_items(self, section):
        try:
            result = self.cr.items(section)
        except configparser.NoSectionError as err:
            print("configparser.NoSectionError: ", err)
            result = ""
        return result


    def Set(self, section, key, value):
        # noinspection PyBroadException
        try:
                self.cr.set(section, key, value)
                with open(self.path, 'w') as config:
                    self.cr.write(config)
                    config.close()
        except Exception as e:
            print(e)
            return False
        return True


