import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

intents =  nextcord.Intents.all()
intents.guilds = True
intents.members = True
intents.bans = True
intents.emojis = True
intents.integrations = True
intents.webhooks = True
intents.invites = True
intents.voice_states = True
intents.messages = True
intents.guild_messages = True
intents.dm_messages = True
intents.reactions = True
intents.guild_reactions = True
intents.dm_reactions = True
intents.typing = True
intents.guild_typing = True
intents.dm_typing = True
intents.presences = True

bot = commands.Bot(
    intents=intents,
    status=nextcord.Status.online,
    activity=nextcord.Game(name="in development!")
)

bot.load_extension('cogs.information')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.affirmation')
bot.load_extension('cogs.moonphase')

@bot.event
async def on_ready():
    print()
    print(f"Logged in as {bot.user} [{bot.application_id}]")
    print()
    
bot.run(token)