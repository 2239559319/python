import requests

def query():
    '''
    查询函数
    :param building:教学楼
    :return: 信息list
    '''
    print("教学楼编号:")
    print("0\t望江东2\n1\t望江东3\n2\t基教A\n3\t基教C\n4\t一教A\n5\t一教B\n6\t一教C\n7\t一教D\n8\t综B\n9\t综C\n10\t文科楼1区\n11\t文科楼2区\n12\t文科楼3区\n13\t华西9教\n14\t华西10教")
    buildingIndex=input("输入要查询的教学楼:")
    url="http://cir.scu.edu.cn/cir/XLRoomData"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    buildingList=["WJdong2","WJdong3","WJjijiaoA","WJjijiaoC",
                  "yjA","yjB","yjC","yjD","zongB","zongC","wen1","wen2","wen3",
                  "HX9","HX10"]
    data={
        "jxlname":buildingList[int(buildingIndex)]
    }
    r=requests.post(url=url,data=data,headers=headers)
    return r.json()["roomdata"]

def deal(dataList):
    '''
    :param dataList:教室信息
    :return:
    '''
    for room in dataList:

        print(room)

dataList=query()
deal(dataList)