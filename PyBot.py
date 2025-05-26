#!/usr/bin/env python
# bot.py  — Telegram-бот: по нажатию кнопки шлёт видео-файл из папки videos/

# 1) Загружаем переменные окружения из .env (или из системы)

import subprocess
import sys
from dotenv import load_dotenv
load_dotenv()

import os
from pathlib import Path
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputFile,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
subprocess.Popen([sys.executable, "parse.py"])
# 2) Берём токен, проверяем, что он есть
TOKEN = os.getenv("TG_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "TG_TOKEN не найден — задайте его в .env "
        "или как переменную окружения!"
    )

# 3) Папка с видео (положите файлы сюда, рядом с ботом)
VIDEO_DIR = Path("downloads")

# ────────────────────────────────────────────────────────────
# ФУНКЦИИ-ХЭНДЛЕРЫ

def make_keyboard() -> InlineKeyboardMarkup:
    """Строим клавиатуру из имён файлов."""
    buttons = [
        [InlineKeyboardButton(text=path.stem, callback_data=path.name)]
        for path in VIDEO_DIR.iterdir() if path.is_file()
    ]
    # Если файлов нет — одна «заглушка»
    if not buttons:
        buttons = [[InlineKeyboardButton("Нет видео", callback_data="NONE")]]
    return InlineKeyboardMarkup(buttons)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start — показать меню."""
    await update.message.reply_text(
        "Выберите видео:",
        reply_markup=make_keyboard(),
    )


async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляем выбранное видео."""
    query = update.callback_query
    await query.answer()

    # «NONE» — клик по заглушке, просто молчим
    if query.data == "NONE":
        return

    file_path = VIDEO_DIR / query.data
    if not file_path.exists():
        await query.message.reply_text("Файл не найден 😔")
        return

    # < 4 ГБ — можно как video, иначе отправляйте как document
    with file_path.open("rb") as f:
        await query.message.reply_video(
            video=InputFile(f, filename=file_path.name),
            caption=f"📹 {file_path.stem}",
        )


# ────────────────────────────────────────────────────────────
# ТОЧКА ВХОДА

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(send_video))

    print("Бот запущен — Ctrl+C для остановки")
    app.run_polling()


if __name__ == "__main__":
    main()
