import telebot

botToken = "5880422234:AAGsrGQG4eHvOQyNfLe2Hb_lu361VkqfWZs"
bot = telebot.TeleBot(botToken)


@bot.message_handler(content_types=['text'])
def sendMessage(message):
    file = open("index.html", "w")
    file.write(message.text)
    file.close()
    bot.send_message(message.chat.id,message.text)

bot.polling(none_stop=True)
