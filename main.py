# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='$',intents=intents)
path = './tarotCards/'
dir_list = os.listdir(path)

# folder path
dir_path = r'./tarotCards/'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$tarot'):
        getNbr = message.content.split()
        for nbr in range(int(getNbr[1])):
            i = random.randint(0, count) - 1
            file_path = f'./tarotCards/{dir_list[i]}'
            await message.channel.send(file=discord.File(file_path))


bot.run('asd')
