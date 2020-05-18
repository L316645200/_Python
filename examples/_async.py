import asyncio
import time

import requests

# async 定义异步任务
# await去执行长时间任务，将会被挂起
async def test2(i):
    r = await other_test(i)
    print(i, r)


async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(4)
    # time.sleep(4)
    print(time.time() - start)
    return r


url = ["https://segmentfault.com/p/1210000013564725",
       "https://www.jianshu.com/p/83badc8028bd",
       "https://www.baidu.com/"]

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
print(start)
loop.run_until_complete(asyncio.wait(task))
endtime = time.time() - start
print(endtime)
loop.close()
