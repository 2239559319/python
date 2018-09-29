import requests
import base64

def gettoken():
    '''
    9.29hao 这一个应用返回的token是
    24.c9af35ee0ecf024999829554498e92f7.2592000.1540790541.282335-14315592
    :return:
    '''
    url="https://aip.baidubce.com/oauth/2.0/token"
    data={
        "grant_type":"client_credentials",
        "client_id":"FYNYlRnN3mpq1MSLEuuaIq4n",
        "client_secret":"btsop6EepUQX1koMl2ihKcL5OEr8eXEG"
    }
    r=requests.post(url=url,data=data)
    token=r.json()['access_token']
    return token

def getstr(filepath):
    with open(filepath, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        return str

def getresult(filepath):
    '''
    url1:通用文字识别，50000次/天
    url2:通用文字识别（含位置信息版），500次/天
    url3:通用文字识别（高精度版），500次/天
    url4:通用文字识别（高精度含位置版），50次/天
    url5:数字识别，500次/天
    :param filepath:
    :return:
    '''
    url1="https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    url2="https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    url3="https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    url4="https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    url5="https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    header={
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data={
        "access_token":gettoken(),
        "image":getstr(filepath),
        "language_type":"CHN_ENG"
    }
    r=requests.post(url=url1,headers=header,data=data)
    print(r.text)
    str=r.json()["words_result"][0]["words"]
    return str

print(getresult('2.jpg'))