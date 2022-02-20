# Import the pycord library into your runtime. 
import discord

client = discord.Client()

# Make sure to replace this with your username
USERNAME = '<YOUR_USERNAME>'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Make sure its responding to people
    if message.author.bot:
        return

    if message.author.name == USERNAME:
        # This code only acts on USERNAME
        ## Prints to cmd
        print('ughh my boss is bugging me again')
        
        if message.content == 'I need you to work overtime':
            await message.reply('I quit')
        elif message.content == 'I\'ve got pizza, how about some overtime?':
            await message.reply('You don\'t pay me enough to eat so I\'m forced to do overtime.')
        else:
            await message.reply('Hey Boss, I\'m still working on those reports.')
    else:
        # This code affects everyone else
        await message.channel.send('Working hard or hardly working?')
        

    
# Required to run the bot, make sure to replace !
client.run('<YOUR_API_TOKEN>')
