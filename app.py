from aiogram import executor
import django
import os
from loader import dp
import filters
from utils.notify_admins import on_startup_notify
from django_project.telegrambot.telegrambot import settings


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_project.telegrambot.telegrambot.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()
    import handlers, middlewares
    executor.start_polling(dp, on_startup=on_startup)
