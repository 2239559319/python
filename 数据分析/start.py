#运行jupyter-notebook
import subprocess
p=subprocess.Popen(["jupyter-notebook"],stdout=subprocess.PIPE)
print(p.stdout.read())