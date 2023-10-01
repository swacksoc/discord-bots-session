# Import the pycord library into your runtime. 
import disnake
from datetime import datetime

bot = disnake.Client()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.startswith('!time'):
        date_time_now = datetime.now()
        await message.channel.send(date_time_now)

    if 'burger king' in message.content:
        await message.reply('Don\'t say that around me.')

    if message.content.startswith('!vertify'):
        splitMsg = message.content.split(' ')
        for word in splitMsg[1:]:
            await message.channel.send(word)

# Required to run the bot, make sure to replace <YOUR_API_TOKEN>!
bot.run('<YOUR_API_TOKEN>')
