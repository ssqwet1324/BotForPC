import telebot
from telebot import types
import pyautogui
from psutil import cpu_percent, virtual_memory, disk_usage
from PIL import ImageGrab                                                              
from tempfile import gettempdir
from subprocess import run, Popen
import os
import time

#Token from botfather
TOKEN = 'Your Token'

bot = telebot.TeleBot(TOKEN)

#initializing buttons
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🖥Информация о ПК')
    item2 = types.KeyboardButton('🌌Открыть приложение')
    item3 = types.KeyboardButton('🔥Взаимодействие с ПК')
    markup.add(item1 , item2, item3)
    bot.send_message(message.chat.id, '👋Привет! Выбери действие:', reply_markup=markup)
    bot.send_message(message.chat.id, '👋Для вызова инструкции напиши /inst', reply_markup=markup)
####

#PC information
@bot.message_handler(func=lambda message: message.text == '🖥Информация о ПК')
def handle_system_info(message):
    info = get_system_info()
    bot.reply_to(message, info)

def get_system_info():
    cpu_usage = cpu_percent()
    ram_usage = virtual_memory().percent
    disk_usagee = disk_usage('/').percent
    system_info = f"Использование CPU: {cpu_usage}%\n"
    system_info += f"Использование RAM: {ram_usage}%\n"
    system_info += f"Использование диска: {disk_usagee}%"

    return system_info
####

#buttons for open app
@bot.message_handler(func=lambda message: message.text == '🌌Открыть приложение')
def handle_open_app(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)         
    item1 = types.KeyboardButton('🔴🎉Открыть Chrome')
    item2 = types.KeyboardButton('📈🧶Открыть uTorrent')
    item3 = types.KeyboardButton('📈🔵Открыть Steam')
    item4 = types.KeyboardButton('⬅️Назад')    
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "🎮Выбери приложение для открытия:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔥Взаимодействие с ПК')
def handle_pc_interaction(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)         
    item1 = types.KeyboardButton('🔄Перезагрузить ПК')
    item2 = types.KeyboardButton('🅾️Выключить ПК')
    item4 = types.KeyboardButton('💪Скриншот')
    item5 = types.KeyboardButton("🧶Взаимодействие с uTorrent")
    item6 = types.KeyboardButton("✈️Сменить окно")
    item3 = types.KeyboardButton('⬅️Назад')      
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, '🗿Выбери действие для ПК:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '⬅️Назад')
def handle_back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🖥Информация о ПК')
    item2 = types.KeyboardButton('🌌Открыть приложение')
    item3 = types.KeyboardButton('🔥Взаимодействие с ПК')
    markup.add(item1 , item2, item3)
    bot.send_message(message.chat.id, '🗿Выбери действие:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔴🎉Открыть Chrome')
def handle_open_app(message):
    try:      
        app_name = message.text.split()[1]
        command = f"start {app_name}"
        Popen(command, shell=True)
        bot.reply_to(message, f"Приложение {app_name} запущено.")
    except Exception as e:
        bot.reply_to(message.chat.id, f"Произошла ошибка: {str(e)}")
        
@bot.message_handler(func=lambda message: message.text == '📈🧶Открыть uTorrent')
def handle_open_torent(message):
    try:
        app_patch1 = r"C:\Users\1\AppData\Roaming\uTorrent\updates\utorrent.exe"
        run([app_patch1])
        bot.reply_to(message, f"Приложение uTorrent запущено.")
    except Exception as e:
        bot.reply_to(message.chat.id, f"Произошла ошибка: {str(e)}")

@bot.message_handler(func=lambda message: message.text == '📈🔵Открыть Steam')
def handle_open_steam(message):
    try:
        app_patch1 = r"C:\Program Files (x86)\Steam\steam.exe"
        run([app_patch1])
        bot.reply_to(message, f"Приложение Steam запущено.")
    except Exception as e:
        bot.reply_to(message.chat.id, f"Произошла ошибка: {str(e)}")


@bot.message_handler(func=lambda message: message.text == '🔄Перезагрузить ПК')
def handle_open_steam(message):
    try:
        os.system('shutdown /r')
        bot.reply_to(message, "ПК будет перезагружен")
    except Exception as e:
        bot.reply_to(message, f"Ошибка при выполнении команды(: {str(e)}")

@bot.message_handler(func=lambda message: message.text == '🅾️Выключить ПК')
def handle_open_steam(message):
    try:
        bot.reply_to(message, f"Через 10 сек комп выключится")
        time.sleep(10)
        os.system("shutdown -s")
        bot.reply_to(message, "Выключение...")
    except Exception as e:
        bot.reply_to(message, f"Ошибка при выполнении команды(: {str(e)}")

@bot.message_handler(func=lambda message: message.text == '✈️Сменить окно')
def handle_open_window(message):
    try:
        pyautogui.hotkey('alt', 'tab')
        bot.reply_to(message, "Окно сменено")
    except Exception as e:
        bot.reply_to(message.chat.id, f"Произошла ошибка: {str(e)}")


@bot.message_handler(func=lambda message: message.text == '🧶Взаимодействие с uTorrent', content_types=['text']) # считываем
def handle_open_browserr(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button_start_download = telebot.types.InlineKeyboardButton(text="Начать загрузку", callback_data="start_download") #добовляем кнопки
    button_pause_download = telebot.types.InlineKeyboardButton(text="Пауза", callback_data="pause_download") #добовляем кнопки
    markup.row(button_start_download, button_pause_download)
    bot.send_message(message.chat.id, "Что делаем?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_queryy(call):
    try:
        if call.data == "start_download":
            pyautogui.rightClick(847, 212)
            pyautogui.leftClick(906, 417)
            bot.answer_callback_query(call.id, text="Загрузка пошла")
        elif call.data == "pause_download":
            pyautogui.rightClick(847, 212)
            pyautogui.leftClick(906, 423)
            bot.answer_callback_query(call.id, text="Пауза")
    except Exception as e:
        bot.answer_callback_query(call.id, text=f"Ошибка при выполнении команды: {str(e)}")

@bot.message_handler(func=lambda message: message.text == '💪Скриншот', content_types=['text'])
def echo_message(message):
    try:
        path = gettempdir() + 'screenshot.png'
        screenshot = ImageGrab.grab()
        screenshot.save(path, 'PNG')
        bot.send_photo(message.chat.id, open(path, 'rb'))
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    bot.polling()

   