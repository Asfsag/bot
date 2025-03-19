from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8028359650:AAFF_az15KTuFFhBEyVb63m941D-sHB0HPY"

# Замените все AUDIO_FILE_ID на реальные file_id аудио из Telegram
AUDIO_FILES = {
    "Вступление": "CQACAgIAAxkBAAPXZ9VnX8iRUJOyNdQi0-EYqCmdn9cAAotnAALLgrFKS3RK-GjlbwI2BA",  # Аудио для вступления
    "О выставке": "CQACAgIAAxkBAAPZZ9Vne8R0yz6ESi7XTaKDizN4PQMAAoxnAALLgrFKhojcO-xQuDw2BA",  # Аудио о выставке
    "РОЗОВЫЙ": [
        "CQACAgIAAxkBAAPbZ9VnmhPj42nOpbVtY5Od4wg4aN0AApFnAALLgrFKTD_lZqJ_h542BA",  # Греческое лето
        "CQACAgIAAxkBAAPdZ9VnpvkHRN_vgrOSm9a0m0LMjfsAApRnAALLgrFKf-9pqDLR51Q2BA",  # Солнце
        "CQACAgIAAxkBAAPoZ9Vn65pkAAEufZPHgX-YSATnPHy8AAKYZwACy4KxSnhtMSc1Q6W_NgQ",  # Голос сердца
        "CQACAgIAAxkBAAPqZ9Vn-URnQf22lMkvK-9uO0bs3YAAAppnAALLgrFKqASIUE62T8k2BA",  # Бусики
    ],
    "ЗЕЛЁНЫЙ": [
        "CQACAgIAAxkBAAPsZ9VoKQfFnkGEelEpDHfBdFEDqOYAAptnAALLgrFKj69rJiZWW1I2BA",  # Жизнь
        "CQACAgIAAxkBAAPuZ9VoKvhpmup7na9S_gSAKKTC-KsAAp1nAALLgrFK_dPAb9ySkWQ2BA",  # Прыжок
        "CQACAgIAAxkBAAPwZ9VoLLiobuiWAdJID3zuJGj3eMwAAp5nAALLgrFKOFApEJxjSHw2BA",  # Гречанки
    ],
    "СИНИЙ": [
        "CQACAgIAAxkBAAPyZ9VoanZ7a5zG0s-exDvGsJp_9-UAAqRnAALLgrFKiEMoAWD_NLg2BA",  # Играющий с ветром
        "CQACAgIAAxkBAAP0Z9VocrUKAVwImd4lnoRNJ3_FW3oAAqVnAALLgrFKEYH7CBrhjWo2BA",  # Про синий цвет
        "CQACAgIAAxkBAAP2Z9Vod7BPtoQHyaE04tPcG8ilQTAAAqZnAALLgrFKi1MXlFHCrsQ2BA",  # Про море
    ],
    "ГОЛУБОЙ": [
        "CQACAgIAAxkBAAP4Z9Von5hROw1UYBdenyBYQC5N_2oAAqlnAALLgrFK6EOYoroJK7o2BA",  # Мне бы в небо
        "CQACAgIAAxkBAAP6Z9VopGGsk9O4Eia_caUf2bBKOFgAAqpnAALLgrFKUR1lS_y286s2BA",  # Птицы. Полёт.
        "CQACAgIAAxkBAAP8Z9VoqBLJSyrnRBhW8FcFcOjA-R8AAqtnAALLgrFKBDrUQEgmcUg2BA",  # Про небо
    ],
}

# Функция для создания клавиатуры меню
def get_menu_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["РОЗОВЫЙ", "ЗЕЛЁНЫЙ"],
            ["СИНИЙ", "ГОЛУБОЙ"]
        ],
        resize_keyboard=True
    )

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Отправляем фото (замените PHOTO_FILE_ID на реальный file_id)
    await update.message.reply_photo(
        photo="AgACAgIAAxkBAAIC82faxc9Y43XWYLdOGiCgDQIubIjsAAKV8TEbMKjZSjAR3ODdTMlhAQADAgADeQADNgQ",
        caption=(
            'Добро пожаловать на мою выставку "СЧАСТЬЕ" в музее современного искусства "Артмуза".\n\n'
            'Я записала этот аудио-гид в дополнение к экспозиции, чтобы вы могли почувствовать и понять моё искусство чуточку лучше❤️\n\n'
            'Тут вы найдёте рассказы почти ко всем картинам, которые представлены на выставке.\n\n'
            'Тут вы найдёте рассказы почти ко всем картинам, которые представлены на выставке.\n\n'
            'Тут вы найдёте рассказы почти ко всем картинам, которые представлены на выставке.\n\n'
            'Тут вы найдёте рассказы почти ко всем картинам, которые представлены на выставке.\n\n'
        )
    )

    # Отправляем аудио "Вступление" и "О выставке"
    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=AUDIO_FILES["Вступление"]
    )
    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=AUDIO_FILES["О выставке"]
    )

    # Показываем меню с разделами
    await update.message.reply_text(
        "",
        reply_markup=get_menu_keyboard()
    )

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    # Обработка разделов цветов
    if text in ["РОЗОВЫЙ", "ЗЕЛЁНЫЙ", "СИНИЙ", "ГОЛУБОЙ"]:
        await update.message.reply_text(f"Раздел {text}:")
        for audio_file_id in AUDIO_FILES[text]:
            await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=audio_file_id
            )
        # Показываем меню снова после отправки аудио
        await update.message.reply_text(
            "",
            reply_markup=get_menu_keyboard()
        )
        return

# Обработчик для получения file_id любого файла
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = None

    # Проверяем тип файла и получаем file_id
    if update.message.photo:
        file_id = update.message.photo[-1].file_id  # Для фото
    elif update.message.audio:
        file_id = update.message.audio.file_id  # Для аудио
    elif update.message.document:
        file_id = update.message.document.file_id  # Для документов
    elif update.message.video:
        file_id = update.message.video.file_id  # Для видео
    elif update.message.voice:
        file_id = update.message.voice.file_id  # Для голосовых сообщений

    # Отправляем file_id пользователю
    if file_id:
        await update.message.reply_text(f"File ID вашего файла: {file_id}")
    else:
        await update.message.reply_text("Этот тип файла не поддерживается.")

def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.PHOTO | filters.AUDIO | filters.Document.ALL | filters.VIDEO | filters.VOICE, handle_file))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
