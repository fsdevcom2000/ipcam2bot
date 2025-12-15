import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties

from monitoring.monitor import MonitoringController
from monitoring.detector import HumanDetector
from monitoring.db import CameraRepository

from handlers.user import user_private_router
from settings import config


bot = Bot(token=config.API_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))


async def start_bot():
    await bot.send_message(int(config.ADMIN_CHAT_ID), f'Start')


async def stop_bot():
    await bot.send_message(int(config.ADMIN_CHAT_ID), f'Stop')


async def main():

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    dp = Dispatcher()
    
    dp.include_router(user_private_router)

    repo = CameraRepository("cameras.db")
    detector = HumanDetector()
    monitor = MonitoringController(bot, repo, detector)

    async def start_monitoring():
        asyncio.create_task(monitor.run())

    dp.startup.register(start_monitoring)
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

   
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # await bot.set_my_commands(
        #     commands=private,
        #     scope=types.BotCommandScopeAllPrivateChats()
        # )
        await dp.start_polling(
            bot,
            allowed_updates=['MESSAGE', 'CALLBACK_QUERY', 'INLINE_QUERY']
        )

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())