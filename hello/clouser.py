def createCounter():
    i = [0]
    def counter():
        i[0] += 1
        return i[0]
    return counter

def createCounter1():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) 
counterB = createCounter1()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')