import discord
from discord.ext import commands
#import keep_alive
TOKEN = ''  #輸入DC bot的token
bot = commands.Bot(command_prefix='')

#這裡開始打程式

# @bot.event
# async def on_ready():
#     print("Hi")




#keep_alive.keep_alive()
bot.run(TOKEN)