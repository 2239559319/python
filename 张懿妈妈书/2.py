import requests

def downImg():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    curPage=1               #当前页
    maxPage=301
    while curPage<=maxPage:
        url = "https://book.yunzhan365.com/byos/fsrl/files/mobile/%d.jpg" % curPage
        r=requests.get(url=url,headers=headers)
        with open("D:\\image\\%d.jpg"%curPage,"wb") as f:
            f.write(r.content)
        print("%d张图片已下载"%curPage)
        curPage+=1
downImg()