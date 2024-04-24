import nextcord
from nextcord.ext import commands
import aiohttp
import base64

class Moonphase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_endpoint = "https://api.astronomyapi.com/api/v2/studio/moon-phase"
        self.api_key = "username:password"
        
    
        
def setup(bot):
    bot.add_cog(Moonphase(bot))