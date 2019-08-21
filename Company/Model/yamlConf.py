# _*_ coding:UTF-8 _*_

import yaml


class yamlConf:

    def __init__(self, path):
        self.path = path

    def Load(self):
        try:
            result = yaml.load(open(self.path), Loader=yaml.FullLoader)
        except yaml.YAMLError as err:
            print("YAMLError: ", err)
            result = ""

        return result

    def LoadAll(self):
        try:
            result = yaml.load_all(open(self.path),Loader=yaml.FullLoader)
        except yaml.YAMLError as err:
            print("YAMLError: ", err)
            result = ""
        return result

    def DumpAll(self,stream):
        try:
            with open(self.path, 'w') as f:
                yaml.dump_all(stream, f)
        except yaml.YAMLError as err:
            print("YAMLError: ", err)




    def Dump(self, stream):
        try:
            with open(self.path, 'w') as f:
                yaml.dump(stream, f)
        except yaml.YAMLError as err:
            print("YAMLError: ", err)








