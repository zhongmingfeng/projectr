import time


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return

        print('[消费者] <--- Consuming %s...' % n)
        time.sleep(0.5)
        r = 'ok'


def producer(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者] ---> Producing %s...' % n)
        # 和next有同样的同能，可以触发函数到下一个yield，
        # 区别于next的是可以像yield的左边的变量传值，例如上面yield左边的n
        c_ret = c.send(n)

        print('[生产者] Consumer return %s' % c_ret)
    c.close()


if __name__ == '__main__':
    c = consumer()
    producer(c)