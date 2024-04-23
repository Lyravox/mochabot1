import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()

cat_api = os.getenv("CAT_KEY")

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Returns a random cat image")
    async def cat(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as response:
                if response.status == 200:
                    data = await response.json()
                    cat_url = data[0]['url']
                    embed = nextcord.Embed(title="Random Cat", color=0x703c2f)
                    embed.set_image(url=cat_url)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message("Could not fetch a cat image :(")
        
def setup(bot):
    bot.add_cog(Fun(bot))