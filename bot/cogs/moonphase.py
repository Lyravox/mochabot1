import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import aiohttp
import base64
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()

class Moonphase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_endpoint = "https://api.astronomyapi.com/api/v2/studio/moon-phase"
        self.application_id = os.getenv("ASTRONOMY_APPLICATION_ID")
        self.application_secret = os.getenv("ASTRONOMY_APPLICATION_SECRET")

    async def get_moon_phase(self):
        auth_bytes = f'{self.application_id}:{self.application_secret}'.encode('utf-8')
        auth_header = base64.b64encode(auth_bytes).decode('utf-8')
        headers = {
            'Authorization': f'Basic {auth_header}'
        }
        body = {
            "format": "png",
            "style": {
                "moonStyle": "default",
                "backgroundStyle": "stars",
                "backgroundColor": "black",
                "headingColor": "white",
                "textColor": "white"
            },
            "observer": {
                "latitude": 6.56774,
                "longitude": 79.88956,
                "date": str(date.today())
            },
            "view": {
                "type": "portrait-simple",
                "orientation": "south-up"
            }
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_endpoint, headers=headers, json=body) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['data']['imageUrl']
                else:
                    body = await response.text()
                    print(f"Failed to fetch moon phase image: HTTP {response.status}, Response Body: {body}")
                    return None
                    
                
    @nextcord.slash_command(description="Returns a image of the current moonphase")
    async def moonphase(self, interaction: Interaction):
        image_url = await self.get_moon_phase()
        if image_url:
            embed = nextcord.Embed(title="Current Moon Phase", color=0x703c2f)
            embed.set_image(url=image_url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Could not fetch the moon phase image :(")
            
        
def setup(bot):
    bot.add_cog(Moonphase(bot))