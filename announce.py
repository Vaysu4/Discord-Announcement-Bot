import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = "+")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Streaming(name = "...", url = "https://twitch.tv/..."))
    print(client.user.name)
    print("Online")
    print("-------")


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def a(ctx,*,message,):
    embed = discord.Embed(title='Attention!',description=message,color=00000)
    embed.set_footer(text="Made For ...")
    await ctx.send(embed=embed)



client.run("TokenHere")
