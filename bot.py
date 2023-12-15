import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers


#Функция конфигурирования и запуска бота
async def main() -> None:

    #Загрузка конфиг в переменную config
    config: Config = load_config()

    #Инициализация ботa и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    #Пропуск накопившихся апдейтов и запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())