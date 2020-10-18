import time


def quadrado(nums):
    for x in nums:
        yield x*x
        time.sleep(0.5)


for i in quadrado(list(range(10))):
    print(i)



def quadrado_lista(nums):
    res = []
    for x in nums:
        res.append(x*x)

    return res


print(quadrado_lista(list(range(10))))
