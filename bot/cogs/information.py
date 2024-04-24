import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Returns information about the bot")
    async def info(self, interaction: Interaction):
        await interaction.response.send_message("You can find my Github repository here: https://github.com/Lyravox/mochabot (More info coming soon!)")        
        
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
        
    @nextcord.slash_command(description="Returns info about a specfic user")
    async def user(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        name = member.name
        avatar = str(member.avatar.url)
        embed = nextcord.Embed(title=f"{name}'s Info", color=0x703c2f)
        embed.set_thumbnail(avatar)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Returns a users avatar")
    async def avatar(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        avatar = str(member.avatar.url)
        name = member.name
        embed = nextcord.Embed(title=f"{name}'s Avatar", color=0x703c2f)
        embed.set_image(url=avatar)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Returns a list of server emojis")
    async def emojis(self, interaction: Interaction):
        emojis = interaction.guild.emojis
    
        if not emojis:
            await interaction.response.send_message("No custom emojis found in this guild.")
        emoji_list = [str(emoji) for emoji in emojis] 
        emojis_message = " ".join(emoji_list)
        embed = nextcord.Embed(title="Emoji List", color=0x703c2f)
        embed.add_field(name="", value=emojis_message)
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Information(bot))