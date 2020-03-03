from multiprocessing import Process
import multiprocessing
import time

def sum(start=0, end=800000000):
    sum = 0
    for i in range(start, end):
        sum += i
if __name__ == "__main__":

    start = time.time()
    sum()
    end = time.time()
    print(end - start)
    # time elapsed: 61.13864707946777


    print("Number of cpu : ", multiprocessing.cpu_count())
    # "Number of cpu :  4"

    start = time.time()
    ps = []
    num = (int) (800000000 / multiprocessing.cpu_count())

    for i in range(1, multiprocessing.cpu_count()):
        p = Process(target=sum, args=(num*(i-1), num*i))
        ps.append(p)
        p.start()

    for p in ps:
        p.join()

    end = time.time()
    print(end - start)
    # time elapsed: 28.492934465408325
