# Discord Bots!

Welcome to our Discord Bots session! This session aims to get you to become more comfortable with how discord bots work, and allow you to make one for yourselves.

For those already comfortable, please skip to the final section where we~~can use you for free labour~~ have some challenges for you!

## Setting up the bot

To begin, need to create and register your bot with the swan_hack server. 
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

## Setting up your environment

Before you can get to programming, you actually need something to do it with. We will be using Python 3 with the [Pycord library](https://pycord.dev/), but don't get intimidated if you're not familiar, that's the point of this session!

You will need:
  - A text editor. A commonly suggested one is [Visual Studio Code](https://code.visualstudio.com/), but it really doesn't matter as long as you're comfortable with it. You can use windows notepad, if you're into that kind of thing.
  - Python 3. We will only touch what we need in python, the rest is up to you. Follow the installation documents [here](https://wiki.python.org/moin/BeginnersGuide/Download).
  - The Pycord library. Once you've installed python, follow [this page](https://docs.pycord.dev/en/master/installing.html) to get it installed. Should be as easy as entering `py -3 -m pip install -U py-cord` in the command prompt.
  - Once you have everything above, you should be ready to go!

## Writing your bot

Now for the fun part, actually making the bot do something!

### Basic Example 

Let's take apart the following example from [the official quickstart guide](https://docs.pycord.dev/en/master/quickstart.html). 
```Python
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
```

Chuck the above into your text editor, replace `<YOUR_API_TOKEN>` with the token (password) saved earlier, and save it to disk as "firstbot.py". Now, enter the following into a command line or terminal window to run the bot:
```
py firstbot.py
```

Try sending $hello in `#sandbox`!

### blah

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
