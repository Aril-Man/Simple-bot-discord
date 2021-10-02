import discord
import random

from discord import client
from discord import message
from discord import channel
from discord import colour
from discord import embeds
from discord.colour import Color

TOKEN = 'ODkzNDQzMTM4NjU4NjM5ODgy.YVbhww.03SR6omNn7I9SgpBG83oWuA0WSg'

client = discord.Client()

@client.event
async def on_read():
    print('We have logger in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
    
    if message.author == client.user:
        return
    
    if message.channel.name == 'bot-command':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hallo {username}')
            return
        elif user_message.lower() == 'hi':
            await message.channel.send(f'Hi {username}')
            return
        elif user_message.lower() == '!status':
            await message.channel.send(f'Me Online')
            return
        elif user_message.lower() == '!random':
            response = f'Ini adalah No ramdom kamu : {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!absenPKL':
            response = f'Nihhh absen nyaa : https://forms.gle/Rf6EGMP1TAQYusCW8'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!18+':
            response = f'Astaghfirullah, Kamu mau apaa? Taubat HEYYY!!'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!jurnal':
            response = f'Nihh link nya : https://forms.gle/Biw8HFgdruMqvev66'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!help':
            myEmbed = discord.Embed(
                title = "HELPPPP!!!",
                description = 'Cari tahu di sini!',
                color = discord.Colour.dark_blue()
            )
            myEmbed.add_field(name="!random", value='Menampilkan No ramdom' ,inline=False)
            myEmbed.add_field(name="!absenPKL", value='Absen PKL' ,inline=False)
            myEmbed.add_field(name="!jurnal", value='Isi jurnal jangan lupa tiap minggu' ,inline=False)
            myEmbed.add_field(name="!18+", value='Please jangan di ketik' ,inline=False)
            await message.channel.send(embed=myEmbed)
            return
        else:
            response = f'Ketik apeee, kaga ngerti gw'
            await message.channel.send(response)
            return    
    
client.run(TOKEN)