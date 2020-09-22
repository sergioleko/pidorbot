import discord
import random
from discord.ext import commands
from discord.utils import get

from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(
        f'Hello, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def roll(ctx):
    author = ctx.message.author
    coin = random.randint(0, 1)
    if coin == 1:
        side = 'Орёл ебать'
    else:
        side = 'Решка нахуй'

    await ctx.send(
        f'{author.mention}, Roll is ' + side
    )

@bot.command()
async def kiss(ctx):
    author = ctx.message.author
    randomUser = random.choice(ctx.message.channel.guild.members)
    emoji = bot.get_emoji(583573593125027850)
    await ctx.send(
        f'Эй, {randomUser.name} , {author.name} поцеловал тебя {emoji}'
    )

bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
