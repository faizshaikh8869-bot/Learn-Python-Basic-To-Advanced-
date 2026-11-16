import asyncio

async def fetch():
    data = {"Name": "Faiz", "age": 20}
    print("Started Fetching...")
    
    await asyncio.sleep(5)
    print("Fetching Complete")

    return data

"""
Python has corotine With are A Little similar to go rotine Like they have some similar properties 
Like 
 When started a task that task will  finish first and then anoter task will be executed 
 until that step is done till that time program is idle
"""
async def server():
    print("Server Started")
    task = fetch()
    task2 = fetch()

    resut = await task
    resut2 = await task2

    print(resut)
    print(resut2)
    print("Task Done")

asyncio.run(server())