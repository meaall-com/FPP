from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
app = Client("gramsession", 14897586, "49db49b537577139a4b337f2764b70a3")


@app.on_message(filters.channel)
def my_function(client, message):
    if message.sender_chat.id != -1001159025906 or message.sender_chat.id != -1001780843936:
        print(message)
        message.forward("@meaallh_for")

my_handler = MessageHandler(my_function)

app.add_handler(my_handler)

app.run()
