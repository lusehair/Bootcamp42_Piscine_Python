import os 
import time

def ft_progress(it):
    start = time.time()
    time_stamp = 0.0
    _rest = 0.0
    for x in it:
        eta = (_rest - time_stamp) * (it[-1] - x)
        et = time.time() - start
        percentage = ((x * 100) // it[-1])
        rest = "{}/{}".format(x+1, it[-1]+1)
        progress = "{}>".format('=' * ((int(percentage) // 5) - 1))
        os.system('clear')
        print("ETA: {:.2f}s [{:3.0f}%] [{:20}] {} | elapsed time {:.2f}s".format(eta, percentage, progress, rest, et))
        time_stamp = time.time()
        yield x
        _rest = time.time()


if __name__ == "__main__":

    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)