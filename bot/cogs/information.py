import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Returns bot latency")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! My latency is {latency}ms.")
        
    @nextcord.slash_command(description="Returns server info")
    async def server(self, interaction: Interaction):
        server = interaction.guild
        name = server.name
        icon = server.icon.url
        creation = server.created_at.strftime("%b %d %Y - %H:%M")
        owner = server.owner
        members = server.member_count
        id = server.id
        embed = nextcord.Embed(title=f"{name}", color=0x703c2f)
        embed.add_field(name="Owner", value=owner)
        embed.add_field(name="Member Count", value=members)
        embed.set_footer(text=f"ID: {id} | Created • {creation}")
        embed.set_thumbnail(icon)
        await interaction.response.send_message(embed=embed)
        
        
    @nextcord.slash_command(description="Returns a users avatar")
    async def avatar(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        avatar = str(member.avatar.url)
        name = member.name
        embed = nextcord.Embed(
            title=f"{name}'s Avatar", color=0x703c2f)
        embed.set_image(avatar)
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Information(bot))