#运行jupyter-notebook
import os
p=os.popen("jupyter-notebook")
print(p.read())