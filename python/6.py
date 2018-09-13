#md5加密实例
import hashlib

#待加密信息
str="this is a string"
#创建md5对象
h=hashlib.md5()
#此处必须声明encode
h.update(str.encode(encoding="utf-8"))
#加密后
print(h.hexdigest())