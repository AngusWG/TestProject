# wss3.py
import threadpool
import time

pool = threadpool.ThreadPool(2)


class AAA(object):

    def start_by_thread(func):
        def __decorator(*arg):
            list_var1 = arg
            reult = None
            request = threadpool.WorkRequest(func, list_var1, callback=reult)
            print("start by thread")
            pool.putRequest(request)
            pool.wait()
            return reult

        return __decorator

    @start_by_thread
    def plist(self, tes):
        """
        >>> plist(6)
        18
        >>> plist(8)
        24
        """
        print("AAA", tes)
        return tes * 3


if __name__ == '__main__':
    print(AAA().plist(2))
