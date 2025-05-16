from time import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
import datetime
import respond_current_data

import bot

async def async_wrapper(coroutine_func, *args, **kwargs):
    await coroutine_func(*args, **kwargs)
    print_message()

def print_message():
    print("job activated")

def startsch(channel):
    trigger = CronTrigger(day_of_week='sun', hour=9, minute=00)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(async_wrapper, trigger, args=[bot.send_weather, channel])
    scheduler.start()

    
        
    




