#m.weibo.cn操作
import requests
import time

class Query(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'cookie':'''Cookie: _T_WM=6e5ced355e9ee288e1529115fa1f7d9a; WEIBOCN_FROM=1110106030; ALF=1554387506; SCF=AinddVvRwLE6lgBp9ZPK-QimeCgjYnpg57j0j5k5Xn7iS3gnWKSGNoNn86bj4Vvu6YEjCfnoVyCb0FhcuWe5lfM.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh6DYYRU4_A_J01h1lvXfnn5JpX5KMhUgL.FozNSoeRSh.Ee022dJLoIE-LxKnLBoBLBo2LxKnLBo-LBo5LxK-L1h2L12qLxK.L12zL1KiD; SUB=_2A25xevVsDeRhGeRJ7VEZ9CfOyD2IHXVShJskrDV6PUJbkdANLXH8kW1NUkRrhwCSmbpStE1HJUXLmrqqNAfwLF0B; SUHB=0JvhUSTVAb_p_H; SSOLoginState=1551795516; MLOGIN=1; XSRF-TOKEN=69a931; M_WEIBOCN_PARAMS=oid%3D4346499800699547%26lfid%3D4346499800699547%26luicode%3D20000174%26uicode%3D20000174'''
        }           #这里必须用cookie保存登录状态，获取转发和评论的id列表
        self.s=requests.Session()
    def getAuthorize(self):                 #验证登录
        url1 = "https://m.weibo.cn/api/config"
        r = requests.get(url=url1, headers=self.headers)
        self.st=r.json()['data']['st']
        print(r.json())

    def getCommentId(self,id,mid):
        '''
        获取全部评论列表
        :param id: 微博id :str
        :param mid 微博mid :str
        :return: 评论的人列表
        '''
        userList=[]             #评论的id列表
        #初始请求
        url="https://m.weibo.cn/comments/hotflow"
        startUrl=url+"?id="+id+"&mid="+mid+"&max_id_type=0"
        curPage=1           #当前的评论页
        userMsg={}          #id信息
        r=requests.get(url=startUrl,headers=self.headers)
        msg=r.json()['data']
        for i in msg['data']:
            userMsg['id']=i['user']['id']
            userMsg['username']=i['user']['screen_name']
            userList.append(userMsg)
        print("第%d页评论已处理"%curPage)

        max_id=msg['max_id']        #max_id为判断是否还有下一页的标志
        while max_id!=0:            #为0是表示是最后一页
            time.sleep(3)           #限制请求速度
            curPage+=1
            nextUrl=url+"?id="+id+"&mid="+mid+"&max_id="+str(max_id)+"&max_id_type=0"
            r=requests.get(url=nextUrl,headers=self.headers)
            msg = r.json()['data']
            for i in msg['data']:
                userMsg['id'] = i['user']['id']
                userMsg['username'] = i['user']['screen_name']
                userList.append(userMsg)
            max_id = msg['max_id']  #更新max_id
            print("第%d页评论已处理"%curPage)
        print("评论列表已全部完成")
        return userList

    def getRepostId(self,id):
        '''
        获取全部转发列表
        :param id: 微博id :str
        :return: 转发人列表
        '''
        userList=[]
        url="https://m.weibo.cn/api/statuses/repostTimeline"
        curPage=1
        userMsg={}
        #初始请求
        startUrl=url+"?id="+id+"&page=%d"%curPage
        r=requests.get(url=startUrl,headers=self.headers)
        msg=r.json()['data']
        for i in msg['data']:
            userMsg['id'] = i['user']['id']
            userMsg['username'] = i['user']['screen_name']
            userList.append(userMsg)
        maxPage=msg['max']              #最大的页数
        print("第%d页已完成"%curPage)
        curPage+=1

        while curPage<=maxPage:         #小于最大页时继续请求
            time.sleep(3)
            nextUrl=url+"?id="+id+"&page=%d"%curPage
            r=requests.get(url=nextUrl,headers=self.headers)
            msg = r.json()['data']
            for i in msg['data']:
                userMsg['id'] = i['user']['id']
                userMsg['username'] = i['user']['screen_name']
                userList.append(userMsg)
            print("第%d页已完成" % curPage)
            curPage += 1

        print("转发列表已全部完成")
        return userList


query=Query()
query.getAuthorize()
