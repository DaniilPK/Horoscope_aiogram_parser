import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp.web import AppRunner, TCPSite
from aiohttp.web_app import Application

from handlers import register_router

logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
APP_BASE_URL = getenv("APP_BASE_URL")

storage = MemoryStorage()
bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/update")


async def main():
    dp["base_url"] = APP_BASE_URL
    dp.startup.register(on_startup)

    app = Application()

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(app, path="/update")
    setup_application(app, dp, bot=bot)

    logger.info("Starting bot")

    register_router(dp)

    runner = AppRunner(app)

    await runner.setup()
    site = TCPSite(runner, host="127.0.0.1", port=5000)
    await site.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    asyncio.run(main())
