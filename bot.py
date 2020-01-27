from telebot import types
import time
import telebot
bot = telebot.TeleBot("BOT_TOKEN")

def inline_gde():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('🏠Екатерингбург', callback_data='ekb'),
            types.InlineKeyboardButton('🏠Абакан', callback_data='abk'),
            types.InlineKeyboardButton('🏠Минусинск', callback_data='minus'),
    types.InlineKeyboardButton('🏠Черногорск', callback_data='cherno'),
    types.InlineKeyboardButton('🏠Саяногорск', callback_data='saya'))
    return key

def inline_chto ():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('🎁Crystal (White)', callback_data='cryw'),
            types.InlineKeyboardButton('🎁Crystal (Blue)', callback_data='cryb'),
    types.InlineKeyboardButton('🎁Меф', callback_data='mef'),
    types.InlineKeyboardButton('🎁Гашиш', callback_data='gash'))
    return key

def inline_keybord():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('0.5гр-->1200р', callback_data='1'),
            types.InlineKeyboardButton('1гр-->2200р', callback_data='2'),
            types.InlineKeyboardButton('1.5гр-->3200р', callback_data='3'))
    return key

def qiwi():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('🥝QIWI', callback_data='qiwi'))
    return key

def inline_keybordtwo ():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('Проверить оплату', callback_data='check'))
    return key


@bot.message_handler(commands=["start"])
def inline(message):
	bot.send_message(message.chat.id, "Вас приветствует магазин KILLER DILLER\n\nTelegram: TKD24_7KD\n\nУдачных покупок!\n\nДля покупки нажмите свой город из списка снизу:", reply_markup=inline_gde())

x=0

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    global x
    if c.data=='ekb':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🏠 ЕКАТЕРИНБУPГ.\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите товар:",
            parse_mode="markdown",
            reply_markup=inline_chto ())
    elif c.data=='abk':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🏠 АБАКАН.\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите товар:",
            parse_mode="markdown",
            reply_markup=inline_chto ())
    elif c.data=='minus':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🏠 МИНУСИНСК.\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите товар:",
            parse_mode="markdown",
            reply_markup=inline_chto ())
    elif c.data=='cherno':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🏠 ЧЕРНОГОРСК.\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите товар:",
            parse_mode="markdown",
            reply_markup=inline_chto ())
    elif c.data=='saya':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🏠 САЯНОГОРСК.\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите товар:",
            parse_mode="markdown",
            reply_markup=inline_chto ())
    elif c.data=='cryw':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🎁 Crystal (White)\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:",
            parse_mode="markdown",
            reply_markup=inline_keybord())
    elif c.data=='cryb':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🎁 Crystal (Blue)\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:",
            parse_mode="markdown",
            reply_markup=inline_keybord())
    elif c.data=='mef':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🎁 Меф\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:",
            parse_mode="markdown",
            reply_markup=inline_keybord())
    elif c.data=='gash':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 🎁 Гашиш\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:",
            parse_mode="markdown",
            reply_markup=inline_keybord())
    elif c.data=='1':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 0.5гр-->1200р\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите способ оплаты:",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="1200р"
    elif c.data=='2':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 1гр-->2200р\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите способ оплаты:",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="2200р"
    elif c.data=='3':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Вы выбрали 1.5гр-->3200р\n\n➖➖➖➖➖➖➖➖➖➖\nВыберите способ оплаты:",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="3200р"
    elif c.data=='qiwi':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text=f'Переведите на Пополнить баланс через 🥝Qiwi🥝 в течение 3 часов\n➖➖➖➖➖➖➖➖➖➖\nКошелек: ➡️79509618644⬅️\nСумма: {x} рублей\n\n➖➖➖➖➖➖➖➖➖➖\n❗️Оплата неточной суммы - потеря вашего платежа.❗️\n❗️ОПЛАТА РУБЛЬ В РУБЛЬ❗️\n❗️Оплата только ОДНОЙ суммой (сборные суммы не принимаем)❗️',
            parse_mode="markdown",
            reply_markup=inline_keybordtwo ())  
    elif c.data=='check':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Проводится проверка платежа, примерное время ожидания 1-5мин",
            parse_mode="markdown")
        time.sleep(90)
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Платеж не был найден, повторите проверку спястя какое-то время, возможно проблема со стороны киви",
            parse_mode="markdown",
            reply_markup=inline_keybordtwo())
    



if __name__ == "__main__":
    bot.polling(none_stop=True)
