import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'mem ')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def hi(ctx):
    await ctx.send('hi')

@client.command()
async def lavigne(ctx):
    await ctx.send(':heart::heart_eyes::heart::heart_eyes::heart::heart_eyes::heart:')

@client.command()
async def gay(ctx):
    await ctx.send('gay for u :heart_eyes:')

@client.command()
async def furret(ctx):
    await ctx.send('https://imgur.com/gallery/B9DAYhn')

@client.command()
async def add(ctx, arg1, arg2):
    await ctx.send(float(arg1) + float(arg2))

@client.command()
async def subtract(ctx, arg1, arg2):
    await ctx.send(float(arg1) - float(arg2))

@client.command()
async def multiply(ctx, arg1, arg2):
    await ctx.send(float(arg1) * float(arg2))

@client.command()
async def divide(ctx, arg1, arg2):
    await ctx.send(float(arg1) / float(arg2))



@client.command()
async def spam(ctx):
    await ctx.send('oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   'oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L oops L '
                   )

client.run('NjcxNzYzODU1NjkyNTI5Njg0.XjGpew.19si6G3xfLVeelynXoSZc8wGpmQ')
