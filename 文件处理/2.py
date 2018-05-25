from multiprocessing import Process
from multiprocessing import Pool
def run(name):
    print("this is process %d"%name)
if __name__=="__main__":
    p1=Process(target=run,args=(1,))
    p2=Process(target=run,args=(2,))
    pool=Pool(2)
    pool.map(run,(3,))
    pool.close()
'''
Pool类
close()
关闭进程池（pool），使其不在接受新的任务。
terminate()
结束工作进程，不在处理未处理的任务。
join()
主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。
'''