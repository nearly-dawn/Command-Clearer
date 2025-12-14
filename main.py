import discord
import os

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    await bot.sync_commands(commands=[], force=True)
    print('All slash commands have been cleared!')
    
    print('Command clearing complete!')

bot.run("YOUR DISCORD BOT TOKEN")
