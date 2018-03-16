import time, functools
def logger(text):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, fn.__name__))
            start = time.time()
            ret = fn(*args, **kw)
            print('%s executed in %s ms' % (fn.__name__, time.time()-start))
            return ret
        return wrapper
    return metric
# 测试
@logger('test1')
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@logger('test2')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
    
