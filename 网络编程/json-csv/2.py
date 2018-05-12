import json
str=[{"username":"七夜","age":"24"},(2,3),1]
json_str=json.dumps(str,ensure_ascii=False)
print(json_str)
with open('D:/txt/qiye.txt','w') as fp:
    json.dump(str,fp=fp,ensure_ascii=False)

new_str=json.loads(json_str)
print(new_str)
with open('D:/txt/qiye.txt','r') as fp:
    print(json.load(fp))