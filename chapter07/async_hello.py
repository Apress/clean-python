import asyncio

async def hello(first_print, second_print):
    print(first_print)
    await asyncio.sleep(1)
    print(second_print)
 
asyncio.run(hello("Welcome", "Good by"))    
# Welcome  
# Good by 
