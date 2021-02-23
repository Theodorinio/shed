import discord
import configparser
from discord.ext import commands
import json
import requests
import praw
import time
import random
import os

####################################################

file = open('token.txt', 'r')
if file.mode == 'r':
    token = file.read()

bot = commands.Bot(command_prefix = '.')

####################################################

@bot.command
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

reddit = praw.Reddit(client_id='llKmkdLHvGKViA',
                     client_secret='CL3APA_ZoK7yWW8EA1-mpe6qd9WS0g',
                     user_agent='Mozilla/5.0 (iPod; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="v1.0.2"))
    print('ACTIVE')

#           red       green     blue     orang     pink      grey      black     white    yellow     blue2     red2    custom1   custom2    custom3   custom4   custom5
colors = [0xE10000, 0x00FF7F, 0x2A57FD, 0xFF5733, 0xF405FF, 0x4D4242, 0xADFF2F, 0xFFFFFF, 0xFFC300, 0x00ECFF, 0xE74C3C, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]


@bot.command()
async def rules2(ctx):
    embed = discord.Embed(title = "— rules for Winter's Den", description = 'Disobeying the rules will result in a ban.', color = 0xffffff)
    embed.add_field(name = 'Rules:', value = "× respect eachother & treat others how you want to be treated, we are a non-toxic community.\n \n× racism, homophobia, hate speech, etc is not allowed. that type of behavior is not/will not be tolerated at all.\n \n× please follow discord tos & guidelines !!!\n \n× no self ads/dm ads you will get banned.\n \n× bringing drama into the server is not tolerated, keep that stuff in dms or drop it.\n \n× any doxxing / ddossing / cp / gore / raiding / hate speech = instant ban\n \n× if you need any help, anyone with these roles will be glad to help out!\n(@winter, @administrator, @moderator).")
    embed.set_footer(icon_url = 'https://cdn.discordapp.com/avatars/355407534376353793/629bc71abbd52d319rrc0fb1baf8623aec.png?size=128', text = f'Made & Written by: {ctx.author.display_name}')
    await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
    embed = discord.Embed(title = 'Test Embed', description = 'KEKW', color = random.choice(colors))
    embed.add_field(name = 'Test', value = "This is an embed")
    embed.set_image(url = f'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FiOSsetups%2Fcomments%2F8nezdt%2Ftest_image%2F&psig=AOvVaw0J7iru3IrUM5rIUBz4V728&ust=1612620841413000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKiVoPb20u4CFQAAAAAdAAAAABAl')
    await ctx.send(embed=embed)

bot.run(os.environ['DISCORD_TOKEN'])