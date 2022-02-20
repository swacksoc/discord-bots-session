# Import the pycord library into your runtime. 
import discord

# Assign the discord client to an object, we call client.
# All discord actions will act on this variable.
client = discord.Client()

# This is a function.
# It executes whenever the bot has succesfully initialised. 
# In this case, it simply prints "We have logged in ..." to the terminal.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# This function executes whenever the bot has received a new message.
# This can be a DM or a message in a channel that the bot can see.
@client.event
async def on_message(message):
    # If the message starts with $hello, respond with Hello!
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Required to run the bot, make sure to replace <YOUR_API_TOKEN>!
client.run('<YOUR_API_TOKEN>')
