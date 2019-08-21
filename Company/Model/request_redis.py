import redis
import sys
import Model.config
import os
import platform

config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/configure/sqlconf.ini'
if 'Windows' in platform.system():
        # windows os
    config_path = config_path.replace('/', '\\')

conf = Model.config.Configure(config_path)
port = conf.Get("Redis","port")
host = conf.Get("Redis","host")
password = conf.Get("Redis","password")


class Redis():
    def __init__(self):
        self.port = port
        self.host = host
        self.password = password
        try:
            self.redisconn = redis.StrictRedis(host=self.host, port=self.port, db=0,password=self.password)
        except Exception as  e:
            print ("Connect Error!  reason is %s"%(e))
            sys.exit(1)

    # def flushdb(self,params):
    #     for i in  range(0,len(params)):
    #         result = self.redisconn.delete(*self.redisconn.keys(pattern=params[i]))
    #         print(result)
    #     return

if __name__ == '__main__':
    Rc = Redis()
    # #params = "HomePageServiceImpl/hotAuthorInfo*"
    # params= ["/kgApp/article/v12/articleRecommend*",
    #          "HomePageServiceImpl/hotAuthorInfo*",
    #          "UserProfileServiceImpl/getUserproFile*",
    #          "UserProfileServiceImpl/selectByuserprofileId*",
    #          "ArticleAppServiceImpl/getArticleOutModelText*",
    #          "ArticlekgServiceImpl/selectRelatedArticle*",
    #          "ArticlekgServiceImpl/selectTopArticle*",
    #          "/kgApp/adver/getRecommendAdvs*",
    #          "adver/*",
    #          "ArticleAppServiceImpl/getArticleOutModelText*",
    #          "VideoServiceImpl/hotVideoList*",
    #          "KeywordsServiceImpl/getKeywordsAll*",
    #          "KeywordsServiceImpl/getHotSearch:*",
    #          "ArticlekgServiceImpl/selectTopArticle:*",
    #          "VideoServiceImpl/hotVideoList:*"
    #          ]
    print(Rc)
