from rediscluster import StrictRedisCluster
import sys
class redis_cluster():
    def __init__(self):
        redis_nodes = [
                       {'host':'172.16.0.33','port':"9001"},
                       {'host':'172.16.0.33','port':"9002"},
                       {'host':'172.16.0.33','port':"9003"},
                       {'host':'172.16.0.33','port':"9004"},
                       {'host':'172.16.0.33','port':"9005"},
                       {'host':'172.16.0.33','port':"9006"}
                       ]
        try:
            self.redisconn = StrictRedisCluster(startup_nodes=redis_nodes,decode_responses=True,password ='KGcomRedis')
        except Exception as  e:
            print ("Connect Error!  reason is %s"%(e))
            sys.exit(1)

    def flushdb(self,params):
        for i in  range(0,len(params)):
            result = self.redisconn.delete(*self.redisconn.keys(pattern=params[i]))
            print(result)
        return

if __name__ == '__main__':
    Rc = redis_cluster()
    #params = "HomePageServiceImpl/hotAuthorInfo*"
    params= ["/kgApp/article/v12/articleRecommend*",
             "HomePageServiceImpl/hotAuthorInfo*",
             "UserProfileServiceImpl/getUserproFile*",
             "UserProfileServiceImpl/selectByuserprofileId*",
             "ArticleAppServiceImpl/getArticleOutModelText*",
             "ArticlekgServiceImpl/selectRelatedArticle*",
             "ArticlekgServiceImpl/selectTopArticle*",
             "/kgApp/adver/getRecommendAdvs*",
             "adver/*",
             "ArticleAppServiceImpl/getArticleOutModelText*",
             "VideoServiceImpl/hotVideoList*",
             "KeywordsServiceImpl/getKeywordsAll*",
             "KeywordsServiceImpl/getHotSearch:*",
             "ArticlekgServiceImpl/selectTopArticle:*",
             "VideoServiceImpl/hotVideoList:*"
             ]
    print(Rc.flushdb(params))
