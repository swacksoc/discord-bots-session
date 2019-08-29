# Discord Bots - Episode 10

Why Discord Bots?  Because they're cool, and actually they're really easy to do and can teach you a lot.  Most good languages already have libraries and APIs set up for Discord Bots which makes things super easy.

For these examples I shall be using Python but similar steps can be taken in JavaScript and if you're feeling a particular kind of crazy .. Java, I use Java.

## Setting up a Discord Bot

As expected there are some hoops to jump through, not literally (I hate jumping), before you can get a Discord Bot up and running.  Firstly you need to sign into Discord and navigate to the [Discord Developers Page](https://discordapp.com/developers/applications/me) and hit the "New Application" button, from here you should give your bot a witty name and finally select "Create".

After you've done this you need to scroll down and select "Add Bot User", this basically lets Discord know that you want to make a Bot and to provide the necessary stuff for you.

## Getting your Bot onto the swan_hack server

On the same page you need to select the "Generate OAuth 2 URL" button and hope nothing bad happens.. With any luck this should generate a bunch of options for you to select what you want the Bot to be able to do.  In your case select "be a bot" and then get ready to Coffee Pasta the URL it spits out to a member of the Committee.

## Writing your Bot

Now, time to actually do something with your bot!  With Python the easiest way to get started is to use the [discord.ext.commands](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html) framework from the [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) API.

Start with the boilerplate:

```Python
from discord.ext import commands

# Because it acts like a password it is best practice to store your API token in an external text file
TOKEN_FILE = open("/path/to/token", "r")
TOKEN = TOKEN_FILE.read()
OWNER_ID = # Change this to your USER_ID
```

To get your USED_ID right click on your name in Discord and select "copy ID"

Your bot should only respond to messages from you, so add a check for this:

```Python
@bot.check
def isOwner(ctx):
    async def predicate(ctx):
        return ctx.author.id == OWNER_ID
    return commands.check(predicate)
```

Now we can write some commands!  First though you shouldse up a character to start all your commands with.  In the following example, the `ping` command is run when you send ">ping".

```Python
# All your commands must start with this prefix for your bot to respond
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def logout(ctx):
    await ctx.bot.logout()
```

Finally, run your bot:

```Python    
bot.run(TOKEN)
```

## Next steps

* Prevent your Bot from replying to itself, spam has been known to occur!
* Write a method that can reverse an input, for example "Something!" -> "!gnihtemoS"
* Write a method than returns the total number of users on the server
  * Make this output display how many are bots and how many are actively online
* Write a function to count and output the total number of times a word has been said
* Write a function to sort a list of numbers

## Slightly harder next steps

* Write a function to create commands dynamically
  * For example "create test this is not a test" creates a command "test" which returns "this is not a test"
  * Write a function to remove dynamic commands
* Write a function to encrypt an input like Enigma
  * Write a function to decrypt the output back to the input
  * Ideally these should not be cyclical (decrypting text and then encrypting it should not return the input)
* Use a third party API to pull weather data for a given location
  * Have this command also output an image representing the weather conditions
  * Reminder that some cities share names with other cities in another country so don't forget to also take in a country or region, for example Manchester,UK or Birmingham,US
* Now write a help function because you know you'll forget this nonsense!

.. Something Something ..
