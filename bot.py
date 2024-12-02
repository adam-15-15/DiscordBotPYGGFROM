import discord
from discord.ext import commands

# Remplace par le token de ton bot
TOKEN = "MTMxMzIwMTQxMDI3MTA4NDU1NA.GFjkFh.VKHGyTuQCjBwjnby57pq2_elD4vVp9lOItfAgo"

# Initialisation du bot avec les intents
intents = discord.Intents.default()
intents.messages = True  # Permet d'écouter les messages (ou ajuste les intents selon tes besoins)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est maintenant en ligne !")

# Démarrage du bot
bot.run(TOKEN)
