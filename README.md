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

Let's take apart the following modified example from [the official quickstart guide](https://docs.pycord.dev/en/master/quickstart.html). 
```Python
# Import the pycord library into your runtime. 
import discord

# Assign the discord client to an object, we call client.
# All discord actions will act on this variable.
client = discord.Client()

# This is a function.
# It executes whenever the bot has successfully initialised. 
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

### Important Mechanisms
The basic example had a simple response to a simple message. This is nice, but we'd like to make it do something more useful. The following sections go over some of the important mechanisms in the Pycord API.

#### Safety 
The bot's `on_message` function activates on _every_ message, including those from other bots and itself. It's best to design precautions of this into the start of the function.

To stop execution if the message came from the bot itself:
```Python
if message.author == client.user:
    return
```

Or, to stop execution if the message came from a bot (including itself):
```Python
if message.author.bot:
    return
```

#### Messages
Every message the bot receives, goes through the `on_message` function. This includes channel messages and DMs. 

The message is represented with a Message object. You can access important information and perform function with that object, including:
  * Content string with `content`
  * User object with `author`
  * Creation time/date with `created_at`
  * Others documented [here](https://docs.pycord.dev/en/master/api.html#message)
  
For example, if you wanted to print a message if a user with a specific name messaged it:
```Python
if message.author.name == 'meetowl':
    print('ughh my boss is bugging me again')
```

If you then wanted to reply to that message:
```Python
await message.reply('Hey Boss, I'm still working on those reports.')
```

Or send a new message to the channel of that message:
```Python 
await message.channel.send('Working hard or hardly working?')
```

Or do something only if the message matches a specific string:
```Python
if message.content == 'I need you to work overtime':
    await message.reply('I quit')
    
if message.content == 'I've got pizza, how about some overtime?':
    await message.reply('You don't pay me enough to eat so I'm forced to do overtime.')
```

You can find a runnable example with all of this [here](https://github.com/swanhack/discord-bots-session/blob/master/examples/Message.py).

#### Python Strings
You don't want to be hardcoding messages like above. You can use Python's strings to make it much more useful and flexible. You can take a quick look at an overview of Python strings [here](https://www.w3schools.com/python/python_strings.asp), and the full list of functions on strings [here](https://www.w3schools.com/python/python_ref_string.asp).

If you want to only act on messages that start with a specific string:
```Python
if message.content.startswith('!time'):
    date_time_now = datetime.now()
    await message.channel.send(datetime_now)
```

If you want to only act on messages that contains a specific string:
```Python
if 'burger king' in message.content:
    await message.reply('Don't say that around me.')
```

If you want to split a string into words (separated by spaces), and iterate through all of them:
```Python
splitMsg = message.content.split(' ')
for word in splitMsg:
    print(f'{word}')
```

You may also find array slicing useful for the last one. To only work on all but the first word, use splitMsg[1:], which translates to a new array, that contains all elements from 1:
```Python
splitMsg = message.content.split(' ')
for word in splitMsg[1:]:
    print(f'{word}')
```

There are many more things you can do with strings. A runnable example of the above can be found [here](https://github.com/swanhack/discord-bots-session/blob/master/examples/String.py).

### General tips
  * Always put `await` before a discord API call. This is due to how the API works.
  * Have a separate file for your bot API so you don't accidentally share it. We have it in the source file here for simplicity.
  * Python is full of APIs and is often referred to as a "glue language", so don't be afraid to use other APIs with your discord bot!
  * Take a look at the developer portal again, and see how many more permissions the bot can have. Those are all things that the bot can have control over.
## Next steps
  * Write a method that can reverse an input, for example "Something!" -> "!gnihtemoS"
  * Write a function to count and output the total number of times a word has been said
  * Write a function to sort a list of numbers

## Harder next steps

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

## Contributions to swan_hack
We currently have need for two bots that I can't find the time to write. If you want to get started / improve your GitHub portfolio, or just want to build something that will be used with discord bots, we encourage you to try solving these two issues:
  * Bot that can manage channels within a category. Specifically for our Miscellaneous category.
  * Bot that combines all messages from a channel, within a date range, into a text, PDF, DOCX or other file. For a small event we want to run. 



# Resources

Resources used and suggested
  * [Pycord library](https://pycord.dev/)
  * [Official Pycord documentation](https://docs.pycord.dev/en/master/quickstart.html)
  * [Python installation guide](https://wiki.python.org/moin/BeginnersGuide/Download)
  * [Python Strings tutorial](https://www.w3schools.com/python/python_strings.asp)
  * [Python Strings methods](https://www.w3schools.com/python/python_ref_string.asp)
