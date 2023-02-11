from keys import chat_key, tg_key
import openai
import telebot

bot = telebot.TeleBot(tg_key)
openai.api_key = chat_key


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Ask me something!')


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )

    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


if __name__ == "__main__":
    bot.polling()
