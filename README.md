# Discord Bots!

Welcome to our Discord Bots session! This session aims to get you to become more comfortable with how discord bots work, and allow you to make one for yourselves.

For those already comfortable, please skip to the final section where we~~can use you for free labour~~ have some challenges for you!

## Setting up a Discord Bot

Before you can get to programming, we need to create and register your bot with the swan_hack server. 
    1. Open up the [Discord Developers Page](https://discordapp.com/developers/applications/me)
    2. Create a new application with the top-left "New Application" button. Call it something silly.
    3. Your application should appear in the "My Applications" list. Open it up, go to the "Bot" page, and click "Add Bot".
    4. Right below the username, you will see your "API" token. Make sure you ~~share that with everybody~~ keep it concealed! This is your "password" to the bot.
    5. Go to the "OAuth2 -> URL Generator" section
       - Here, we will generate the link that will let me add your bot to our server, or any server for that matter.
       - You first define the "scope" of the bot, for this you just need "Bot"
       - You must then define what the bot needs access to. For this basic one, it simply needs "Read Messages/View Channels" and "Send Messages"
       - After you ticked all the boxes, copy the url from the "Generated URL" field, and save it.
    6. Send the generated URL above to meetowl#3690 (me), I will then notify you when I've added the bot. You should see the bot in the right pane of the `#sandbox` text channel.

## Writing your Bot

Now, time to actually do something with your bot!  With Python the easiest way to get started is to use the [discord.ext.commands](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html) framework from the [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) API.

To install this library on your machine type the following into a terminal:

```bash
python3 -m pip install -U discord.py
```

Now lets start writing your bot.. with everyone's favourite boilerplate:

```Python
from discord.ext import commands

# Because it acts like a password it is best practice to store your API token in an external text file
TOKEN_FILE = open("/path/to/token", "r")
TOKEN = TOKEN_FILE.read()
```

First, to prevent accidental usage, we recommend you set up a character to start all of your commands with:

```Python
# All your commands must start with this prefix for your bot to respond
bot = commands.Bot(command_prefix='>')
```

Secondly, to prevent spam, your bot should only respond to messages from you, so add a check for this:

```Python
bot.owner_id = # your USER_ID
```

To get your USER_ID right click on your name in Discord and select "copy ID", this will then allow you to paste it into your code.

With this all setup we can finally start writing some commands!   In the following example the `ping` command is run when you send ">ping".

```Python
@commands.is_owner()
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@commands.is_owner()
@bot.command()
async def logout(ctx):
    await ctx.bot.logout()
```

Finally, some code to actually run your bot:

```Python
bot.run(TOKEN)
```

Now you should be able to start up your bot by typing the following into a terminal:

```bash
python3 /path/to/file.py
```

## Next steps

* Prevent your Bot from replying to itself, spam has been known to occur!
* Write a method that can reverse an input, for example "Something!" -> "!gnihtemoS"
* Write a method than returns the total number of users on the server
  * Make this output display how many are bots and how many are actively online
* Write a function to count and output the total number of times a word has been said
* Write a function to sort a list of numbers

## Slightly harder next steps

These challenges can take some time but are possible in most languages, including Java!

* Write a function to create commands dynamically
  * For example "create test this is not a test" creates a command "test" which returns "this is not a test"
  * Write a function to remove dynamic commands
* Write a function to encrypt an input like Enigma
  * Write a function to decrypt the output back to the input
  * Ideally these should not be cyclical (decrypting text and then encrypting it should not return the input)
* Use a third party API to pull weather data for a given location
  * Have this command also output an image representing the weather conditions
  * Reminder: Some cities share names with other cities in another country so don't forget to also take in a country or region, for example [Swansea,US](https://en.wikipedia.org/wiki/Swansea,_Massachusetts)
* Now write a help function because you know you'll forget this nonsense!

## Rules for having a bot on the swan_hack server

For a list of rules your bot should follow please check the `#info` channel on the swan_hack server.

## And for those who left their brain outside

Feel free not to [build a bot in Java!](https://github.com/Javacord/Javacord)

Although it is possible..

![Don't do this!](https://github.com/swanhack/Discord-Bots---Episode-10/blob/master/SomethingWentWrong.png)

# Resources

Resources used and suggested
    - [OFficial guide](https://docs.pycord.dev/en/master/quickstart.html)
