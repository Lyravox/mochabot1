import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()

cat_api = os.getenv("CAT_KEY")
apod_api = os.getenv("APOD_KEY")

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
        
    @nextcord.slash_command(description="Returns a random affirmation")
    async def affirmation(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.affirmations.dev/") as response:
                if response.status == 200:
                    data = await response.json()
                    affirmation = data['affirmation']
                    await interaction.response.send_message(f"Affirmation: {affirmation}")
                else:
                    await interaction.response.send_message("Could not fetch a affirmation :(")
                    
                    
    @nextcord.slash_command(description="Returns the astronomy picture of the day (APOD)")
    async def apod(self, interaction: Interaction):
        apod_url = "https://api.nasa.gov/planetary/apod"
        async with aiohttp.ClientSession() as session:
            params = {'api_key': apod_api}
            async with session.get(apod_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    image_url = data.get("url")
                    explanation = data.get("explanation")
                    embed = nextcord.Embed(title="Astronomy Picture of the Day", color=0x703c2f, description=explanation)
                    embed.set_image(url=image_url)
                    await interaction.response.send_message(embed=embed)
                else:
                    error_msg = await response.text()
                    print(f"Failed to retrive APOD. Status: {response.status}, Error: {error_msg}")
                    await interaction.response.send_message("Failed to retrieve Astronomy Picture of the Day :(")
            
def setup(bot):
    bot.add_cog(Fun(bot))