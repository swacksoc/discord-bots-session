# Discord Bots - Episode 10

Why Discord Bots?  Because they're cool, and actually they're really easy to do and can teach you a lot.  Most good languages already have libraries and APIs set up for Discord Bots which makes things super easy.

For these examples I shall be using Python but similar steps can be taken in JavaScript and if you're feeling a particular kind of crazy .. Java, I use Java.

## Setting up a Discord Bot

As expected there are some hoops to jump through, not literally (I hate jumping), before you can get a Discord Bot up and running.  Firstly you need to sign into Discord and navigate to the [Discord Developers Page](https://discordapp.com/developers/applications/me) and hit the "New Application" button, from here you should give your bot a witty name and finally select "Create".

After you've done this you need to scroll down and select "Add Bot User", this basically lets Discord know that you want to make a Bot and to provide the necessary stuff for you.

## Getting your Bot onto the swan_hack server

On the same page you need to select the "Generate OAuth 2 URL" button and hope nothing bad happens.. With any luck this should generate a bunch of options for you to select what you want the Bot to be able to do.  In your case select "be a bot" and then get ready to Coffee Pasta the URL it spits out to a member of the Committee.

## Writing your Bot

Now, time to actually do something with your bot! For Python the easiest way to get started is to use the [discord.ext.commands](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html) framework of the [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) API:

```Python
from discord.ext import commands

TOKEN = "Your Discord API token here"

# All your commands must start with this prefix for your bot to respond
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(TOKEN)
```

## Next steps

.. Something Something ..
